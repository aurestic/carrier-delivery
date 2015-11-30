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
