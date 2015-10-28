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


class DHLLine(BaseLine):
    fields = (
        ('cocodcli', 6),
        ('coanod', 1),
        ('copade', 2),
        ('coexpe_ddd', 8),
        ('cocorr', 1),
        ('cofill01', 1),
        ('cotser', 1),
        ('consig', 40),
        ('codirdes', 40),
        ('copobdes', 20),
        ('cocpdes', 9),
        ('cptlfdes', 9),
        ('cofill02', 1),
        ('corefcli', 35),
        ('cofill03', 2),
        ('cobultos', 3),
        ('cokilos', 5),
        ('cokilvol', 5),
        ('coreembo', 11),
        ('comonrem', 3),
        ('copreemb', 1),
        ('covaseg', 9),
        ('comonval', 3),
        ('copvaseg', 1),
        ('coalbfir', 1),
        ('cifill02', 1),
        ('coobser1', 40),
        ('coobser2', 40),
        ('coclvadu', 1),
        ('cofecsal', 8),
        ('conomrem', 40),
        ('codirrem', 40),
        ('copobrem', 20),
        ('cocprem', 5),
        ('cotlfrem', 9),
        ('cofill03', 11),
        ('coclpint', 3),
        ('coprodu', 3),
        ('conomcto', 25),
        ('codesbie', 70),
        ('coimpadu', 15),
        ('comonadu', 3),
        ('cotlfint', 15),
        ('cocliaer', 9),
        ('coawb', 10),
        ('copaor', 2),
        ('comailrem', 50),
        ('coctorem', 25),
        ('comaildes', 50),
        ('covolum', 4),
        ('coprofeat', 90)
    )

    zerofill_fields = ['cocodcli', 'coexpe_ddd', 'cobultos', 'cokilos',
                       'coprodu']

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


class DHLFileGenerator(CarrierFileGenerator):

    @classmethod
    def carrier_for(cls, carrier_name):
        return carrier_name == 'dhl_domestic_economy'

    def _get_rows(self, picking, configuration):
        dhl_country_service_env = picking.env['dhl.country.service']
        ir_sequence_env = picking.env['ir.sequence']
        country_services = dhl_country_service_env.search([
            ('country_id', '=', picking.partner_id.country_id.id)
        ])

        if not country_services:
            return []
        coprodu = country_services.service_number

        time_now = datetime.now()
        line = DHLLine()
        partner_id = picking.partner_id
        wh_partner_id = picking.picking_type_id.warehouse_id.partner_id
        line.cocodcli = configuration.dhl_account_code
        line.coanod = str(time_now.year)[-1]
        line.corefcli = picking.name
        line.copade = picking.partner_id.country_id.code
        line.coexpe_ddd = ir_sequence_env.next_by_id(
            configuration.dhl_package_sequence.id)
        line.cocorr = "0"
        line.consig = partner_id.name
        ship_address = partner_id.street
        if partner_id.street2:
            ship_address = u"{}, {}".format(ship_address, partner_id.street2)
        line.codirdes = ship_address
        line.copobdes = partner_id.city
        line.cocpdes = partner_id.zip
        line.cpltfdes = partner_id.phone and partner_id.phone.replace(
            '-', '').replace(' ', '').replace('.', '') or ''
        line.cobultos = picking.number_of_packages or "1"
        line.cokilos = int(picking.weight) or "1"
        line.cofecsal = time_now.strftime('%d%m%Y')

        line.conomrem = wh_partner_id.name or ''
        line.codirrem = wh_partner_id.street or ''
        line.copobrem = wh_partner_id.city or ''
        line.cocprem = wh_partner_id.zip or ''
        line.cotlfrem = wh_partner_id.phone and wh_partner_id.phone.replace(
            '-', '').replace(' ', '').replace('.', '') or ''

        # Pagador gastos expedicion
        # CPT: Remitente
        # EXW: Consignatario
        line.coclpint = "CPT"

        line.coprodu = coprodu
        return [line.get_fields()]

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

    def _dhl_filename(self, configuration, extension='EXP'):
        date_now = datetime.now()
        formatted_date = date_now.strftime('%y%m%d_%H%M%S')
        return "T{}_{}_{}.{}".format(
            configuration.dhl_origin_station,
            configuration.dhl_account_code.zfill(10),
            formatted_date, extension
        )

    def _get_filename_grouped(self, configuration, extension='EXP'):
        return self._dhl_filename(configuration, extension)

    def _get_filename_single(self, picking, configuration, extension='EXP'):
        return self._dhl_filename(configuration, extension)

    def generate_files(self, pickings, configuration):
        res = super(DHLFileGenerator, self).generate_files(
            pickings, configuration)
        return res
