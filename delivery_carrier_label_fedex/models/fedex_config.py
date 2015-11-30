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
from openerp import models, fields

FEDEX_SERVICE_TYPES = [
    ('EUROPE_FIRST_INTERNATIONAL_PRIORITY',
     'EUROPE_FIRST_INTERNATIONAL_PRIORITY'),
    ('FEDEX_1_DAY_FREIGHT', 'FEDEX_1_DAY_FREIGHT'),
    ('FEDEX_2_DAY', 'FEDEX_2_DAY'),
    ('FEDEX_2_DAY_FREIGHT', 'FEDEX_2_DAY_FREIGHT'),
    ('FEDEX_3_DAY_FREIGHT', 'FEDEX_3_DAY_FREIGHT'),
    ('FEDEX_EXPRESS_SAVER', 'FEDEX_EXPRESS_SAVER'),
    ('STANDARD_OVERNIGHT', 'STANDARD_OVERNIGHT'),
    ('PRIORITY_OVERNIGHT', 'PRIORITY_OVERNIGHT'),
    ('FEDEX_GROUND', 'FEDEX_GROUND'),
    ('GROUND_HOME_DELIVERY', 'GROUND_HOME_DELIVERY'),
    ('FEDEX_FREIGHT_ECONOMY', 'FEDEX_FREIGHT_ECONOMY'),
    ('FEDEX_FREIGHT_PRIORITY', 'FEDEX_FREIGHT_PRIORITY'),
    ('INTERNATIONAL_ECONOMY', 'INTERNATIONAL_ECONOMY'),
    ('INTERNATIONAL_ECONOMY_FREIGHT', 'INTERNATIONAL_ECONOMY_FREIGHT'),
    ('INTERNATIONAL_FIRST', 'INTERNATIONAL_FIRST'),
    ('INTERNATIONAL_PRIORITY', 'INTERNATIONAL_PRIORITY'),
    ('INTERNATIONAL_PRIORITY_FREIGHT', 'INTERNATIONAL_PRIORITY_FREIGHT')
]


class FedexConfig(models.Model):
    _name = 'fedex.config'

    name = fields.Char('Name', required=True)
    is_test = fields.Boolean('Is a test?')
    account_number = fields.Char('Account Number', required=True)
    key = fields.Char('Key', required=True)
    password = fields.Char('Password', required=True)
    meter_number = fields.Char('Meter Number', required=True)
    freight_account_number = fields.Char('Freight Account Number')
    weight_uom = fields.Selection([('KG', 'KG'), ('LB', 'LB')], required=True,
                                  default="KG")
    dimension_uom = fields.Selection([('CM', 'CM'), ('IN', 'IN')],
                                     required=True, default='CM')
    default_service = fields.Selection(FEDEX_SERVICE_TYPES,
                                       string='Default Service',
                                       default='INTERNATIONAL_ECONOMY')
    label_type = fields.Selection([
        ('PDF', 'PDF'),
        ('PNG', 'PNG'),
        ('DPL', 'DPL'),
        ('EPL2', 'EPL'),
        ('ZPLII', 'ZPL')], 'Label Type', required=True, default='ZPLII')
    label_template = fields.Selection([
        ('STOCK_4X6', 'STOCK_4X6'),
        ('STOCK_4X6.75_LEADING_DOC_TAB', 'STOCK_4X6.75_LEADING_DOC_TAB'),
        ('STOCK_4X6.75_TRAILING_DOC_TAB', 'STOCK_4X6.75_TRAILING_DOC_TAB'),
        ('STOCK_4X8', 'STOCK_4X8'),
        ('STOCK_4X9_LEADING_DOC_TAB', 'STOCK_4X9_LEADING_DOC_TAB'),
        ('STOCK_4X9_TRAILING_DOC_TAB', 'STOCK_4X9_TRAILING_DOC_TAB')
    ], 'Label Template', required=True, default='STOCK_4X6')
