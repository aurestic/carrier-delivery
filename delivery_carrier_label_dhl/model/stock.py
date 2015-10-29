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
from dhl.service import DHLService
from dhl.resources.address import DHLPerson, DHLCompany
from dhl.resources.package import DHLPackage
from dhl.resources.shipment import DHLShipment
from openerp import models, fields, api, exceptions, _


class ShippingLabel(models.Model):
    _inherit = 'shipping.label'

    @api.model
    def _get_file_type_selection(self):
        res = super(ShippingLabel, self)._get_file_type_selection()
        dhl_file_types = [
            ('pdf', 'pdf'),
            ('zpl', 'zpl'),
            ('epl', 'epl'),
            ('lpl2', 'lpl2')
        ]
        res += dhl_file_types
        res = list(set(res))
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def _get_dhl_service_type(self):
        return [
            ('K', 'K - Express 9:00'),
            ('T', 'T - Express 12:00'),
            ('U', 'U - Express Worldwide (Europe)'),
            ('P', 'P - Express Worldwide (Rest Of the world)'),
            ('7', '7 - Express Easy (Europe)'),
            ('8', '8 - Express Easy (Rest of the world)'),
            ('W', 'W - Economy select'),
            ('N', 'N - Domestic Express'),
            ('G', 'G - Domestic Economy select'),
            ('1', '1 - Domestic Express 12:00'),
            ('C', 'C - Medical Express (Europe)'),
            ('Q', 'Q - Medical Express (Rest of the world)')
        ]

    dhl_service_type = fields.Selection(
        '_get_dhl_service_type', string='DHL Service', default='U')

    @api.multi
    def _generate_dhl_label(self, package_ids=None):
        self.ensure_one()
        if not self.carrier_id.dhl_config_id:
            raise exceptions.Warning(_('No DHL config defined in carrier'))
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        warehouse_partner = self.picking_type_id.warehouse_id.partner_id

        dhl_config = self.carrier_id.dhl_config_id
        dhl_service = DHLService(dhl_config.username, dhl_config.password,
                                 dhl_config.account_number,
                                 test_mode=dhl_config.is_test)
        shipper = DHLPerson(warehouse_partner.name,
                            warehouse_partner.street, warehouse_partner.city,
                            warehouse_partner.zip,
                            warehouse_partner.country_id.code,
                            warehouse_partner.phone,
                            warehouse_partner.email)
        if warehouse_partner.street2:
            shipper.street_lines2 = warehouse_partner.street2

        partner_phone = self.partner_id.mobile or self.partner_id.phone or ''
        if not self.partner_id.is_company and self.partner_id.parent_id \
                and self.partner_id.use_parent_address:
            rec_company = self.partner_id.parent_id
            recipient = DHLCompany(rec_company.name, self.partner_id.name,
                                   rec_company.street, rec_company.city,
                                   rec_company.zip,
                                   rec_company.country_id.code,
                                   partner_phone, self.partner_id.email)
            if rec_company.street2:
                recipient.street_lines2 = rec_company.street2
        else:
            recipient = DHLPerson(self.partner_id.name, self.partner_id.street,
                                  self.partner_id.city, self.partner_id.zip,
                                  self.partner_id.country_id.code,
                                  partner_phone, self.partner_id.email)
            if self.partner_id.street2:
                recipient.street_lines2 = self.partner_id.street2

        packages = []
        number_of_packages = self.number_of_packages or 1
        picking_weight = self.weight or 1.0
        for p in range(number_of_packages):
            packages.append(DHLPackage(
                str(picking_weight / number_of_packages),
                "30", "30", "30", description="Electronic Devices"
            ))
        shipment = DHLShipment(shipper, recipient, packages,
                               reference_code=self.name,
                               drop_off_type="REQUEST_COURIER")
        shipment.label_type = dhl_config.label_type
        shipment.label_format = dhl_config.label_template

        dhl_shipment_request = dhl_service.send(shipment)
        if not dhl_shipment_request.success:
            error_messages = map(
                lambda err: "Code {}: {}".format(err[0], err[1]),
                dhl_shipment_request.errors)
            raise exceptions.Warning(_('Error on DHL Shipment request: %s' % (
                '\n'.join(error_messages))))

        tracking_number = dhl_shipment_request.tracking_numbers[0]
        file_extension = dhl_config.label_type.lower()
        label = {
            'file': str(dhl_shipment_request.label_bytes).decode('base64'),
            'file_type': file_extension,
            'name': "{}.{}".format(tracking_number, file_extension)
        }

        self.write({'carrier_tracking_ref': tracking_number})
        return [label]

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for DHL """
        self.ensure_one()
        if self.carrier_id.type == 'dhl':
            return self._generate_dhl_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
