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


def _to_ascii(text):
    text = unicode(text)
    return unicodedata.normalize('NFKD', text).encode(
        'ascii', 'ignore').upper()

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
        res.append(('zpl', 'ZPL'))
        res = list(set(res))
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def _generate_gefco_zpl_label(self, package_ids=None):
        self.ensure_one()
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        ir_sequence_env = self.env['ir.sequence']
        gefco_destination_env = self.env['gefco.destination']
        gefco_configuration = self.carrier_id.carrier_file_id
        template_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'template')
        template_file_path = os.path.join(template_path,
                                          'gefco_label_template.mako')
        template_file = file(template_file_path, 'rb')
        label_template = mako_template_env.from_string(template_file.read())
        template_file.close()

        carrier_tracking_ref = self.carrier_tracking_ref
        if not carrier_tracking_ref:
            carrier_tracking_ref = ir_sequence_env.next_by_id(
                gefco_configuration.gefco_picking_sequence.id)
            self.write({'carrier_tracking_ref': carrier_tracking_ref})

        gefco_destination = gefco_destination_env.search([
            ('country_id', '=', self.partner_id.country_id.id),
            ('zip_code', '=', self.partner_id.zip)
        ])
        directional_code = ''
        destination_code = ''
        if gefco_destination:
            directional_code = gefco_destination.directional_code
            destination_code = gefco_destination.destination_code

        pickup_datetime = datetime.strptime(self.date_done,
                                            DEFAULT_SERVER_DATETIME_FORMAT)
        number_of_packages = self.number_of_packages or 1
        labels = []
        for i in range(number_of_packages):
            label_barcode = "{}{}".format(self.carrier_tracking_ref,
                                          str(i + 1).zfill(2))
            rendered_label = label_template.render({
                'picking': self,
                'wh_address': self.picking_type_id.warehouse_id.partner_id,
                'barcode_ref': label_barcode,
                'pickup_date': pickup_datetime.strftime('%d/%m/%Y'),
                'package_number': str(i + 1).zfill(3),
                'total_packages': str(number_of_packages).zfill(3),
                'gefco_configuration': gefco_configuration,
                'directional_destination_code': directional_code,
                'destination_code': destination_code,
                'weight': round((self.weight or 1.0) / number_of_packages, 2)
            })

            label = {
                'file': rendered_label,
                'file_type': 'zpl',
                'name': label_barcode + '.zpl',
            }
            labels.append(label)

        return labels

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for DHL """
        self.ensure_one()
        if self.carrier_id.type == 'gefco_carrier_file':
            return self._generate_gefco_zpl_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
