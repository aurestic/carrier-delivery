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


class DHLConfig(models.Model):
    _name = 'dhl.config'

    @api.model
    def _get_dhl_label_template(self):
        return [
            ('ECOM26_84_001', 'ECOM26_84_001'),
            ('ECOM26_A6_001', 'ECOM26_A6_001'),
            ('ECOM26_84CI_001', 'ECOM26_84CI_001'),
            ('ECOM26_A4_001', 'ECOM26_A4_001')
        ]

    @api.model
    def _get_dhl_label_type(self):
        return [
            ('PDF', 'PDF'),
            ('ZPL', 'ZPL'),
            ('EPL', 'EPL'),
            ('LPL2', 'LPL2')
        ]

    name = fields.Char("Configuration Description", required=True)
    is_test = fields.Boolean('Is a test?')
    username = fields.Char("Username", required=True)
    password = fields.Char("Password", required=True)
    account_number = fields.Char("Account number", required=True)
    label_template = fields.Selection('_get_dhl_label_template',
                                      string="Label template",
                                      required=True, default="ECOM26_84_001")
    label_type = fields.Selection('_get_dhl_label_type', string="Label type",
                                  required=True, default='PDF')
