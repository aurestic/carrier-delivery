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
from ClassicUPS import UPSConnection
from ClassicUPS.ups import UPSError
from openerp import models, fields, api, exceptions, _
from .ups_config import UPS_LABEL_FORMAT


class ShippingLabel(models.Model):
    _inherit = 'shipping.label'

    @api.model
    def _get_file_type_selection(self):
        """ To inherit to add file type """
        res = super(ShippingLabel, self)._get_file_type_selection()
        res += UPS_LABEL_FORMAT
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def _get_ups_service_type(self):
        return [
            ('standard', 'Standard'),
            ('1dayair', 'Next Day Air'),
            ('2dayair', '2nd Day Air'),
            ('ground', 'Ground'),
            ('worldwide_expedited', 'Expedited'),
            ('3_day_select', '3 Day Select'),
            ('next_day_air_saver', 'Next Day Air Saver'),
            ('next_day_air_early_am', 'Next Day Air Early AM'),
            ('express_plus', 'Express Plus'),
            ('2nd_day_air_am', '2nd Day Air A.M.'),
            ('ups_saver', 'UPS Saver')
        ]

    ups_service_type = fields.Selection('_get_ups_service_type',
                                        string='Ups Service',
                                        default='standard')
    ups_shipment_description = fields.Char(string='UPS Description', size=49)
    length = fields.Float(string='Length', default=30)
    width = fields.Float(string='Width', default=30)
    height = fields.Float(string='height', default=30)

    @api.multi
    def _generate_ups_contry_code(self, partner):
        if partner.country_id.code == 'ES' and partner.zip.startswith('35'):  # If Canary Islands
            country_code = 'IC'
        else:
            country_code = partner.country_id.code
        return country_code

    @api.multi
    def _generate_ups_state_code(self, partner):
        if partner.country_id.code in ['US', 'CA']:
            state_code = partner.state_id.code
        else:
            state_code = ''
        return state_code

    @api.multi
    def _generate_ups_label(self, package_ids=None):
        self.ensure_one()
        if not self.carrier_id.ups_config_id:
            raise exceptions.Warning(_('No UPS config defined in carrier'))
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        warehouse_partner = self.picking_type_id.warehouse_id.partner_id

        ups_config = self.carrier_id.ups_config_id
        ups_client = UPSConnection(
            ups_config.access_license, ups_config.username,
            ups_config.password, ups_config.shipper_number,
            debug=ups_config.is_test)

        warehouse_street = warehouse_partner.street
        if warehouse_partner.street2:
            warehouse_street = u"{}, {}".format(warehouse_street,
                                                warehouse_partner.street2)
        from_addr = {
            'name': warehouse_partner.name,
            'address1': warehouse_partner.street,
            'address2': warehouse_partner.street2 or '',
            'city': warehouse_partner.city,
            'country': self._generate_ups_contry_code(warehouse_partner),
            'state': self._generate_ups_state_code(warehouse_partner),
            'postal_code': warehouse_partner.zip,
            'phone': warehouse_partner.phone or '',
            'email': warehouse_partner.email or ''
        }

        to_addr = {
            'name': self.partner_id.name,
            'address1': self.partner_id.street,
            'address2': self.partner_id.street2 or '',
            'city': self.partner_id.city,
            'country': self._generate_ups_contry_code(self.partner_id),
            'state': self._generate_ups_state_code(self.partner_id),
            'postal_code': self.partner_id.zip,
            'phone': self.partner_id.mobile or self.partner_id.phone or '',
            'email': self.partner_id.email or ''
        }

        number_of_packages = self.number_of_packages or 1
        weight = self.weight or 1
        packages = []
        for p in range(number_of_packages):
            packages.append({
                'packaging_type': '02',
                'dimensions': {
                    'length': self.length,
                    'width': self.width,
                    'height': self.height
                },
                'weight': weight / float(number_of_packages)
            })

        try:
            shipment = ups_client.create_shipment(
                from_addr, to_addr, packages, self.ups_service_type,
                file_format=ups_config.label_file_format,
                description=self.ups_shipment_description,
                dimensions_unit=ups_config.dimension_uom,
                weight_unit=ups_config.weight_uom)
        except UPSError, e:
            raise exceptions.Warning(u"UPS Error: {}".format(e.message))

        labels = []

        label_no = 1
        for label_content in shipment.get_label():
            label = {
                'file': label_content,
                'file_type': ups_config.label_file_format,
                'name': u"{}_{}.{}".format(shipment.tracking_number,
                                           label_no,
                                           ups_config.label_file_format)
            }
            labels.append(label)

        self.write({'carrier_tracking_ref': shipment.tracking_number})
        return labels

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        self.ensure_one()
        if self.carrier_id.type == 'ups':
            return self._generate_ups_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
