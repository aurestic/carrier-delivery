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
from fedex.base_service import FedexError, SchemaValidationError
from fedex.config import FedexConfig
from fedex.services.ship_service import FedexProcessShipmentRequest
from openerp import models, fields, api, exceptions, _
from openerp.addons.delivery_carrier_label_fedex.models.fedex_config import \
    FEDEX_SERVICE_TYPES


class ShippingLabel(models.Model):
    _inherit = 'shipping.label'

    @api.model
    def _get_file_type_selection(self):
        res = super(ShippingLabel, self)._get_file_type_selection()
        fedex_file_types = [
            ('pdf', 'pdf'),
            ('zplii', 'zplii'),
            ('epl2', 'epl2'),
            ('dpl', 'dpl'),
            ('png', 'png')
        ]
        res += fedex_file_types
        res = list(set(res))
        return res


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    fedex_service_type = fields.Selection(
        FEDEX_SERVICE_TYPES, string="Fedex Service")

    @api.onchange('carrier_id')
    def carrier_id_change(self):
        result = super(StockPicking, self).carrier_id_change()
        if not self.carrier_id and not self.carrier_id.type != 'fedex' or (
                not self.carrier_id.fedex_config_id):
            return result
        if self.carrier_id.fedex_config_id.default_service:
            self.fedex_service_type =\
                self.carrier_id.fedex_config_id.default_service
        return result

    @api.multi
    def _generate_fedex_label(self, package_ids=None):
        self.ensure_one()
        if not self.carrier_id.fedex_config_id:
            raise exceptions.Warning(_('No Fedex config defined in carrier'))
        if not self.fedex_service_type:
            raise exceptions.Warning(
                _('A Fedex Service type is required to generate a shipment'
                  ' request and label'))
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        warehouse_partner = self.picking_type_id.warehouse_id.partner_id

        odoo_fedex_config = self.carrier_id.fedex_config_id
        fedex_config = FedexConfig(
            key=odoo_fedex_config.key,
            password=odoo_fedex_config.password,
            account_number=odoo_fedex_config.account_number,
            meter_number=odoo_fedex_config.meter_number,
            freight_account_number=(
                odoo_fedex_config.freight_account_number),
            use_test_server=odoo_fedex_config.is_test)
        shipment = FedexProcessShipmentRequest(fedex_config)
        requested_shipment = shipment.RequestedShipment
        shipment.RequestedShipment.DropoffType = 'REGULAR_PICKUP'
        shipment.RequestedShipment.ServiceType = 'PRIORITY_OVERNIGHT'
        shipment.RequestedShipment.PackagingType = 'YOUR_PACKAGING'

        # Shipper contact info.
        shipper_contact = shipment.RequestedShipment.Shipper.Contact
        shipper_contact.PersonName = warehouse_partner.name
        shipper_contact.CompanyName = warehouse_partner.name
        shipper_contact.PhoneNumber = warehouse_partner.phone

        # Shipper address.
        shipper_address = shipment.RequestedShipment.Shipper.Address
        shipper_street_lines = [warehouse_partner.street]
        if warehouse_partner.street2:
            shipper_street_lines.append(warehouse_partner.street2)
        shipper_address.StreetLines = shipper_street_lines
        shipper_address.City = warehouse_partner.city
        shipper_address.StateOrProvinceCode = warehouse_partner.country_id.code
        shipper_address.PostalCode = warehouse_partner.zip
        shipper_address.CountryCode = warehouse_partner.country_id.code
        shipper_address.Residential = True

        # Recipient contact info.
        recipient_contact = shipment.RequestedShipment.Recipient.Contact
        recipient_contact.PersonName = self.partner_id.name
        recipient_contact.CompanyName = self.partner_id.parent_id.name or ''
        recipient_contact.PhoneNumber = self.partner_id.phone

        # Recipient address
        recipient_address = shipment.RequestedShipment.Recipient.Address
        recipient_street_lines = [self.partner_id.street]
        if self.partner_id.street2:
            recipient_street_lines.append(self.partner_id.street2)
        recipient_address.StreetLines = recipient_street_lines
        recipient_address.City = self.partner_id.city
        recipient_address.StateOrProvinceCode = self.partner_id.country_id.code
        recipient_address.PostalCode = self.partner_id.zip
        recipient_address.CountryCode = self.partner_id.country_id.code
        recipient_address.Residential = True

        shipment.RequestedShipment.EdtRequestType = 'NONE'

        shipping_charges_payment =\
            shipment.RequestedShipment.ShippingChargesPayment
        payor_responsible_party =\
            shipping_charges_payment.Payor.ResponsibleParty
        payor_responsible_party.AccountNumber = fedex_config.account_number
        payor_responsible_party.Address.CountryCode =\
            warehouse_partner.country_id.code

        shipping_charges_payment.PaymentType = 'SENDER'

        # Label Specification
        requested_shipment.LabelSpecification.LabelFormatType = 'COMMON2D'
        requested_shipment.LabelSpecification.ImageType =\
            odoo_fedex_config.label_type
        requested_shipment.LabelSpecification.LabelStockType =\
            odoo_fedex_config.label_template
        requested_shipment.LabelSpecification.LabelPrintingOrientation =\
            'BOTTOM_EDGE_OF_TEXT_FIRST'

        number_of_packages = self.number_of_packages or 1
        # if warehouse_partner.country_id.code != \
        #         self.partner_id.country_id.code:
        #     # Add customs Value
        #     customs_detail = requested_shipment.CustomsClearanceDetail
        #     duties_payment = customs_detail.DutiesPayment
        #     # duties_payment.PaymentType = 'RECIPIENT'
        #     customs_detail.CustomsValue.Currency = 'EUR'
        #     customs_detail.CustomsValue.Amount = 100
        #     # customs_detail.Commodities.Descriptions = 'GOODS'

        picking_weight = self.weight or 1.0
        for package in range(number_of_packages):
            package_weight = shipment.create_wsdl_object_of_type('Weight')
            package_weight.Value = picking_weight / float(number_of_packages)
            package_weight.Units = odoo_fedex_config.weight_uom

            package = shipment.create_wsdl_object_of_type(
                'RequestedPackageLineItem')
            package.PhysicalPackaging = 'BOX'
            package.Weight = package_weight
            shipment.add_package(package)

        labels = []
        label_extension = odoo_fedex_config.label_type.lower()
        try:
            shipment.send_request()
            if shipment.response.HighestSeverity == 'ERROR':
                error_response = shipment.response.Notifications[0]
                raise exceptions.Warning(_('Fedex Error: {} {}').format(
                    error_response.Code, error_response.Message))
            completed_shipment = shipment.response.CompletedShipmentDetail
            tracking_number = completed_shipment.CompletedPackageDetails[0].\
                TrackingIds[0].TrackingNumber
            for package_response in completed_shipment.CompletedPackageDetails:
                label = {
                    'file': str(package_response.Label.Parts[0].Image).decode(
                        'base64'),
                    'file_type': label_extension,
                    'name': "{}.{}".format(
                        package_response.TrackingIds[0].TrackingNumber,
                        label_extension)
                }
                labels.append(label)
            self.write({'carrier_tracking_ref': tracking_number})
        except FedexError, e:
            raise exceptions.Warning(_('Fedex Error {}: {}').format(
                e.error_code, e.value))
        except SchemaValidationError, e:
            raise exceptions.Warning(_('Fedex Schema Error {}: {}').format(
                e.error_code, e.value))

        return labels

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for Fedex """
        self.ensure_one()
        if self.carrier_id.type == 'fedex':
            return self._generate_fedex_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
