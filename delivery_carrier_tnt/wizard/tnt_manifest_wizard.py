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
from openerp import models, fields, api, exceptions, _
import logging
import tempfile
import base64
from datetime import datetime

_logger = logging.getLogger(__name__)

class tnt_manifest_wizard(models.TransientModel):
    _name = 'tnt.manifest.wizard'
    to_date = fields.Datetime('To Date', required=True)
    file_out = fields.Binary('Manifest', readonly=True)
    filename = fields.Char('File Name', readonly=True)
    notes = fields.Text('Result', readonly=True)
    state = fields.Selection(selection = [('init', 'Init'),('file', 'File'),('end', 'END')], string='State', readonly=True, default='init')

    @api.multi
    def get_manifest_file(self):
        notes = ''
        picking_pool = self.env['stock.picking']
        state = 'file'
        result = False
        is_test = False
        manifest = ''
        values = {}
        for record in self:
            picking_ids = picking_pool.search([('carrier_id.tnt_config_id','!=', False),('lines_manifest','!=', False), ('datetime_label','<',self.to_date), ('notified2carrier', '=',False)])
            if picking_ids:
                for picking in picking_ids:
                    manifest = manifest + picking.lines_manifest + '\n'
                    if (not is_test) and picking.carrier_id.tnt_config_id.is_test:
                        is_test = True

                f = tempfile.NamedTemporaryFile(delete=False)
                f.write(manifest.encode("utf-8"))
                f.close()
                try:
                    with open(f.name, "rb") as fileopen:
                        result = base64.b64encode(fileopen.read())
                except:
                    raise exceptions.Warning("Error",
                                result)

                if not is_test:
                    state = 'end'
                    notes = _("Sended Manifest")
                    picking_ids.write({'notified2carrier':True})
                    try:
                        _logger.info("Trying to send via FTP")
                    except:
                        notes = _("Error sending Manifest")
                else:
                    notes = _("Test Manifest")


            else:
                state = 'end'
                notes = _("Not exist pending pickings to insert on file manifest")

            values = {
                'notes':notes,
                'state': state
            }
            if result:
                values.update({
                'file_out': result,
                'filename': 'ManifiestoTNT'+str(datetime.now())+'.nff'})
        record.write(values)

        view_ids = self.env['ir.ui.view'].search([('model', '=', 'tnt.manifest.wizard')])
        return {
                'name':'TNT Manifest',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'tnt.manifest.wizard',
                'view_id':False,
                'target':'new',
                'type':'ir.actions.act_window',
                'domain':[('id','=',self.id)],
                'context':self.env.context,
                'nodestroy':True,
                'res_id':self.id,
        }
