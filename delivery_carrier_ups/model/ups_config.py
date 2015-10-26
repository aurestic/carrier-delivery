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
from openerp import models, fields, api

UPS_LABEL_FORMAT = [
    ('EPL', 'EPL'),
    ('ZPL', 'ZPL'),
    ('GIF', 'GIF'),
    ('STARPL', 'STARPL'),
    ('SPL', 'SPL')
]


class UPSConfig(models.Model):
    _name = 'ups.config'

    @api.model
    def _ups_weight_uom(self):
        return [
            ('KGS', 'KGS'),
            ('LBS', 'LBS')
        ]

    @api.model
    def _ups_dimension_uom(self):
        return [
            ('CM', 'CM'),
            ('IN', 'IN')
        ]

    @api.model
    def _ups_label_file_format(self):
        return UPS_LABEL_FORMAT

    name = fields.Char('UPS Config Name', required=True)
    is_test = fields.Boolean('Is a test?')
    username = fields.Char('UPS Username', required=True)
    password = fields.Char('UPS Password', required=True)
    access_license = fields.Char('UPS Access license', required=True)
    shipper_number = fields.Char('UPS Shipper number', required=True)

    weight_uom = fields.Selection('_ups_weight_uom', required=True,
                                  default="KGS")
    dimension_uom = fields.Selection('_ups_dimension_uom', required=True,
                                     default='CM')

    label_file_format = fields.Selection('_ups_label_file_format',
                                         required=True, default='EPL')
