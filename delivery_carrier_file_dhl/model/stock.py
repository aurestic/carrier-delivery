# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 FactorLibre (http://www.factorlibre.com)
#                  Hugo Santos <hugo.santos@factorlibre.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import unicodedata
import os
from jinja2.sandbox import SandboxedEnvironment
from datetime import datetime
from openerp import models, api, exceptions, _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from .dhl_tools import dhl_format_zip


def _to_ascii(text):
    text = unicode(text)
    return unicodedata.normalize('NFKD', text).encode(
        'ascii', 'ignore')

mako_template_env = SandboxedEnvironment(
    block_start_string="<%",
    block_end_string="%>",
    variable_start_string="${",
    variable_end_string="}",
    comment_start_string="<%doc>",
    comment_end_string="</%doc>",
    line_statement_prefix="%",
    line_comment_prefix="##"
)
mako_template_env.globals.update({
    'str': str,
    'to_ascii': _to_ascii,
    'int': int
})


class ShippingLabel(models.Model):
    _inherit = 'shipping.label'

    @api.model
    def _get_file_type_selection(self):
        res = super(ShippingLabel, self)._get_file_type_selection()
        res.append(('epl', 'EPL'))
        res = list(set(res))
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def _dhl_country_service(self, country):
        self.ensure_one()
        dhl_country_service_env = self.env['dhl.country.service']
        country_services = dhl_country_service_env.search([
            ('country_id', '=', country.id)
        ])
        if not country_services:
            raise exceptions.Warning(
                _('DHL service for country {} not found').format(
                    country.code))
        return country_services[0]

    @api.multi
    def _dhl_facility_code(self):
        self.ensure_one()
        dhl_zipcode_facility_env = self.env['dhl.zipcode.facility']
        dhl_zip = dhl_format_zip(self.partner_id.country_id.code,
                                 self.partner_id.zip)
        facility = dhl_zipcode_facility_env.search([
            ('zipcode', '=', dhl_zip)
        ])
        if not facility:
            raise exceptions.Warning(
                _('No DHL Facility found for zipcode {}').format(dhl_zip))
        return facility

    @api.multi
    def _dhl_routing_code(self):
        self.ensure_one()
        country_service = self._dhl_country_service(self.partner_id.country_id)
        routing_code = "2L{}{}+{}000{}".format(
            self.partner_id.country_id.code,
            dhl_format_zip(self.partner_id.country_id.code,
                           self.partner_id.zip),
            country_service.service_number.zfill(3),
            "000"  # Suma Codigos especificos de servicio DHL
        )
        legible_routing_code = "({}) {}".format(routing_code[0:2],
                                                routing_code[2:-1])
        return routing_code, legible_routing_code

    @api.multi
    def _dhl_licence_plate_code(self, dhl_config, carrier_tracking_ref):
        self.ensure_one()
        year = str(datetime.now().year)[-1:]
        licence_plate_code = "JJD00{}{}{}{}0".format(
            "006",  # Origin country Code ¿006 para ES?
            dhl_config.dhl_origin_station, year,
            carrier_tracking_ref.zfill(8)
        )
        legible_licence_plate_code = "({}) {} {} {} {} {} {}".format(
            licence_plate_code[0:1], licence_plate_code[1:5],
            licence_plate_code[5:7], licence_plate_code[7:11],
            licence_plate_code[11:15], licence_plate_code[15:19],
            licence_plate_code[19:])
        return licence_plate_code, legible_licence_plate_code

    @api.multi
    def _generate_dhl_epl_label(self, package_ids=None):
        self.ensure_one()
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        ir_sequence_env = self.env['ir.sequence']
        dhl_configuration = self.carrier_id.carrier_file_id
        template_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'template')
        template_file_path = os.path.join(template_path, 'label_template.mako')
        template_file = file(template_file_path, 'rb')
        label_template = mako_template_env.from_string(template_file.read())
        carrier_tracking_ref = self.carrier_tracking_ref
        if not carrier_tracking_ref:
            carrier_tracking_ref = ir_sequence_env.next_by_id(
                dhl_configuration.dhl_package_sequence.id)
            self.write({'carrier_tracking_ref': carrier_tracking_ref})

        routing_code, legible_routing_code = self._dhl_routing_code()
        licence_plate_code, legible_licence_plate_code = \
            self._dhl_licence_plate_code(dhl_configuration,
                                         carrier_tracking_ref)

        inboundsort = ""
        # TODO: Inboundsort establecido a Aereo o Maritimo en funcion
        # de si es a Canarias o Azores y solo para estos destinos

        dhl_facility = self._dhl_facility_code()
        facility_code = "{} {}".format(dhl_facility.facility_code,
                                       dhl_facility.facility_name)
        pickup_datetime = datetime.strptime(self.date_done,
                                            DEFAULT_SERVER_DATETIME_FORMAT)
        rendered_label = label_template.render({
            'picking': self,
            'destination_country': 'ES',
            'pickup_date': pickup_datetime.strftime('%Y-%m-%d'),
            'shipment_ref': carrier_tracking_ref,
            'routing_code': routing_code,
            'legible_routing_code': legible_routing_code,
            'licence_plate_code': licence_plate_code,
            'legible_licence_plate_code': legible_licence_plate_code,
            'inboundsort': inboundsort,
            'facility_code': facility_code
        })

        label = {
            'file': rendered_label,
            'file_type': 'epl',
            'name': carrier_tracking_ref + '.epl',
        }

        return [label]

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for DHL """
        self.ensure_one()
        if self.carrier_id.type == 'dhl_carrier_file':
            return self._generate_dhl_epl_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
