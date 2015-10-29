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
    dom = etree.parse(xmlname)
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


def toplainstr(value, num_decimals):
    decimal_part = (value - int(value))
    if decimal_part > 0:
        decimal_value = str(int(decimal_part *10*num_decimals)).ljust(num_decimals, '0')
    else:
        decimal_value = ''.zfill(num_decimals)
    result = str(int(value))+decimal_value
    return result

def make_clean(value, paddzeros):
    result = ''
    if paddzeros:
        result = value[1][:value[0]].zfill(value[0])
    else:
        result = value[1][:value[0]].ljust(value[0], ' ')
    return result


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    lines_manifest = fields.Text(string='Lines Manifest')

    @api.multi
    def _tnt_transm_envio_request(self):

        lines_manifest=''
        self.ensure_one()
        message=''
        res=''
        consigment_code = self.env['ir.sequence'].get('tnt.consignment.sequence')
        if consigment_code>self.carrier_id.tnt_config_id.max_range_code or consigment_code<self.carrier_id.tnt_config_id.min_range_code:
            raise exceptions.Warning(_('Invalid consigment code for TNT Range codes, configure sequence Delivery TNT next number'))
        collection_date = get_collection_date(self.carrier_id.tnt_config_id.time)

        requestlabel = tnt.labelRequest()
        requestlabel.consignment.append(tnt.labelConsignmentsType())
        requestlabel.consignment[0].key = 'con1'
        requestlabel.consignment[0].consignmentIdentity = tnt.consignmentIdentityType()
        consigment_code = consigment_code + getTNTDC(consigment_code)
        requestlabel.consignment[0].consignmentIdentity.consignmentNumber =  consigment_code
        requestlabel.consignment[0].consignmentIdentity.customerReference = self.name
        requestlabel.consignment[0].collectionDateTime = collection_date


        requestlabel.consignment[0].sender = tnt.nameAndAddressRequestType()
        warehouse_address = self.picking_type_id.warehouse_id.partner_id
        requestlabel.consignment[0].sender.name = warehouse_address.name
        requestlabel.consignment[0].sender.addressLine1 = warehouse_address.street
        if warehouse_address.street2:
            requestlabel.consignment[0].sender.addressLine2 = warehouse_address.street2
        if warehouse_address.city:
            requestlabel.consignment[0].sender.town = warehouse_address.city
            requestlabel.consignment[0].sender.exactMatch = 'N'
        if warehouse_address.state_id:
            requestlabel.consignment[0].sender.province = warehouse_address.state_id.name or ''
        if warehouse_address.zip:
            requestlabel.consignment[0].sender.postcode = warehouse_address.zip.zfill(5)
        requestlabel.consignment[0].sender.country = warehouse_address.country_id.code or ''


        requestlabel.consignment[0].delivery = tnt.nameAndAddressRequestType()
        requestlabel.consignment[0].delivery.name = (self.partner_id and self.partner_id.parent_id and self.partner_id.parent_id.name) or (self.partner_id and self.partner_id.name) or ''
        requestlabel.consignment[0].delivery.addressLine1 = self.partner_id.street
        if self.partner_id.street2:
            requestlabel.consignment[0].delivery.addressLine2 = self.partner_id.street2
        if self.partner_id.city:
            requestlabel.consignment[0].delivery.town = self.partner_id.city
            requestlabel.consignment[0].delivery.exactMatch = 'N'
        if self.partner_id.state_id:
            requestlabel.consignment[0].delivery.province = self.partner_id.state_id.name
        if self.partner_id.zip:
            requestlabel.consignment[0].delivery.postcode = self.partner_id.zip.zfill(5)
        requestlabel.consignment[0].delivery.country = self.partner_id.country_id.code or ''

        requestlabel.consignment[0].contact = tnt.contactType()
        requestlabel.consignment[0].contact.name = (self.partner_id and self.partner_id.parent_id and self.partner_id.parent_id.name) or (self.partner_id and self.partner_id.name) or ''
        if self.partner_id.phone:
            requestlabel.consignment[0].contact.telephoneNumber = self.partner_id.phone
        if self.partner_id.email:
            requestlabel.consignment[0].contact.emailAddress = self.partner_id.email

        requestlabel.consignment[0].product = tnt.productType()
        requestlabel.consignment[0].product.lineOfBusiness = '1'
        requestlabel.consignment[0].product.groupId = '0'
        requestlabel.consignment[0].product.subGroupId = '0'
        requestlabel.consignment[0].product.id = 'EX'
        requestlabel.consignment[0].product.type = 'N'

        requestlabel.consignment[0].account = tnt.accountType()
        if self.carrier_id.tnt_config_id.is_test:
            requestlabel.consignment[0].account.accountNumber = '1234567'
        else:
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

        zeros_fill = ['con_sender_acc_id',  'con_opsa_tgrs_wt', 'con_oa_tot_vl', 'con_tot_piece_qt', 'con_ins_am', 'con_coll_tm_hh', 'con_val_of_goods_am', 'con_oc_tot_vl', 'con_oc_tgrs_wt', 'condim_vl', 'condim_wt', 'condim_qt']

        #Ponemos valor a cada variable
        #Solicitar a TNT Trading Partner
        size_values={'to_user':[8,''],
            'transmission_cd':[20,'Preguntar a TNT'],########################
            'con_sender_acc_id':[9, self.carrier_id.tnt_config_id.account_number or ''],
            'con_id':[15,consigment_code],
            'pack_id':[10,''],
            'pack_id2':[3,'1'],
            'rec_id0':[2,'00'],
            'rec_id1':[2,'01'],
            'rec_id2':[2,'02'],
            'rec_id3':[2,'03'],
            'edi_vers_no':[14,'1.001105090002'],
            'conversion_type':[35,''],
            'origin_system':[20,'ISOLUTIONS'],
            'system_version':[8,'4.03. 11'],
            'sys_code':[59,''],
            'con_com_id':[2,'WW'],
            'con_opsa_tgrs_wt':[8,toplainstr((self.weight or 1), 3)],
            'con_oa_tot_vl':[7,toplainstr((self.number_of_packages or 1)*(self.carrier_id.tnt_config_id.height_package*self.carrier_id.tnt_config_id.width_package*self.carrier_id.tnt_config_id.length_package),3)],
            'con_tot_piece_qt':[5,str(self.number_of_packages or 1)],
            'con_div_id':[3,'D'],
            'con_prd_id_contr':[4,'15N'],
            'con_ins_am':[13,''],
            'con_cuy_id_ins':[3,''],
            'con_cuy_id_cust_ins':[3,''],
            'con_packing_ds':[20,'CAJA'],
            'con_clnt_ref_tx':[24,self.name],
            'con_coll_dt_cc':[8,collection_date[:collection_date.index('T')].replace('-', '')],
            'con_coll_tm_hh':[4,''],
            'con_val_of_goods_am':[13,''],
            'con_cuy_id_val_of_goods':[3,'EUR'],
            'con_cuy_id_cust_val_of_goods':[3,'EUR'],
            'con_oc_tot_vl':[6,toplainstr((self.number_of_packages or 1)*(self.carrier_id.tnt_config_id.height_package*self.carrier_id.tnt_config_id.width_package*self.carrier_id.tnt_config_id.length_package),3)],
            'con_ops_instr_tx':[60,''],
            'con_oc_tgrs_wt':[7,toplainstr((self.weight or 1), 3)],
            'con_option_1':[3,''],
            'con_option_2':[3,''],
            'con_option_3':[3,''],
            'con_option_4':[3,''],
            'con_top_id_ops_act':[1,'S'],
            'con_cnd_note_src_cd':[48,'ED61201'],
            'con_cmr':[1,'N'],
            'con_label_in':[1,'Y'],
            'con_haz_in':[2,'N'],
            'con_haz_in_2':[37,''],
            'con_cod_in':[1,''],
            'con_delivery_in_in':[217,''],
            'con_cod_am':[13,''],
            'con_cuy_id_cod':[3,''],
            'con_cust_trade_tx':[121,''],
            'con_goods_ds':[30,'CAJA'],
            'con_ooq_am':[36,''],
            'con_un_cd':[4,''],
            'con_hax_cd':[4,''],
            'con_third_party_in':[5,''],
            'con_cod_type_cd':[1,''],
            'bul_id_special':[95,''],
            'controlled_in':[1,''],
            'ex_warehouse_in':[58,''],

            'art_id':[7,''],
            'condim_vl':[7,toplainstr((self.number_of_packages or 1)*(self.carrier_id.tnt_config_id.height_package*self.carrier_id.tnt_config_id.width_package*self.carrier_id.tnt_config_id.length_package),3)],
            'condim_wt':[8,toplainstr((self.weight or 1), 3)],
            'condim_ln':[6,''],
            'condim_ht':[6,''],
            'condim_wd':[6,''],
            'condim_qt':[5,str(self.number_of_packages or 1)],

            'cpn_id_s':[2,'S'],
            'cpn_vat_id_s':[20,''],
            'cpn_addr_1_ds_s':[90,warehouse_address.street or ''],
            'cpn_pcode_cd_s':[9,warehouse_address.zip and warehouse_address.zip.zfill(5) or ''],
            'cpn_tel_1_id_s':[16,''],
            'cpn_acc_id_s':[9,self.carrier_id.tnt_config_id.account_number or ''],
            'cpn_nm_s':[50,warehouse_address.name or ''],
            'cpn_cou_id_s':[3,'ES'],
            'cpn_cpf_tel_1_id_s':[16,''],
            'cpn_city_nm_s':[30,''],
            'cpn_cpf_last_nm_s':[22,warehouse_address.city or ''],
            'cpn_fax_1_id_s':[16,''],
            'cpn_telex_1_id_s':[9,''],
            'cpn_prv_nm_s':[30,''],
            'cpn_cust_cou_id_s':[53,''],
            'con_email_address_s':[50,''],
            'con_sms1_id_s':[16,''],

            'cpn_id_r':[2,'R'],
            'cpn_vat_id_r':[20,''],
            'cpn_addr_1_ds_r':[90,self.partner_id.street or ''],
            'cpn_pcode_cd_r':[9,self.partner_id.zip and self.partner_id.zip.zfill(5) or ''],
            'cpn_tel_1_id_r':[16,''],
            'cpn_acc_id_r':[9,''],
            'cpn_nm_r':[50,(self.partner_id and self.partner_id.parent_id and self.partner_id.parent_id.name) or (self.partner_id and self.partner_id.name) or ''],
            'cpn_cou_id_r':[3,'ES'],
            'cpn_cpf_tel_1_id_r':[16,''],
            'cpn_city_nm_r':[30,self.partner_id.city or ''],
            'cpn_cpf_last_nm_r':[22,''],
            'cpn_fax_1_id_r':[16,''],
            'cpn_telex_1_id_r':[9,''],
            'cpn_prv_nm_r':[30,''],
            'cpn_cust_cou_id_r':[53,''],
            'con_email_address_r':[50,self.partner_id.email or ''],
            'con_sms1_id_r':[16,self.partner_id.mobile or self.partner_id.phone or '']}


        #Por cada albaran vamos a construir un registro de tipo 0,1,2,3S y 3R
        line_00 = ['to_user',
                    'transmission_cd',
                    'con_sender_acc_id',
                    'con_id',
                    'pack_id',
                    'rec_id0',
                    'edi_vers_no',
                    'conversion_type',
                    'origin_system',
                    'system_version',
                    'sys_code']

        line_01 = ['to_user',
                    'transmission_cd',
                    'con_sender_acc_id',
                    'con_id',
                    'pack_id',
                    'rec_id1',
                    'con_com_id',
                    'con_opsa_tgrs_wt',
                    'con_oa_tot_vl',
                    'con_tot_piece_qt',
                    'con_div_id',
                    'con_prd_id_contr',
                    'con_ins_am',
                    'con_cuy_id_ins',
                    'con_cuy_id_cust_ins',
                    'con_packing_ds',
                    'con_clnt_ref_tx',
                    'con_coll_dt_cc',
                    'con_coll_tm_hh',
                    'con_val_of_goods_am',
                    'con_cuy_id_val_of_goods',
                    'con_cuy_id_cust_val_of_goods',
                    'con_oc_tot_vl',
                    'con_ops_instr_tx',
                    'con_oc_tgrs_wt',
                    'con_option_1',
                    'con_option_2',
                    'con_option_3',
                    'con_option_4',
                    'con_top_id_ops_act',
                    'con_cnd_note_src_cd',
                    'con_cmr',
                    'con_label_in',
                    'con_haz_in',
                    'con_haz_in_2',
                    'con_cod_in',
                    'con_delivery_in_in',
                    'con_cod_am',
                    'con_cuy_id_cod',
                    'con_cust_trade_tx',
                    'con_goods_ds',
                    'con_ooq_am',
                    'con_un_cd',
                    'con_hax_cd',
                    'con_third_party_in',
                    'con_cod_type_cd',
                    'bul_id_special',
                    'controlled_in',
                    'ex_warehouse_in']

        line_02 = ['to_user',
                    'transmission_cd',
                    'con_sender_acc_id',
                    'con_id',
                    'pack_id2',
                    'art_id',
                    'rec_id2',
                    'condim_vl',
                    'condim_wt',
                    'condim_ln',
                    'condim_ht',
                    'condim_wd',
                    'condim_qt']

        line_03s = ['to_user',
                    'transmission_cd',
                    'con_sender_acc_id',
                    'con_id',
                    'pack_id',
                    'rec_id3',
                    'cpn_id_s',
                    'cpn_vat_id_s',
                    'cpn_addr_1_ds_s',
                    'cpn_pcode_cd_s',
                    'cpn_tel_1_id_s',
                    'cpn_acc_id_s',
                    'cpn_nm_s',
                    'cpn_cou_id_s',
                    'cpn_cpf_tel_1_id_s',
                    'cpn_city_nm_s',
                    'cpn_cpf_last_nm_s',
                    'cpn_fax_1_id_s',
                    'cpn_telex_1_id_s',
                    'cpn_prv_nm_s',
                    'cpn_cust_cou_id_s',
                    'con_email_address_s',
                    'con_sms1_id_s']


        line_03r = ['to_user',
                    'transmission_cd',
                    'con_sender_acc_id',
                    'con_id',
                    'pack_id',
                    'rec_id3',
                    'cpn_id_r',
                    'cpn_vat_id_r',
                    'cpn_addr_1_ds_r',
                    'cpn_pcode_cd_r',
                    'cpn_tel_1_id_r',
                    'cpn_acc_id_r',
                    'cpn_nm_r',
                    'cpn_cou_id_r',
                    'cpn_cpf_tel_1_id_r',
                    'cpn_city_nm_r',
                    'cpn_cpf_last_nm_r',
                    'cpn_fax_1_id_r',
                    'cpn_telex_1_id_r',
                    'cpn_prv_nm_r',
                    'cpn_cust_cou_id_r',
                    'con_email_address_r',
                    'con_sms1_id_r']

        str_line00 = ''
        for field in line_00:
            str_line00 = str_line00 + make_clean(size_values.get(field), field in zeros_fill)

        str_line01 = ''
        for field in line_01:
            str_line01 = str_line01 + make_clean(size_values.get(field), field in zeros_fill)

        str_line02 = ''
        for field in line_02:
            str_line02 = str_line02 + make_clean(size_values.get(field), field in zeros_fill)

        str_line03s = ''
        for field in line_03s:
            str_line03s = str_line03s + make_clean(size_values.get(field), field in zeros_fill)

        str_line03r = ''
        for field in line_03r:
            str_line03r = str_line03r + make_clean(size_values.get(field), field in zeros_fill)

        lines_manifest = str_line00 + "\n" + str_line01 + "\n" + str_line02 + "\n" + str_line03s + "\n" + str_line03r
        try:
            host = "express.tnt.com"
            url = "/expresslabel/documentation/getlabel"
            username = self.carrier_id.tnt_config_id.username
            password = self.carrier_id.tnt_config_id.password
            if self.carrier_id.tnt_config_id.is_test:
                username = username + "_Test"
                password = password + "_Test"
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
        except:
            raise exceptions.Warning(_('Error sending XML Request'))

        return res, lines_manifest

    @api.multi
    def _generate_tnt_label(self, package_ids=None):
        self.ensure_one()
        if not self.carrier_id.tnt_config_id:
            raise exceptions.Warning(_('No TNT Config defined in carrier'))
        if not self.picking_type_id.warehouse_id.partner_id:
            raise exceptions.Warning(
                _('Please define an address in the %s warehouse') % (
                    self.warehouse_id.name))
        response, lines_manifest = self._tnt_transm_envio_request()
        if "<consignmentLabelData>" not in response:
            raise exceptions.Warning(("Error in xml communication: %s") % (response))
        file_to_del = []
        with tempfile.NamedTemporaryFile(suffix="response.xml",
                                         delete=False) as xml_file:
            xml_file.write(response)
        xml_name = xml_file.name
        file_to_del.append(xml_file.name)
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        label_pdf=transform(self.name, current_path, xml_name,'/HTMLRoutingLabelRenderer_Local.xsl')
        self.lines_manifest = lines_manifest
        self.datetime_label = datetime.now()
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
        file_to_del.append(out_filename)
        if webkit_path:
            command = [webkit_path]
            command.append('--quiet')
            command.extend(['--encoding', 'utf-8'])
            command.extend(['--page-height', '157'])
            command.extend(['--page-width', '120'])
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
