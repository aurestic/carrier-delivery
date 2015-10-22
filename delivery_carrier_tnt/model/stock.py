# -*- encoding: utf-8 -*-
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
import urllib
from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, tools
from openerp.tools.translate import _
import httplib
import base64
import tempfile
from lxml import etree
import tnt
import os
import sys
import subprocess
import logging
_logger = logging.getLogger(__name__)

def transform(name, path, xmlname, xslname):
    dom = etree.parse(path+xmlname)
    xslt = etree.parse(path+xslname)
    transform = etree.XSLT(xslt)
    newdom = transform(dom, css_dir="'file://"+path+"'")
    html_label = etree.tostring(newdom, pretty_print=True)
    return html_label

def getTNTDC(code):

    factors = [8,6,4,2,3,5,9,7]
    dc = 0
    step1 = 0
    for i,c in enumerate(code):
        step1 = step1+int(c)*factors[i]

    step2 = int(step1/11)*11
    step3 = step1-step2
    if step3==0:
        dc = "5"
    elif step3==1:
        dc = "0"
    else:
        dc = str(11-step3)
    return dc

def get_collection_date(time):
    now = datetime.now()
    collection = now.replace(hour=int(time), minute = int((time - int(time))*60), second=0, microsecond=0)
    if collection <= now:
        collection = collection+timedelta(days=1)
    return collection.strftime("%Y-%m-%dT%H:%M:%S")


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.multi
    def _tnt_transm_envio_request(self):
        self.ensure_one()

        consigment_code = self.env['ir.sequence'].get('tnt.consignment.sequence')
        if consigment_code>self.carrier_id.tnt_config_id.max_range_code and consigment_code<self.carrier_id.tnt_config_id.min_range_code:
            raise exceptions.Warning(_('Exceeded TNT Range codes'))
        
        requestlabel = tnt.labelRequest()
        requestlabel.consignment.append(tnt.labelConsignmentsType())
        requestlabel.consignment[0].key = 'con1'
        requestlabel.consignment[0].consignmentIdentity = tnt.consignmentIdentityType()

        requestlabel.consignment[0].consignmentIdentity.consignmentNumber =  consigment_code + getTNTDC(consigment_code)
        requestlabel.consignment[0].consignmentIdentity.customerReference = self.name
        requestlabel.consignment[0].collectionDateTime = get_collection_date(self.carrier_id.tnt_config_id.time)


        requestlabel.consignment[0].sender = tnt.nameAndAddressRequestType()
        warehouse_address = self.picking_type_id.warehouse_id.partner_id
        requestlabel.consignment[0].sender.name = warehouse_address.name
        requestlabel.consignment[0].sender.addressLine1 = warehouse_address.street
        if warehouse_address.street2:
            requestlabel.consignment[0].sender.addressLine2 = warehouse_address.street2
        requestlabel.consignment[0].sender.town = warehouse_address.city
        requestlabel.consignment[0].sender.exactMatch = 'N'
        requestlabel.consignment[0].sender.province = warehouse_address.state_id.name or ''
        requestlabel.consignment[0].sender.postcode = warehouse_address.zip.zfill(5)
        requestlabel.consignment[0].sender.country = warehouse_address.country_id.code or ''


        requestlabel.consignment[0].delivery = tnt.nameAndAddressRequestType()
        requestlabel.consignment[0].delivery.name = self.partner_id.name or ''
        requestlabel.consignment[0].delivery.addressLine1 = self.partner_id.street
        if self.partner_id.street2:
            requestlabel.consignment[0].delivery.addressLine2 = self.partner_id.street2
        requestlabel.consignment[0].delivery.town = self.partner_id.city
        requestlabel.consignment[0].sender.exactMatch = 'N'
        requestlabel.consignment[0].delivery.province = self.partner_id.state_id.name or ''
        requestlabel.consignment[0].delivery.postcode = self.partner_id.zip.zfill(5)
        requestlabel.consignment[0].delivery.country = self.partner_id.country_id.code or ''

        requestlabel.consignment[0].contact = tnt.contactType()
        requestlabel.consignment[0].contact.name = (self.partner_id and self.partner_id.parent_id and self.partner_id.parent_id.name) or (self.partner_id and self.partner_id.name) or ''
        requestlabel.consignment[0].contact.telephoneNumber = self.partner_id.phone or ''
        requestlabel.consignment[0].contact.emailAddress = self.partner_id.email or ''

        requestlabel.consignment[0].product = tnt.productType()
        requestlabel.consignment[0].product.lineOfBusiness = '1'
        requestlabel.consignment[0].product.groupId = '0'
        requestlabel.consignment[0].product.subGroupId = '0'
        requestlabel.consignment[0].product.id = 'EX'
        requestlabel.consignment[0].product.type = 'N'

        requestlabel.consignment[0].account = tnt.accountType()
        requestlabel.consignment[0].account.accountNumber = self.carrier_id.tnt_config_id.account_number
        requestlabel.consignment[0].account.accountCountry = self.carrier_id.tnt_config_id.account_country

        requestlabel.consignment[0].totalNumberOfPieces = self.number_of_packages or 1

        requestlabel.consignment[0].pieceLine.append(tnt.pieceLineType())
        requestlabel.consignment[0].pieceLine[0].identifier = 1
        desc = ','.join([move.name[0:5] for move in self.move_lines])
        requestlabel.consignment[0].pieceLine[0].goodsDescription = desc[0:30]
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements = tnt.measurementsType()
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.length = self.carrier_id.tnt_config_id.length_package
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.width = self.carrier_id.tnt_config_id.width_package
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.height = self.carrier_id.tnt_config_id.height_package
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.weight = self.weight or 1

        requestlabel.consignment[0].pieceLine[0].pieces.append(tnt.pieceType())
        requestlabel.consignment[0].pieceLine[0].pieces[0].sequenceNumbers = str(range(1,(self.number_of_packages or 1)+1)).strip('[]').replace(' ','')
        requestlabel.consignment[0].pieceLine[0].pieces[0].pieceReference = 'COMPONENT'
        message = requestlabel.toxml("utf-8")


        host = "express.tnt.com"
        url = "/expresslabel/documentation/getlabel"
        username = self.carrier_id.tnt_config_id.username
        password = self.carrier_id.tnt_config_id.password


        auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        webservice = httplib.HTTPS(host)
        webservice.putrequest("POST", url)
        webservice.putheader("Host", host)
        webservice.putheader("User-Agent", "Python http auth")
        webservice.putheader("Content-type", "text/xml")
        webservice.putheader("Content-length", "%d" % len(message))
        webservice.putheader("Authorization", "Basic %s" % auth)
        webservice.endheaders()
        webservice.send(message)
        statuscode, statusmessage, header = webservice.getreply()
        res = webservice.getfile().read()

        return res

    @api.multi
    def _generate_tnt_label(self, package_ids=None):
        self.ensure_one()
        if not self.carrier_id.tnt_config_id:
            raise exceptions.Warning(_('No TNT Config defined in carrier'))
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        response = self._tnt_transm_envio_request()
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        label_pdf=transform(self.name, current_path, '/label.xml','/HTMLRoutingLabelRenderer_Local.xsl')

        try:
            defpath = os.environ.get('PATH', os.defpath).split(os.pathsep)
            if hasattr(sys, 'frozen'):
                defpath.append(os.getcwd())
                if tools.config['root_path']:
                    defpath.append(os.path.dirname(tools.config['root_path']))
            webkit_path = tools.which('wkhtmltopdf', path=os.pathsep.join(defpath))
        except IOError:
            webkit_path = None
        command = ""

        fd, out_filename = tempfile.mkstemp(suffix=".pdf",
                                            prefix="tnt.labels.")
        file_to_del = [out_filename]
        if webkit_path:
            command = [webkit_path]
            command.append('--quiet')
            command.extend(['--encoding', 'utf-8'])

            count = 0
            with tempfile.NamedTemporaryFile(suffix="%d.html" %count,
                                             delete=False) as html_file:
                html_file.write(label_pdf)
            file_to_del.append(html_file.name)
            command.append(html_file.name)
        command.append(out_filename)
        status = False
        try:
            status = subprocess.call(command)
            with open(out_filename, 'rb') as pdf_file:
                pdf = pdf_file.read()
            os.close(fd)
        finally:
            
            for f_to_del in file_to_del:
                try:
                    os.unlink(f_to_del)
                except (OSError, IOError), exc:
                    _logger.error('cannot remove file %s: %s', f_to_del, exc)
        label = {
            'file': pdf,
            'file_type': 'pdf',
            'name': self.name + '.pdf',
        }
        return [label]

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for TNT """
        self.ensure_one()
        if self.carrier_id.type == 'tnt':
            return self._generate_tnt_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
