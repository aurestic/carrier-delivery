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
from openerp import models, fields, api, exceptions
from openerp.tools.translate import _
import tnt


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
            requestlabel.consignment[0].sender.addressLine2 = warehouse_address.street
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
        requestlabel.consignment[0].name = self.partner_id.name or ''
        requestlabel.consignment[0].telephoneNumber = self.partner_id.phone or ''
        requestlabel.consignment[0].emailAddress = self.partner_id.email or ''

        requestlabel.consignment[0].product = tnt.productType()
        requestlabel.consignment[0].product.lineOfBusiness = '1'
        requestlabel.consignment[0].product.groupId = '0'
        requestlabel.consignment[0].product.subGroupId = '0'
        requestlabel.consignment[0].product.id = 'EX'
        requestlabel.consignment[0].product.type = 'N'

        requestlabel.consignment[0].account = tnt.accountType()
        requestlabel.consignment[0].account.accountNumber = '123456'
        requestlabel.consignment[0].account.accountCountry = 'ES'

        requestlabel.consignment[0].totalNumberOfPieces = self.number_of_packages or 1

        requestlabel.consignment[0].pieceLine.append(tnt.pieceLineType())
        requestlabel.consignment[0].pieceLine[0].identifier = 1
        desc = ','.join([move.name[0:5] for move in self.move_lines])
        requestlabel.consignment[0].pieceLine[0].goodsDescription = desc[0:30]
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements = tnt.measurementsType()
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.length = 0.01
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.width = 0.01
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.height = 0.01
        requestlabel.consignment[0].pieceLine[0].pieceMeasurements.weight = 0.01

        requestlabel.consignment[0].pieceLine[0].pieces.append(tnt.pieceType())
        requestlabel.consignment[0].pieceLine[0].pieces[0].sequenceNumbers = str(range(1,(self.number_of_packages or 1)+1)).strip('[]').replace(' ','')
        requestlabel.consignment[0].pieceLine[0].pieces[0].pieceReference = 'COMPONENT'
        
        return requestlabel.toxml("utf-8")

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

        raise exceptions.Warning(str(response))
        #if response.Estado != '1' and not response.NumeroEnvio:
        #    raise exceptions.Warning(response.Mensaje)
        #label_factory = self._mrw_etiqueta_envio_request(mrw_api,
        #                                                 response.NumeroEnvio)
        #label_response = client.service.EtiquetaEnvio(label_factory)
        #
        #label = {
        #    'file': label_response.EtiquetaFile.decode('base64'),
        #    'file_type': 'pdf',
        #    'name': response.NumeroEnvio + '.pdf',
        #}
        return [True]

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """ Add label generation for TNT """
        self.ensure_one()
        if self.carrier_id.type == 'tnt':
            return self._generate_tnt_label(package_ids=package_ids)
        return super(StockPicking, self).generate_shipping_labels(
            package_ids=package_ids)
