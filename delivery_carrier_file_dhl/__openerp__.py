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
{
    'name': 'Delivery Carrier File: DHL (Spain, Portugal and Andorra)',
    'version': '0.1',
    'author': "FactorLibre, Odoo Community Association (OCA)",
    'category': 'Generic Modules/Warehouse',
    'depends': [
        'base_delivery_carrier_files',
        'base_delivery_carrier_label',
        'document'
    ],
    'website': 'http://factorlibre.com',
    'data': [
        'security/ir.model.access.csv',
        'data/directory_data.xml',
        'data/dhl.country.service.csv',
        'data/dhl.zipcode.facility.csv',
        'view/carrier_file_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
