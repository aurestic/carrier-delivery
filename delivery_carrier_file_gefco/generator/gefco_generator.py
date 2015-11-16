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
from datetime import datetime
from openerp.addons.base_delivery_carrier_files.generator import \
    CarrierFileGenerator, BaseLine


class GefcoBaseLine(BaseLine):

    zerofill_fields = []

    def get_fields(self):
        """
        According to the class attribute "fields",
        generate a row with all the value of the line.
        If a width is defined on some fields,
        their content is cut to their maximal length.

        :return: a list of values for each field in the
                 order of the class attribute "fields"
        """
        res = []
        zerofill_fields = self.zerofill_fields or []
        for field in self.fields:
            field_name, width = self._field_definition(field)
            if field_name:
                value = getattr(self, field_name)
                if value in (False, None):
                    value = ''
                elif not isinstance(value, (str, unicode)):
                    value = unicode(value)
                if width:
                    value = value[0:width]
                    if field_name in zerofill_fields:
                        value = value.zfill(width)
                    if width > len(value):
                        need_width = width - len(value)
                        value = u"{}{}".format(value, ' ' * need_width)
            else:
                value = ''
            res.append(value)
        return res


class GefcoHeaderLine(GefcoBaseLine):
    fields = (
        ('header_id', 2),
        ('application', 3),
        ('shipper_id', 35),
        ('account_number', 17),
        ('shipper_name', 35),
        ('shipper_city', 35),
        ('agency_code', 35),
        ('agency_city', 35),
        ('manifest_number', 8),
        ('load_number', 2),
        ('document_date', 8),
        ('shipments_in_load', 3),
        ('number_of_packages', 4),
        ('total_weight', 5),
        ('cash_on_delivery_total', 15),
        ('cash_on_delivery_currency', 3),
        ('filler', 11)
    )

    zerofill_fields = ['manifest_number', 'load_number', 'shipments_in_load',
                       'number_of_packages', 'total_weight',
                       'cash_on_delivery_total']

    required_fields = ['header_id', 'application', 'shipper_id', 'agency_code',
                       'manifest_number', 'document_date']


class GefcoDetailLine(GefcoBaseLine):
    fields = (
        ('detail_id', 3),
        ('picking_reference', 35),
        ('waybill_number', 8),
        ('print_receipt', 1),
        ('shipping_conditions', 1),  # 1=Express, 3=normal, 9=other
        ('recipient_id', 35),
        ('recipient_name', 35),
        ('recipient_address1', 35),
        ('recipient_address2', 35),
        ('recipient_zipcode', 9),
        ('recipient_city', 35),
        ('recipient_country_code', 2),
        ('final_recipient_country_code', 2),
        ('recipient_phone', 25),
        ('recipient_contact_number', 35),
        ('number_of_packages', 4),
        ('number_of_handing_units', 4),
        ('number_of_retornable_equiment', 4),
        ('weight', 5),
        ('incoterms', 3),  # Appendix 2 - DHL flat file
        ('requested_delivery_date', 8),
        ('requested_delivery_hour_start', 4),
        ('requested_delivery_hour_end', 4),
        ('goods_description', 25),
        ('dangerous_goods', 1),
        ('delivery_instructions', 70),
        ('unity_of_charge', 3),
        ('units_to_tax', 9),
        ('cash_on_delivery_amount', 15),
        ('cash_on_delivery_currency', 3),
        ('assurance_amount', 15),
        ('assurance_currency', 3),
        ('trader_invoice_amount', 15),
        ('trader_invoice_currency', 3),
        ('traffic_type', 3),
        ('account_analytic_number', 17),
        ('charge_codeI', 17),
        ('shipper_id', 35),  # Fill if different to the regular shipper
        ('shipper_name', 35),
        ('shipper_address1', 35),
        ('shipper_address2', 35),
        ('shipper_zipcode', 9),
        ('shipper_city', 35),
        ('shipper_country_code', 2),
        ('volume', 6),
        ('length', 6)
    )

    zerofill_fields = ['waybill_number', 'recipient_phone',
                       'number_of_packages',
                       'number_of number_of_handing_units',
                       'number_of_retornable_equiment',
                       'requested_delivery_date',
                       'requested_delivery_hour_start',
                       'requested_delivery_hour_end', 'units_to_tax',
                       'cash_on_delivery_amount', 'assurance_amount',
                       'trader_invoice_amount', 'volume', 'length']

    required_fields = ['detail_id', 'picking_reference', 'waybill_number',
                       'shipping_conditions', 'recipient_name',
                       'recipient_address1', 'recipient_zipcode',
                       'recipient_country_code', 'number_of_packages',
                       'number_of_handing_units']


class GefcoPackageLine(GefcoBaseLine):
    fields = [
        ('package_record_id', 3),
        ('shipper_parcel_number', 35),  # Barcode Number
        ('handling_unit_number', 35),  # Barcode Sticked on the handling unit
        ('filler', 55)
    ]

    required_fields = ['package_record_id', 'shipper_parcel_number']


