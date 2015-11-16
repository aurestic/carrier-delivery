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
import os
import csv
from openerp import models, api, exceptions


class GefcoDestinationConfigWizard(models.TransientModel):
    _name = 'gefco.destination.config.wizard'

    @api.multi
    def import_destination_data(self):
        gefco_destination_env = self.env['gefco.destination']
        country_env = self.env['res.country']
        data_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'data')
        gefco_destination_file = os.path.join(data_path,
                                              'gefco_destination_codes.csv')
        with open(gefco_destination_file, 'rb') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                country = country_env.search([
                    ('code', '=', row['country_id'])
                ])
                if not country:
                    raise exceptions.Warning("Country {} not found".format(
                        row['country_id']))
                zip_code = row['zip_code'].zfill(5)
                destination = gefco_destination_env.search([
                    ('country_id', '=', country.id),
                    ('zip_code', '=', zip_code)
                ])
                if not destination:
                    gefco_destination_env.create({
                        'country_id': country.id,
                        'zip_code': zip_code,
                        'directional_code': row['directional_code'],
                        'destination_code': row['destination_code']
                    })
        return True
