##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 FactorLibre (http://www.factorlibre.com)
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


class TntConfig(models.Model):
    _name = 'tnt.config'

    name = fields.Char('Name', required=True)
    is_test = fields.Boolean('Is a test?', default=True)
    username = fields.Char('Username', required=True)
    password = fields.Char('Password', required=True)
    time = fields.Float("Collection Time", required=True)
    min_range_code = fields.Char('Min Code', size=8, required=True)
    max_range_code = fields.Char('Max Code', size=8, required=True)
    account_number = fields.Char('Account number', required=True)
    trading_partner = fields.Char('Trading partner', required=True)
    account_country = fields.Char('Account country', size=2, required=True)
    length_package = fields.Float('Package length', required=True)
    width_package = fields.Float('Package width', required=True)
    height_package = fields.Float('Package height', required=True)
