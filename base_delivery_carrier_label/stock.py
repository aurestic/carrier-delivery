# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: David BEAL <david.beal@akretion.com>
#             Sébastien BEAU <sebastien.beau@akretion.com>
#    Copyright (C) 2012-TODAY Akretion <http://www.akretion.com>.
#    Author: Yannick Vaucher <yannick.vaucher@camptocamp.com>
#    Copyright 2013-2014 Camptocamp SA
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
from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError
import openerp.addons.decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    weight = fields.Float(
        digits=dp.get_precision('Stock Weight'),
        help="Weight of the pack_operation"
    )

    @api.multi
    def get_weight(self):
        """Calc and save weight of pack.operations.

        Warning: Type conversion not implemented
                it will return False if at least one uom or uos not in kg
        return:
            the sum of the weight of [self]
        """
        total_weight = 0
        kg = self.env.ref('product.product_uom_kgm').id
        units = self.env.ref('product.product_uom_unit').id
        allowed = (False, kg, units)
        cant_calc_total = False

        for operation in self:
            product = operation.product_id

            # if not defined we assume it's in kg
            if not (
                product.uom_id.id in allowed or
                product.uos_id.id in allowed
            ):
                _logger.warning(
                    'Type conversion not implemented for product %s' %
                    product.id)
                cant_calc_total = True
            weight = product.weight or product.weight_net
            operation.weight = (weight * operation.product_qty)

            total_weight += operation.weight

        if cant_calc_total:
            return False
        return total_weight


class StockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    parcel_tracking = fields.Char(string='Parcel Tracking')
    weight = fields.Float(
        digits=dp.get_precision('Stock Weight'),
        help="Total weight of the package in kg, including the "
             "weight of the logistic unit."
    )

    @api.multi
    def _complete_name(self, name, args):
        res = super(StockQuantPackage, self)._complete_name(name, args)
        for pack in self:
            if pack.parcel_tracking:
                res[pack.id] += ' [%s]' % pack.parcel_tracking
            if pack.weight:
                res[pack.id] += ' %s kg' % pack.weight
        return res

    @api.multi
    def get_weight(self):
        """Compute the weight of a pack.

        Get all the children packages and sum the weight of all
        the product and the weight of the Logistic Units of the packages.

        So if I put in PACK65:
         * 1 product A of 2kg
         * 2 products B of 4kg
        The box of PACK65 weights 0.5kg
        And I put in PACK66:
         * 1 product A of 2kg
        The box of PACK66 weights 0.5kg

        Then I put PACK65 and PACK66 in the PACK67 having a box that
        weights 0.5kg, the weight of PACK67 should be: 13.5kg

        """
        total_weight = 0

        for package in self:
            # weight of the wrapper
            packaging_weight = 0
            if package.ul_id:
                packaging_weight = package.ul_id.weight

            # package.pack_operations would be too easy
            operations = self.env['stock.pack.operation'].search(
                [('result_package_id', '=', package.id),
                 ('product_id', '!=', False),
                 ])

            # we make use get_weight with  @api.muli instead of
            # sum([op.get_weight for op in operations])

            # sum of the pack_operation
            payload_weight = operations.get_weight()

            # sum of the packages contained in this package (children)
            child_packages_weight = package.children_ids.get_weight()

            # sum and save in package
            package.weight = (
                payload_weight +
                child_packages_weight +
                packaging_weight)

            total_weight += package.weight

        return total_weight


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def _get_carrier_type_selection(self):
        carrier_obj = self.env['delivery.carrier']
        return carrier_obj._get_carrier_type_selection()

    carrier_id = fields.Many2one(
        comodel_name='delivery.carrier',
        string='Carrier',
        states={'done': [('readonly', True)]},
    )
    carrier_type = fields.Selection(
        related='carrier_id.type',
        string='Carrier Type',
        readonly=True,
    )
    carrier_code = fields.Char(
        related='carrier_id.code',
        readonly=True,
    )
    option_ids = fields.Many2many(comodel_name='delivery.carrier.option',
                                  string='Options')

    @api.multi
    def generate_default_label(self, package_ids=None):
        """ Abstract method

        :param package_ids: optional list of ``stock.quant.package`` ids
                            only packs in this list will have their label
                            printed (all are generated when None)

        :return: (file_binary, file_type)

        """
        raise UserError(_('No label is configured for the '
                          'selected delivery method.'))

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        """Generate a shipping label by default

        This method can be inherited to create specific shipping labels
        a list of label must be return as we can have multiple
        stock.quant.package for a single picking representing packs

        :param package_ids: optional list of ``stock.quant.package`` ids
                             only packs in this list will have their label
                             printed (all are generated when None)

        :return: list of dict containing
           name: name to give to the attachement
           file: file as string
           file_type: string of file type like 'PDF'
           (optional)
           tracking_id: tracking_id if picking lines have tracking_id and
                        if label generator creates shipping label per
                        pack

        """
        default_label = self.generate_default_label(package_ids=package_ids)
        if not package_ids:
            return [default_label]
        labels = []
        for package_id in package_ids:
            pack_label = default_label.copy()
            pack_label['tracking_id'] = package_id
            labels.append(pack_label)
        return labels

    @api.multi
    def generate_labels(self, package_ids=None):
        """ Generate the labels.

        A list of package ids can be given, in that case it will generate
        the labels only of these packages.

        """
        label_obj = self.env['shipping.label']

        for pick in self:
            if package_ids:
                shipping_labels = pick.generate_shipping_labels(
                    package_ids=package_ids
                )
            else:
                shipping_labels = pick.generate_shipping_labels()
            for label in shipping_labels:
                data = {
                    'name': label['name'],
                    'res_id': pick.id,
                    'res_model': 'stock.picking',
                    'datas': label['file'].encode('base64'),
                    'file_type': label['file_type'],
                }
                if label.get('package_id'):
                    data['package_id'] = label['package_id']
                context_attachment = self.env.context.copy()
                # remove default_type setted for stock_picking
                # as it would try to define default value of attachement
                if 'default_type' in context_attachment:
                    del context_attachment['default_type']
                label_obj.with_context(context_attachment).create(data)
        return True

    @api.multi
    def action_generate_carrier_label(self):
        """ Method for the 'Generate Label' button.

        It will generate the labels for all the packages of the picking.

        """
        return self.generate_labels()

    @api.onchange('carrier_id')
    def carrier_id_change(self):
        """ Inherit this method in your module """
        if not self.carrier_id:
            return
        # This can look useless as the field carrier_code and
        # carrier_type are related field. But it's needed to fill
        # this field for using this fields in the view. Indeed the
        # module that depend of delivery base can hide some field
        # depending of the type or the code
        carrier = self.carrier_id
        self.carrier_type = carrier.type
        self.carrier_code = carrier.code
        self.option_ids = carrier.default_options()
        result = {
            'domain': {
                'option_ids': [('id', 'in', carrier.available_option_ids.ids)],
            }
        }
        return result

    @api.onchange('option_ids')
    def option_ids_change(self):
        if not self.carrier_id:
            return
        carrier = self.carrier_id
        for available_option in carrier.available_option_ids:
            if (available_option.mandatory and
                    available_option not in self.option_ids):
                # XXX the client does not allow to modify the field that
                # triggered the onchange:
                # https://github.com/odoo/odoo/issues/2693#issuecomment-56825399
                # Ideally we should add the missing option
                raise UserError(
                    _("You should not remove a mandatory option."
                      "Please cancel the edit or "
                      "add back the option: %s.") % available_option.name
                )

    @api.model
    def _values_with_carrier_options(self, values):
        values = values.copy()
        carrier_id = values.get('carrier_id')
        option_ids = values.get('option_ids')
        if carrier_id and not option_ids:
            carrier_obj = self.env['delivery.carrier']
            carrier = carrier_obj.browse(carrier_id)
            default_options = carrier.default_options()
            if default_options:
                values.update(option_ids=[(6, 0, default_options.ids)])
        return values

    @api.multi
    @api.returns('stock.quant.package')
    def _get_packages_from_picking(self):
        """ Get all the packages from the picking """
        self.ensure_one()
        operation_obj = self.env['stock.pack.operation']
        packages = self.env['stock.quant.package'].browse()
        operations = operation_obj.search(
            ['|',
             ('package_id', '!=', False),
             ('result_package_id', '!=', False),
             ('picking_id', '=', self.id)]
        )
        for operation in operations:
            # Take the destination package. If empty, the package is
            # moved so take the source one.
            packages |= operation.result_package_id or operation.package_id
        return packages

    @api.multi
    def write(self, vals):
        """ Set the default options when the delivery method is changed.

        So we are sure that the options are always in line with the
        current delivery method.

        """
        vals = self._values_with_carrier_options(vals)
        return super(StockPicking, self).write(vals)

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        """ Trigger carrier_id_change on create

        To ensure options are setted on the basis of carrier_id copied from
        Sale order or defined by default.

        """
        vals = self._values_with_carrier_options(vals)
        return super(StockPicking, self).create(vals)

    @api.multi
    def _get_label_sender_address(self):
        """ On each carrier label module you need to define
            which is the sender of the parcel.
            The most common case is 'picking.company_id.partner_id'
            and then choose the contact which has the type 'delivery'
            which is suitable for each delivery carrier label module.
            But your client might want to customize sender address
            if he has several brands and/or shops in his company.
            In this case he doesn't want his customer to see
            the address of his company in his transport label
            but instead, the address of the partner linked to his shop/brand

            To reach this modularity, call this method to get sender address
            in your delivery_carrier_label_yourcarrier module, then every
            developer can manage specific needs by inherit this method in
            module like :
            delivery_carrier_label_yourcarrier_yourproject.
        """
        self.ensure_one()
        partner = self.company_id.partner_id
        address_id = partner.address_get(adr_pref=['delivery'])['delivery']
        return self.env['res.partner'].browse(address_id)

    @api.multi
    def set_pack_weight(self):
        # I cannot loop on the "quant_ids" of packages, because, at this step,
        # this field doesn't have a value yet
        self.ensure_one()
        for packop in self.pack_operation_ids:
            package = packop.result_package_id or packop.package_id
            if package:
                weight = package.get_weight()
                package.write({'weight': weight})
        return

    @api.multi
    def _check_existing_shipping_label(self):
        """ Check that labels don't already exist for this picking """
        self.ensure_one()
        labels = self.env['shipping.label'].search([
            ('res_id', '=', self.id),
            ('res_model', '=', 'stock.picking')])
        if labels:
            raise UserError(
                _('Some labels already exist for the picking %s.\n'
                  'Please delete the existing labels in the '
                  'attachments of this picking and try again')
                % self.name)


class ShippingLabel(models.Model):
    """ Child class of ir attachment to identify which are labels """

    _name = 'shipping.label'
    _inherits = {'ir.attachment': 'attachment_id'}
    _description = "Shipping Label"

    @api.model
    def _get_file_type_selection(self):
        """ To inherit to add file type """
        return [('pdf', 'PDF')]

    @api.model
    def __get_file_type_selection(self):
        file_types = self._get_file_type_selection()
        file_types = list(set(file_types))
        file_types.sort(key=lambda t: t[0])
        return file_types

    file_type = fields.Selection(
        selection=__get_file_type_selection,
        string='File type',
        default='pdf',
    )
    package_id = fields.Many2one(comodel_name='stock.quant.package',
                                 string='Pack')
    attachment_id = fields.Many2one(
        comodel_name='ir.attachment',
        string='Attachement',
        required=True,
        ondelete='cascade',
    )