class GefcoFileGenerator(CarrierFileGenerator):

    @classmethod
    def carrier_for(cls, carrier_name):
        return carrier_name == 'gefco'

    def _get_header_rows(self, pickings, configuration):
        ir_sequence_env = pickings.env['ir.sequence']
        manifest_number = ir_sequence_env.next_by_id(
            configuration.gefco_manifest_sequence.id)
        header_line = GefcoHeaderLine()
        header_line.header_id = "H1"
        header_line.application = "787"
        header_line.shipper_id = configuration.gefco_shipper_id
        header_line.account_number = configuration.gefco_account_number
        header_line.shipper_name = ""
        header_line.shipper_city = ""
        header_line.agency_code = configuration.gefco_agency_code
        header_line.manifest_number = manifest_number
        header_line.load_number = 0
        header_line.document_date = datetime.now().strftime("%Y%m%d")
        header_line.shipments_in_load = len(pickings)
        return [header_line.get_fields()]

    def _get_rows(self, picking, configuration):
        ir_sequence_env = picking.env['ir.sequence']
        picking_sequence = ir_sequence_env.next_by_id(
            configuration.gefco_picking_sequence.id)
        number_of_packages = picking.number_of_packages or 1

        detail_line = GefcoDetailLine()
        detail_line.detail_id = "RDE"
        detail_line.picking_reference = picking.origin
        detail_line.waybill_number = picking_sequence
        detail_line.print_receipt = "1"

        partner_id = picking.partner_id
        wh_partner_id = picking.picking_type_id.warehouse_id.partner_id

        detail_line.recipient_id = partner_id.ref
        detail_line.recipient_name = partner_id.name
        detail_line.recipient_address1 = partner_id.street
        if partner_id.street2:
            detail_line.recipient_address2 = partner_id.street2
        detail_line.recipient_city = partner_id.city
        detail_line.recipient_zipcode = partner_id.zip
        detail_line.recipient_phone = partner_id.phone and \
            partner_id.phone.replace('-', '').replace(' ', '').replace(
                '.', '') or ''
        detail_line.recipient_country_code = partner_id.country_id.code
        detail_line.final_recipient_country_code = partner_id.country_id.code

        detail_line.number_of_packages = str(number_of_packages)
        detail_line.number_of_handing_units = str(number_of_packages)
        detail_line.number_of_retornable_equiment = "0"
        detail_line.weight = int(picking.weight) or "1"
        # Incoterms
        # EXW: Ex Works
        # FAS: Free along side
        # FOB: Free on board
        # CFR: Cost and freight
        # CIF: Cost, insurance and freight
        # CPT: Carriage paid to
        # CIP: Carriage and insurance paid
        # DAF: Delivered at frontier
        # DES: Delivered ex ship
        # DEQ: Delivered ex quai
        # DDU: Delivery duty unpaid
        # DDP: Delivery duty paid
        if partner_id.country_id.code == wh_partner_id.country_id.code:
            incoterm = "P"
        detail_line.incoterms = incoterm

        detail_line.shipper_id = configuration.gefco_shipper_id
        detail_line.shipper_name = wh_partner_id.name or ''
        detail_line.shipper_address1 = wh_partner_id.street or ''
        detail_line.shipper_address2 = wh_partner_id.street2 or ''
        detail_line.shipper_city = wh_partner_id.city or ''
        detail_line.shipper_zipcode = wh_partner_id.zip or ''
        detail_line.shipper_country_code = wh_partner_id.country_id.code or ''
        packages_lines = []
        for package_number in range(number_of_packages):
            package_line = GefcoPackageLine()
            package_code = "{}{}".format(
                picking_sequence, str(package_number + 1).zfill(2))
            package_line.package_record_id = "PCI"
            package_line.shipper_parcel_number = package_code
            package_line.handling_unit_number = package_code
            packages_lines.append(package_line.get_fields())

        picking_lines = [detail_line.get_fields()] + packages_lines

        return picking_lines

    def _write_rows(self, file_handle, rows, configuration):
        """
        Write the rows in the file (file_handle)

        :param StringIO file_handle: file to write in
        :param rows: rows to write in the file
        :param browse_record configuration: configuration of the file to
               generate
        :return: the file_handle as StringIO with the rows written in it
        """
        row_text = ""
        for row in rows:
            row_text += u"{}\n".format("".join(row))
        row_text = unicodedata.normalize('NFKD', row_text).encode(
            'ascii', 'ignore')
        file_handle.write(row_text)
        return file_handle

    def generate_files(self, pickings, configuration):
        res = super(GefcoFileGenerator, self).generate_files(
            pickings, configuration)
        return res

    def _generate_files_single(self, pickings, configuration):
        """
        Base method to generate the pickings files, one file per picking
        It returns a list of tuple with a filename, its content and a
        list of pickings ids in the file

        :param browse_record pickings: list of browsable pickings records
        :param browse_record configuration: configuration of
                                            the file to generate
        :return: list of tuple with files to create like:
                 [('filename1', file, [picking ids]),
                  ('filename2', file2, [picking ids])]
        """
        files = []
        for picking in pickings:
            filename = self._get_filename_single(picking, configuration)
            filename = self.sanitize_filename(filename)
            rows = self._get_header_rows(picking, configuration)
            rows += self._get_rows(picking, configuration)
            file_content = self._get_file(rows, configuration)
            files.append((filename, file_content, [picking.id]))
            # Generate manifest
        return files

    def _generate_files_grouped(self, pickings, configuration):
        """
        Base method to generate the pickings files, one file
        for all pickings
        It returns a list of tuple with a filename, its content
         and a list of pickings ids in the file

        :param browse_record pickings: list of browsable pickings records
        :param browse_record configuration: configuration of
                                            the file to generate
        :return: list of tuple with files to create like:
                 [('filename1', file, [picking ids]),
                  ('filename2', file2, [picking ids])]
        """
        files = []
        rows = self._get_header_rows(pickings, configuration)
        filename = self._get_filename_grouped(configuration)
        filename = self.sanitize_filename(filename)
        for picking in pickings:
            rows += self._get_rows(picking, configuration)
        file_content = self._get_file(rows, configuration)
        files.append((filename, file_content, [p.id for p in pickings]))
        return files
