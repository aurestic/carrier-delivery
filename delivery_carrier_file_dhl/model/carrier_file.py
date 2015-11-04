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
from openerp import models, fields, api


class CarrierFile(models.Model):
    _inherit = 'delivery.carrier.file'

    @api.model
    def get_type_selection(self):
        res = super(CarrierFile, self).get_type_selection()
        res.append(('dhl_domestic_economy', 'DHL DOMESTIC ECONOMY SELECT'))
        return res

    type = fields.Selection('get_type_selection', 'Type', required=True)
    dhl_account_code = fields.Char('DHL Account Code')
    dhl_origin_station = fields.Char('DHL Origin Station')
    dhl_package_sequence = fields.Many2one('ir.sequence',
                                           "DHL Package Sequence")
