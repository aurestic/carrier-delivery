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
from openerp.osv import orm, fields
from openerp.tools.translate import _
import base64
import tempfile

class tnt_manifest_wizard(orm.TransientModel):
    _name = 'tnt.manifest.wizard'

    _columns = {
        'from_date': fields.datetime('From Date', required=True),
        'file': fields.binary('Manifest', readonly=True),
        'filename': fields.char('File Name', readonly=True),
        'state': fields.selection((
            ('init', 'Init'),
            ('file', 'File')
        ), 'State', readonly=True)
    }

    _defaults = {
        'state': 'init'
    }

    def get_manifest_file(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        wiz = self.browse(cr, uid, ids[0], context=context)

        f = tempfile.NamedTemporaryFile(delete=False)
        f.close()
        f.name


        try:
            base64.b64decode(result)
        except:
            raise orm.except_orm(
                "Error",
                result
            )

        self.write(cr, uid, ids[0], {
            'file': result,
            'filename': 'ManifiestoTNT.pdf',
            'state': 'file'
        }, context=context)

        view_ids = self.pool['ir.ui.view'].search(
            cr, uid, [('model', '=', 'tnt.manifest.wizard')])

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'tnt.manifest.wizard',
            'name': _('TNT Manifest'),
            'res_id': ids[0],
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_ids[0],
            'target': 'new',
            'nodestroy': True,
            'context': context
        }
