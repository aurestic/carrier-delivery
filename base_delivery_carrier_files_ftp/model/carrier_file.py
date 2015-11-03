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
import tempfile
from ftplib import FTP
from openerp import models, api, fields, exceptions, _


class CarrierFile(models.Model):
    _inherit = 'delivery.carrier.file'

    @api.model
    def get_write_mode_selection(self):
        res = super(CarrierFile, self).get_write_mode_selection()
        res.append(('ftp', 'FTP'))
        return res

    write_mode = fields.Selection(get_write_mode_selection, 'Write on',
                                  required=True)
    ftp_host = fields.Char('FTP Host')
    ftp_user = fields.Char('FTP User')
    ftp_password = fields.Char('FTP Password')

    @api.multi
    def _write_file(self, filename, file_content):
        if self.write_mode == 'ftp':
            ftp_user = self.ftp_user or 'anonymous'
            ftp_password = self.ftp_password or 'anonymous@'
            try:
                ftp = FTP(self.ftp_host, ftp_user, ftp_password)
            except Exception as e:
                raise exceptions.Warning(_(
                    'Failed to connect/login to FTP: {}').format(e))
            ftp_command = "STOR {}".format(filename)
            with tempfile.NamedTemporaryFile() as temp:
                temp.write(file_content)
                temp.flush()
                with open(temp.name) as file_handle:
                    try:
                        ftp.storbinary(ftp_command, file_handle)
                    except Exception as e:
                        raise exceptions.Warning(_(
                            'Problem uploading file to FTP: {}').format(e))
        else:
            return super(CarrierFile, self)._write_file(filename, file_content)
