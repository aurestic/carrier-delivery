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
from openerp import models, fields, api


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    @api.model
    def _get_carrier_type_selection(self):
        """ Add TNT carrier type """
        res = super(DeliveryCarrier, self)._get_carrier_type_selection()
        res.append(('tnt', 'TNT'))
        return res

    TNT_SERVICES = [
        ('100_EX_N_D_15N', 'Express'),
        ('100_EX10_N_D_10N', '10:00 Express'),
        ('100_EX12_N_D_12N', '12:00 Express'),
        ('109_EX_N_D_15', 'Express Plus'),
        ('200_EC_N_G_48N', 'International-Economy Express'),
        ('200_EC12_N_G_412', 'International-12:00 Economy Express'),
        ('200_EX_N_G_15N', 'International-Express'),
        ('200_EX09_N_G_09N', 'International-9:00 Express'),
        ('200_EX10_N_G_10N', 'International-10:00 Express'),
        ('200_EX12_N_G_12N', 'International-12:00 Express'),
    ]

    tnt_config_id = fields.Many2one('tnt.config', string='TNT Config')
    tnt_service_code = fields.Selection(TNT_SERVICES, 'TNT Service')
