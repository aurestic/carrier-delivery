# ./tnt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-10-15 13:59:44.455367 by PyXB version 1.2.4 using Python 2.7.4.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:38d7e6ac-7334-11e5-b763-c8600052b5f5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: stringMinLength2MaxLength2
class stringMinLength2MaxLength2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMinLength2MaxLength2')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 406, 4)
    _Documentation = None
stringMinLength2MaxLength2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
stringMinLength2MaxLength2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
stringMinLength2MaxLength2._InitializeFacetMap(stringMinLength2MaxLength2._CF_maxLength,
   stringMinLength2MaxLength2._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'stringMinLength2MaxLength2', stringMinLength2MaxLength2)

# Atomic simple type: stringMinLength3MaxLength3
class stringMinLength3MaxLength3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMinLength3MaxLength3')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 413, 4)
    _Documentation = None
stringMinLength3MaxLength3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
stringMinLength3MaxLength3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
stringMinLength3MaxLength3._InitializeFacetMap(stringMinLength3MaxLength3._CF_maxLength,
   stringMinLength3MaxLength3._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'stringMinLength3MaxLength3', stringMinLength3MaxLength3)

# Atomic simple type: stringMaxLength4
class stringMaxLength4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength4')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 420, 4)
    _Documentation = None
stringMaxLength4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
stringMaxLength4._InitializeFacetMap(stringMaxLength4._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength4', stringMaxLength4)

# Atomic simple type: stringMaxLength9
class stringMaxLength9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength9')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 426, 4)
    _Documentation = None
stringMaxLength9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
stringMaxLength9._InitializeFacetMap(stringMaxLength9._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength9', stringMaxLength9)

# Atomic simple type: stringMaxLength10
class stringMaxLength10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength10')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 432, 3)
    _Documentation = None
stringMaxLength10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
stringMaxLength10._InitializeFacetMap(stringMaxLength10._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength10', stringMaxLength10)

# Atomic simple type: stringMaxLength30
class stringMaxLength30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength30')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 438, 4)
    _Documentation = None
stringMaxLength30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stringMaxLength30._InitializeFacetMap(stringMaxLength30._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength30', stringMaxLength30)

# Atomic simple type: stringMaxLength40
class stringMaxLength40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength40')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 444, 4)
    _Documentation = None
stringMaxLength40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
stringMaxLength40._InitializeFacetMap(stringMaxLength40._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength40', stringMaxLength40)

# Atomic simple type: stringMaxLength100
class stringMaxLength100 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringMaxLength100')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 450, 4)
    _Documentation = None
stringMaxLength100._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
stringMaxLength100._InitializeFacetMap(stringMaxLength100._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stringMaxLength100', stringMaxLength100)

# Atomic simple type: doubleTwoDecimalPlaces
class doubleTwoDecimalPlaces (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleTwoDecimalPlaces')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 456, 4)
    _Documentation = None
doubleTwoDecimalPlaces._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
doubleTwoDecimalPlaces._InitializeFacetMap(doubleTwoDecimalPlaces._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'doubleTwoDecimalPlaces', doubleTwoDecimalPlaces)

# Atomic simple type: doubleMaxExclusive100MinInclusive0.01
class doubleMaxExclusive100MinInclusive0_01 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleMaxExclusive100MinInclusive0.01')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 462, 4)
    _Documentation = None
doubleMaxExclusive100MinInclusive0_01._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=doubleMaxExclusive100MinInclusive0_01, value=pyxb.binding.datatypes.double(0.01))
doubleMaxExclusive100MinInclusive0_01._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType('100'))
doubleMaxExclusive100MinInclusive0_01._InitializeFacetMap(doubleMaxExclusive100MinInclusive0_01._CF_minInclusive,
   doubleMaxExclusive100MinInclusive0_01._CF_maxExclusive)
Namespace.addCategoryObject('typeBinding', 'doubleMaxExclusive100MinInclusive0.01', doubleMaxExclusive100MinInclusive0_01)

# Atomic simple type: doubleMaxExclusive100000MinInclusive0.01
class doubleMaxExclusive100000MinInclusive0_01 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleMaxExclusive100000MinInclusive0.01')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 469, 4)
    _Documentation = None
doubleMaxExclusive100000MinInclusive0_01._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=doubleMaxExclusive100000MinInclusive0_01, value=pyxb.binding.datatypes.double(0.01))
doubleMaxExclusive100000MinInclusive0_01._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType('100000'))
doubleMaxExclusive100000MinInclusive0_01._InitializeFacetMap(doubleMaxExclusive100000MinInclusive0_01._CF_minInclusive,
   doubleMaxExclusive100000MinInclusive0_01._CF_maxExclusive)
Namespace.addCategoryObject('typeBinding', 'doubleMaxExclusive100000MinInclusive0.01', doubleMaxExclusive100000MinInclusive0_01)

# Atomic simple type: longMaxLength10
class longMaxLength10 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longMaxLength10')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 476, 4)
    _Documentation = None
longMaxLength10._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=longMaxLength10, value=pyxb.binding.datatypes.long(0))
longMaxLength10._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.long, value=pyxb.binding.datatypes.integer(10000000000))
longMaxLength10._InitializeFacetMap(longMaxLength10._CF_minInclusive,
   longMaxLength10._CF_maxExclusive)
Namespace.addCategoryObject('typeBinding', 'longMaxLength10', longMaxLength10)

# Atomic simple type: integerMin0Max9
class integerMin0Max9 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerMin0Max9')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 483, 4)
    _Documentation = None
integerMin0Max9._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=integerMin0Max9, value=pyxb.binding.datatypes.int(0))
integerMin0Max9._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=integerMin0Max9, value=pyxb.binding.datatypes.int(9))
integerMin0Max9._InitializeFacetMap(integerMin0Max9._CF_minInclusive,
   integerMin0Max9._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'integerMin0Max9', integerMin0Max9)

# Atomic simple type: productTypeEnum
class productTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'productTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 490, 4)
    _Documentation = None
productTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=productTypeEnum, enum_prefix=None)
productTypeEnum.N = productTypeEnum._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
productTypeEnum.D = productTypeEnum._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
productTypeEnum._InitializeFacetMap(productTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'productTypeEnum', productTypeEnum)

# Atomic simple type: booleanEnum
class booleanEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'booleanEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 497, 4)
    _Documentation = None
booleanEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=booleanEnum, enum_prefix=None)
booleanEnum.N = booleanEnum._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
booleanEnum.Y = booleanEnum._CF_enumeration.addEnumeration(unicode_value='Y', tag='Y')
booleanEnum._InitializeFacetMap(booleanEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'booleanEnum', booleanEnum)

# Atomic simple type: senderReceiverEnum
class senderReceiverEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'senderReceiverEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 504, 4)
    _Documentation = None
senderReceiverEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=senderReceiverEnum, enum_prefix=None)
senderReceiverEnum.S = senderReceiverEnum._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
senderReceiverEnum.R = senderReceiverEnum._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
senderReceiverEnum._InitializeFacetMap(senderReceiverEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'senderReceiverEnum', senderReceiverEnum)

# Atomic simple type: cashTypeEnum
class cashTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cashTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 511, 4)
    _Documentation = None
cashTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cashTypeEnum, enum_prefix=None)
cashTypeEnum.n0 = cashTypeEnum._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
cashTypeEnum.n1 = cashTypeEnum._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
cashTypeEnum._InitializeFacetMap(cashTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'cashTypeEnum', cashTypeEnum)

# Complex type consignmentIdentityType with content type ELEMENT_ONLY
class consignmentIdentityType (pyxb.binding.basis.complexTypeDefinition):
    """This element contains a consignment number and optional customer reference. 
                These values are used to distinguish a consignment from any other consignment. 

                This value appears on a routing label and is used as the key for a consignment."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'consignmentIdentityType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 7, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element consignmentNumber uses Python identifier consignmentNumber
    __consignmentNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'consignmentNumber'), 'consignmentNumber', '__AbsentNamespace0_consignmentIdentityType_consignmentNumber', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 15, 12), )

    
    consignmentNumber = property(__consignmentNumber.value, __consignmentNumber.set, None, 'The TNT consignment number in legacy (Global Link) format.')

    
    # Element customerReference uses Python identifier customerReference
    __customerReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'customerReference'), 'customerReference', '__AbsentNamespace0_consignmentIdentityType_customerReference', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 20, 12), )

    
    customerReference = property(__customerReference.value, __customerReference.set, None, 'Contains the optional customer reference for the consignment. \n                        A customer reference is a way for a customer to designate a name \n                        for the consignment.\n                        \n                        This value can be used to track the consignment at a later date.')

    _ElementMap.update({
        __consignmentNumber.name() : __consignmentNumber,
        __customerReference.name() : __customerReference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'consignmentIdentityType', consignmentIdentityType)


# Complex type nameAndAddressRequestType with content type ELEMENT_ONLY
class nameAndAddressRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Information relating to name and address for a participant 
                in the consignment.
                 
                Examples of a participant are:
                 
                The Sender - the company sending the consignment
                The Receiver - the company receiving the consignment
                The Collection Address - the address from which the consignment is picked up
                The Delivery Address - the address to which the consignment should be delivered"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAndAddressRequestType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_nameAndAddressRequestType_name', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 45, 12), )

    
    name = property(__name.value, __name.set, None, 'Either the name of the company as recognised by TNT, or the \n                        contact name at the address')

    
    # Element addressLine1 uses Python identifier addressLine1
    __addressLine1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine1'), 'addressLine1', '__AbsentNamespace0_nameAndAddressRequestType_addressLine1', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 51, 12), )

    
    addressLine1 = property(__addressLine1.value, __addressLine1.set, None, 'This address line is the most commonly used of the three \n                        address lines and is therefore mandatory.')

    
    # Element addressLine2 uses Python identifier addressLine2
    __addressLine2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine2'), 'addressLine2', '__AbsentNamespace0_nameAndAddressRequestType_addressLine2', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 57, 12), )

    
    addressLine2 = property(__addressLine2.value, __addressLine2.set, None, 'This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address.')

    
    # Element addressLine3 uses Python identifier addressLine3
    __addressLine3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine3'), 'addressLine3', '__AbsentNamespace0_nameAndAddressRequestType_addressLine3', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 63, 12), )

    
    addressLine3 = property(__addressLine3.value, __addressLine3.set, None, 'This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address. \n                        NOTE - this will not appear on any routingLabel produced.')

    
    # Element town uses Python identifier town
    __town = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'town'), 'town', '__AbsentNamespace0_nameAndAddressRequestType_town', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 70, 12), )

    
    town = property(__town.value, __town.set, None, 'The town name as recognised by TNT')

    
    # Element exactMatch uses Python identifier exactMatch
    __exactMatch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'exactMatch'), 'exactMatch', '__AbsentNamespace0_nameAndAddressRequestType_exactMatch', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 75, 12), )

    
    exactMatch = property(__exactMatch.value, __exactMatch.set, None, "Flag stating if an exact match on the town name should be used. \n                        If this flag is absent then the exact match value is 'Y'.")

    
    # Element province uses Python identifier province
    __province = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'province'), 'province', '__AbsentNamespace0_nameAndAddressRequestType_province', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 81, 12), )

    
    province = property(__province.value, __province.set, None, 'Optional field to contain the province, county, state, or area \n                        for the given address.')

    
    # Element postcode uses Python identifier postcode
    __postcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'postcode'), 'postcode', '__AbsentNamespace0_nameAndAddressRequestType_postcode', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 87, 12), )

    
    postcode = property(__postcode.value, __postcode.set, None, 'Postcode or zip code is considered a mandatory field where it is \n                        used in a given country. If the postcode is not provided, it may \n                        not be possible to deliver the consignment as indicated by your\n                        chosen service.')

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'country'), 'country', '__AbsentNamespace0_nameAndAddressRequestType_country', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 95, 12), )

    
    country = property(__country.value, __country.set, None, 'The ISO country code for the country of the given address.')

    _ElementMap.update({
        __name.name() : __name,
        __addressLine1.name() : __addressLine1,
        __addressLine2.name() : __addressLine2,
        __addressLine3.name() : __addressLine3,
        __town.name() : __town,
        __exactMatch.name() : __exactMatch,
        __province.name() : __province,
        __postcode.name() : __postcode,
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'nameAndAddressRequestType', nameAndAddressRequestType)


# Complex type nameAndAddressResponseType with content type ELEMENT_ONLY
class nameAndAddressResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Information relating to name and address for a participant 
                in the consignment.
                 
                Examples of a participant are:
                 
                The Sender - the company sending the consignment
                The Receiver - the company receiving the consignment
                The Collection Address - the address from which the consignment is picked up
                The Delivery Address - the address to which the consignment should be delivered"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAndAddressResponseType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 103, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_nameAndAddressResponseType_name', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 116, 12), )

    
    name = property(__name.value, __name.set, None, 'Either the name of the company as recognised by TNT, or the \n                        contact name at the address')

    
    # Element addressLine1 uses Python identifier addressLine1
    __addressLine1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine1'), 'addressLine1', '__AbsentNamespace0_nameAndAddressResponseType_addressLine1', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 122, 12), )

    
    addressLine1 = property(__addressLine1.value, __addressLine1.set, None, 'This address line is the most commonly used of the three \n                        address lines and is therefore mandatory.')

    
    # Element addressLine2 uses Python identifier addressLine2
    __addressLine2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine2'), 'addressLine2', '__AbsentNamespace0_nameAndAddressResponseType_addressLine2', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 128, 12), )

    
    addressLine2 = property(__addressLine2.value, __addressLine2.set, None, 'This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address.')

    
    # Element addressLine3 uses Python identifier addressLine3
    __addressLine3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'addressLine3'), 'addressLine3', '__AbsentNamespace0_nameAndAddressResponseType_addressLine3', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 134, 12), )

    
    addressLine3 = property(__addressLine3.value, __addressLine3.set, None, 'This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address. \n                        NOTE - this will not appear on any routingLabel produced.')

    
    # Element town uses Python identifier town
    __town = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'town'), 'town', '__AbsentNamespace0_nameAndAddressResponseType_town', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 141, 12), )

    
    town = property(__town.value, __town.set, None, 'The town name as recognised by TNT')

    
    # Element province uses Python identifier province
    __province = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'province'), 'province', '__AbsentNamespace0_nameAndAddressResponseType_province', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 146, 12), )

    
    province = property(__province.value, __province.set, None, 'Optional field to contain the province, county, state, or area \n                        for the given address.')

    
    # Element postcode uses Python identifier postcode
    __postcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'postcode'), 'postcode', '__AbsentNamespace0_nameAndAddressResponseType_postcode', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 152, 12), )

    
    postcode = property(__postcode.value, __postcode.set, None, 'Postcode or zip code is considered a mandatory field where it is \n                        used in a given country. If the postcode is not provided, it may \n                        not be possible to deliver the consignment as indicated by your\n                        chosen service.')

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'country'), 'country', '__AbsentNamespace0_nameAndAddressResponseType_country', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 160, 12), )

    
    country = property(__country.value, __country.set, None, 'The ISO country code for the country of the given address.')

    _ElementMap.update({
        __name.name() : __name,
        __addressLine1.name() : __addressLine1,
        __addressLine2.name() : __addressLine2,
        __addressLine3.name() : __addressLine3,
        __town.name() : __town,
        __province.name() : __province,
        __postcode.name() : __postcode,
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'nameAndAddressResponseType', nameAndAddressResponseType)


# Complex type optionType with content type ELEMENT_ONLY
class optionType (pyxb.binding.basis.complexTypeDefinition):
    """The type of option chosen for this consignment. 
                Examples include insurance, priority."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'optionType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 168, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element optionId uses Python identifier optionId
    __optionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optionId'), 'optionId', '__AbsentNamespace0_optionType_optionId', True, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 174, 12), )

    
    optionId = property(__optionId.value, __optionId.set, None, 'Code that defines options for the consignment e.g. insurance, \n                        priority.')

    _ElementMap.update({
        __optionId.name() : __optionId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'optionType', optionType)


# Complex type measurementsType with content type ELEMENT_ONLY
class measurementsType (pyxb.binding.basis.complexTypeDefinition):
    """The dimensions (height, width, length) and weight of the consignment, 
                piece or article. Data must be provided in metres for dimensions, 
                kilograms for weight."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementsType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 183, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_measurementsType_length', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 190, 12), )

    
    length = property(__length.value, __length.set, None, 'The length in metres. The length is the longest dimension \n                        of the piece. (A piece is a box, envelope, or parcel - \n                        i.e. a separate item being shipped.)')

    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_measurementsType_width', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 197, 12), )

    
    width = property(__width.value, __width.set, None, 'The width in metres.')

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_measurementsType_height', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 202, 12), )

    
    height = property(__height.value, __height.set, None, 'The height in metres.')

    
    # Element weight uses Python identifier weight
    __weight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weight'), 'weight', '__AbsentNamespace0_measurementsType_weight', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 207, 12), )

    
    weight = property(__weight.value, __weight.set, None, 'The weight in kilograms.')

    _ElementMap.update({
        __length.name() : __length,
        __width.name() : __width,
        __height.name() : __height,
        __weight.name() : __weight
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'measurementsType', measurementsType)


# Complex type pieceLineType with content type ELEMENT_ONLY
class pieceLineType (pyxb.binding.basis.complexTypeDefinition):
    """A piece line describes a kind of piece sharing the same physical attributes. 
                (A piece is a package, box, envelope or shippable unit. All pieces which are 
                identical are defined for convenience as a piece line with a number of units.)

                For example if there are 5 boxes of 0.1m x 0.2m x 0.3m of weight 0.1kg and 
                1 box of 0.4m x 0.4m x 0.4 of weight 0.5kg this equates to two piece lines as 
                follows:

                PieceLine1: 0.1m x 0.2m x 0.3m, weight 0.1kg, number of units=5
                PieceLine2: 0.4m x 0.4m x 0.4m, weight 0.5kg, number of units=1"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pieceLineType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 215, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AbsentNamespace0_pieceLineType_identifier', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 229, 12), )

    
    identifier = property(__identifier.value, __identifier.set, None, 'Identifier for the pieceLine so that it can be referenced during \n                        processing.  Each pieceLine type should have a unique number, \n                        starting at 1 and incrementing for each piece line type required')

    
    # Element goodsDescription uses Python identifier goodsDescription
    __goodsDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'goodsDescription'), 'goodsDescription', '__AbsentNamespace0_pieceLineType_goodsDescription', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 236, 12), )

    
    goodsDescription = property(__goodsDescription.value, __goodsDescription.set, None, 'Full description of goods being shipped (catalogue numbers or \n                        part numbers will not suffice. The Customs Authorities want to \n                        know what each item actually is so please carefully describe the \n                        goods).')

    
    # Element barcodeForCustomer uses Python identifier barcodeForCustomer
    __barcodeForCustomer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'barcodeForCustomer'), 'barcodeForCustomer', '__AbsentNamespace0_pieceLineType_barcodeForCustomer', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 244, 12), )

    
    barcodeForCustomer = property(__barcodeForCustomer.value, __barcodeForCustomer.set, None, 'A flag to state if a barcode for the customer\n                        reference should be created.')

    
    # Element pieceMeasurements uses Python identifier pieceMeasurements
    __pieceMeasurements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pieceMeasurements'), 'pieceMeasurements', '__AbsentNamespace0_pieceLineType_pieceMeasurements', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 250, 12), )

    
    pieceMeasurements = property(__pieceMeasurements.value, __pieceMeasurements.set, None, 'Dimension and weight measurements relating to the pieces defined \n                        by this type.')

    
    # Element pieces uses Python identifier pieces
    __pieces = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pieces'), 'pieces', '__AbsentNamespace0_pieceLineType_pieces', True, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 256, 12), )

    
    pieces = property(__pieces.value, __pieces.set, None, 'At least one of these sections should be provided per consignment \n                        up to a maximum of one per piece.')

    _ElementMap.update({
        __identifier.name() : __identifier,
        __goodsDescription.name() : __goodsDescription,
        __barcodeForCustomer.name() : __barcodeForCustomer,
        __pieceMeasurements.name() : __pieceMeasurements,
        __pieces.name() : __pieces
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pieceLineType', pieceLineType)


# Complex type pieceType with content type ELEMENT_ONLY
class pieceType (pyxb.binding.basis.complexTypeDefinition):
    """This element is used to identify all the pieces that should be grouped 
                together by the given reference. The list of sequence numbers is included 
                (one sequenceNumber element per piece) with a single pieceReference element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pieceType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 265, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sequenceNumbers uses Python identifier sequenceNumbers
    __sequenceNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sequenceNumbers'), 'sequenceNumbers', '__AbsentNamespace0_pieceType_sequenceNumbers', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 272, 12), )

    
    sequenceNumbers = property(__sequenceNumbers.value, __sequenceNumbers.set, None, 'List of the piece sequence numbers, i.e. 1,2,5,n out of a total of \n                        n pieces that share the same piece reference.')

    
    # Element pieceReference uses Python identifier pieceReference
    __pieceReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pieceReference'), 'pieceReference', '__AbsentNamespace0_pieceType_pieceReference', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 278, 12), )

    
    pieceReference = property(__pieceReference.value, __pieceReference.set, None, 'Reference for this piece or pieces.')

    _ElementMap.update({
        __sequenceNumbers.name() : __sequenceNumbers,
        __pieceReference.name() : __pieceReference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pieceType', pieceType)


# Complex type contactType with content type ELEMENT_ONLY
class contactType (pyxb.binding.basis.complexTypeDefinition):
    """Information about the contact person at the relevant address."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contactType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 286, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_contactType_name', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 291, 12), )

    
    name = property(__name.value, __name.set, None, 'Name of the contact person at the relevant address.')

    
    # Element telephoneNumber uses Python identifier telephoneNumber
    __telephoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'telephoneNumber'), 'telephoneNumber', '__AbsentNamespace0_contactType_telephoneNumber', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 296, 12), )

    
    telephoneNumber = property(__telephoneNumber.value, __telephoneNumber.set, None, 'The full telephone number for the contact person.')

    
    # Element emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emailAddress'), 'emailAddress', '__AbsentNamespace0_contactType_emailAddress', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 301, 12), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, 'Email address for the contact person.')

    _ElementMap.update({
        __name.name() : __name,
        __telephoneNumber.name() : __telephoneNumber,
        __emailAddress.name() : __emailAddress
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'contactType', contactType)


# Complex type accountType with content type ELEMENT_ONLY
class accountType (pyxb.binding.basis.complexTypeDefinition):
    """Information about a TNT account which includes the account number 
                and country code."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 309, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element accountNumber uses Python identifier accountNumber
    __accountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accountNumber'), 'accountNumber', '__AbsentNamespace0_accountType_accountNumber', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 315, 12), )

    
    accountNumber = property(__accountNumber.value, __accountNumber.set, None, 'TNT legacy (global link) account number, which is the 9 digit \n                        number assigned by the TNT sales person.')

    
    # Element accountCountry uses Python identifier accountCountry
    __accountCountry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accountCountry'), 'accountCountry', '__AbsentNamespace0_accountType_accountCountry', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 321, 12), )

    
    accountCountry = property(__accountCountry.value, __accountCountry.set, None, 'ISO country code for the country the TNT account is in.')

    _ElementMap.update({
        __accountNumber.name() : __accountNumber,
        __accountCountry.name() : __accountCountry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'accountType', accountType)


# Complex type depotType with content type ELEMENT_ONLY
class depotType (pyxb.binding.basis.complexTypeDefinition):
    """Details relating to a TNT depot which could be the origin,
                destination or transit depot on the route calculated by TNT to deliver
                a consignment."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'depotType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 329, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element depotCode uses Python identifier depotCode
    __depotCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'depotCode'), 'depotCode', '__AbsentNamespace0_depotType_depotCode', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 336, 12), )

    
    depotCode = property(__depotCode.value, __depotCode.set, None, 'The three character TNT code for the depot.')

    _ElementMap.update({
        __depotCode.name() : __depotCode
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'depotType', depotType)


# Complex type marketType with content type ELEMENT_ONLY
class marketType (pyxb.binding.basis.complexTypeDefinition):
    """This identifies the market type for the consignment comprising the origin 
                country and whether the consignment is being shipped domestically or 
                internationally and within which international trading block, e.g. 'EU'."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'marketType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 344, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element originCountryCode uses Python identifier originCountryCode
    __originCountryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'originCountryCode'), 'originCountryCode', '__AbsentNamespace0_marketType_originCountryCode', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 351, 12), )

    
    originCountryCode = property(__originCountryCode.value, __originCountryCode.set, None, 'The ISO country code for the origin country of the consignment.')

    
    # Element marketSpecification uses Python identifier marketSpecification
    __marketSpecification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'marketSpecification'), 'marketSpecification', '__AbsentNamespace0_marketType_marketSpecification', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 356, 12), )

    
    marketSpecification = property(__marketSpecification.value, __marketSpecification.set, None, 'The market for the consignment - i.e. whether it is being shipped\n                        domestically or internationally, and, if the latter, in which trade\n                        block, e.g. EU, ROW, etc.')

    _ElementMap.update({
        __originCountryCode.name() : __originCountryCode,
        __marketSpecification.name() : __marketSpecification
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'marketType', marketType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """List of business rules that have been breached by the input and that will
                require the user to correct in order to print labels on resubmission of
                XML input file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 372, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element errorCode uses Python identifier errorCode
    __errorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'errorCode'), 'errorCode', '__AbsentNamespace0_CTD_ANON_errorCode', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 374, 16), )

    
    errorCode = property(__errorCode.value, __errorCode.set, None, 'Error code returned by the system to identify the error message.')

    
    # Element errorDescription uses Python identifier errorDescription
    __errorDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'errorDescription'), 'errorDescription', '__AbsentNamespace0_CTD_ANON_errorDescription', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 379, 16), )

    
    errorDescription = property(__errorDescription.value, __errorDescription.set, None, 'Error description returned by the system to signify the data\n                            that needs to be corrected in order to print labels.')

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__AbsentNamespace0_CTD_ANON_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 386, 12)
    __key._UseLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 386, 12)
    
    key = property(__key.value, __key.set, None, 'RequestId number to which the error relates.')

    _ElementMap.update({
        __errorCode.name() : __errorCode,
        __errorDescription.name() : __errorDescription
    })
    _AttributeMap.update({
        __key.name() : __key
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """List of faults that have occured during teh processign of multiple requests"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 397, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__AbsentNamespace0_CTD_ANON__key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 398, 12)
    __key._UseLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 398, 12)
    
    key = property(__key.value, __key.set, None, 'RequestId number to which the fault relates.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __key.name() : __key
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """The root XML element for a LabelRequest message
				sent to
				ExpressLabel in order to produce a routing label per piece.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element consignment uses Python identifier consignment
    __consignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'consignment'), 'consignment', '__AbsentNamespace0_CTD_ANON_2_consignment', True, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 19, 4), )

    
    consignment = property(__consignment.value, __consignment.set, None, 'Data for up to 5 consignments may be supplied\n\t\t\t\t\t\t\tin one request.')

    _ElementMap.update({
        __consignment.name() : __consignment
    })
    _AttributeMap.update({
        
    })



# Complex type labelConsignmentsType with content type ELEMENT_ONLY
class labelConsignmentsType (pyxb.binding.basis.complexTypeDefinition):
    """The view of the consignments information that is
				necessary for
				ExpressLabel to be able to validate addresses,
				determine the routing
				and product availability and successfully
				produce the information
				required to allow routing labels to be
				rendered per piece required.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'labelConsignmentsType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element consignmentIdentity uses Python identifier consignmentIdentity
    __consignmentIdentity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'consignmentIdentity'), 'consignmentIdentity', '__AbsentNamespace0_labelConsignmentsType_consignmentIdentity', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 43, 3), )

    
    consignmentIdentity = property(__consignmentIdentity.value, __consignmentIdentity.set, None, 'This element contains a consignment number and\n\t\t\t\t\t\toptional\n\t\t\t\t\t\tcustomer reference. These values are used to identify a\n\t\t\t\t\t\tconsignment from any other consignment.\n\n\t\t\t\t\t\tThis value appears on a\n\t\t\t\t\t\trouting label and is used as\n\t\t\t\t\t\tthe key for a consignment.\n\t\t\t\t\t')

    
    # Element collectionDateTime uses Python identifier collectionDateTime
    __collectionDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collectionDateTime'), 'collectionDateTime', '__AbsentNamespace0_labelConsignmentsType_collectionDateTime', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 57, 3), )

    
    collectionDateTime = property(__collectionDateTime.value, __collectionDateTime.set, None, "The date that the consignment will be collected,\n\t\t\t\t\t\tto be\n\t\t\t\t\t\tsupplied as CCYY-MM-DD'T'hh:mm:ss e.g 5:30 p.m. on\n\t\t\t\t\t\t30th\n\t\t\t\t\t\tDecember 2008 will be supplied as 2008-12-30T17:30:00.\n\t\t\t\t\t\tThis\n\t\t\t\t\t\tdatatype describes instances identified by the\n\t\t\t\t\t\tcombination of a\n\t\t\t\t\t\tdate and a time. Its value space is\n\t\t\t\t\t\tdescribed as a combination of\n\t\t\t\t\t\tdate and time of day in\n\t\t\t\t\t\tChapter 5.4 of ISO 8601 and the W3C XML\n\t\t\t\t\t\tSchema\n\t\t\t\t\t\tRecommendation . Its lexical space is the extended format:\n\t\t\t\t\t\t[-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]")

    
    # Element sender uses Python identifier sender
    __sender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sender'), 'sender', '__AbsentNamespace0_labelConsignmentsType_sender', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 77, 3), )

    
    sender = property(__sender.value, __sender.set, None, 'The origin is the address the consignment is\n\t\t\t\t\t\tphysically collected\n\t\t\t\t\t\tfrom. This will be used to obtain a route for\n\t\t\t\t\t\tthe consignment and\n\t\t\t\t\t\twill also appear on the label.\n\t\t\t\t\t')

    
    # Element delivery uses Python identifier delivery
    __delivery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'delivery'), 'delivery', '__AbsentNamespace0_labelConsignmentsType_delivery', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 88, 3), )

    
    delivery = property(__delivery.value, __delivery.set, None, 'The delivery is the address the consignment is\n\t\t\t\t\t\tphysically sent\n\t\t\t\t\t\tto. This will be used to obtain a route for the\n\t\t\t\t\t\tconsignment and\n\t\t\t\t\t\twill also appear on the label.')

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__AbsentNamespace0_labelConsignmentsType_contact', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 98, 3), )

    
    contact = property(__contact.value, __contact.set, None, 'This is the contact information for this\n\t\t\t\t\t\tdelivery consignment.\n\t\t\t\t\t\tThis information only appears on some labels\n\t\t\t\t\t\tbut is present in the xml\n\t\t\t\t\t\tresponse.\n                    ')

    
    # Element product uses Python identifier product
    __product = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'product'), 'product', '__AbsentNamespace0_labelConsignmentsType_product', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 109, 3), )

    
    product = property(__product.value, __product.set, None, 'Information relating to the TNT product chosen for this\n                        consignment. Example products are next day, before 10, etc.')

    
    # Element account uses Python identifier account
    __account = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'account'), 'account', '__AbsentNamespace0_labelConsignmentsType_account', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 115, 3), )

    
    account = property(__account.value, __account.set, None, 'The TNT account paying for this consignment to\n\t\t\t\t\t\tbe transported.')

    
    # Element cashAmount uses Python identifier cashAmount
    __cashAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cashAmount'), 'cashAmount', '__AbsentNamespace0_labelConsignmentsType_cashAmount', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 121, 3), )

    
    cashAmount = property(__cashAmount.value, __cashAmount.set, None, 'The cost of the consignment. This will only\n\t\t\t\t\t\tappear on some labels\n\t\t\t\t\t\tand only then if it is cash on delivery\n\t\t\t\t\t')

    
    # Element cashCurrency uses Python identifier cashCurrency
    __cashCurrency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cashCurrency'), 'cashCurrency', '__AbsentNamespace0_labelConsignmentsType_cashCurrency', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 130, 3), )

    
    cashCurrency = property(__cashCurrency.value, __cashCurrency.set, None, 'The currency of the cost of the consignment.\n\t\t\t\t\t\tThis is part of the 2D Barcode.')

    
    # Element cashType uses Python identifier cashType
    __cashType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cashType'), 'cashType', '__AbsentNamespace0_labelConsignmentsType_cashType', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 137, 3), )

    
    cashType = property(__cashType.value, __cashType.set, None, 'The cashType of the consignment. This is part of\n\t\t\t\t\t\tthe 2D Barcode.')

    
    # Element ncolNumber uses Python identifier ncolNumber
    __ncolNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ncolNumber'), 'ncolNumber', '__AbsentNamespace0_labelConsignmentsType_ncolNumber', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 144, 3), )

    
    ncolNumber = property(__ncolNumber.value, __ncolNumber.set, None, 'The ncol number. This is part of the 2D Barcode.\n\t\t\t\t\t')

    
    # Element specialInstructions uses Python identifier specialInstructions
    __specialInstructions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specialInstructions'), 'specialInstructions', '__AbsentNamespace0_labelConsignmentsType_specialInstructions', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 151, 3), )

    
    specialInstructions = property(__specialInstructions.value, __specialInstructions.set, None, 'Any special instructions required to appear on\n\t\t\t\t\t\tthe label.')

    
    # Element bulkShipment uses Python identifier bulkShipment
    __bulkShipment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bulkShipment'), 'bulkShipment', '__AbsentNamespace0_labelConsignmentsType_bulkShipment', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 158, 3), )

    
    bulkShipment = property(__bulkShipment.value, __bulkShipment.set, None, 'This is a flag to show if this is a bulk\n\t\t\t\t\t\tshipment or not')

    
    # Element customControlled uses Python identifier customControlled
    __customControlled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'customControlled'), 'customControlled', '__AbsentNamespace0_labelConsignmentsType_customControlled', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 165, 3), )

    
    customControlled = property(__customControlled.value, __customControlled.set, None, 'This is a flag to show if this is a custom\n\t\t\t\t\t\tcontrolled consignment or not')

    
    # Element termsOfPayment uses Python identifier termsOfPayment
    __termsOfPayment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'termsOfPayment'), 'termsOfPayment', '__AbsentNamespace0_labelConsignmentsType_termsOfPayment', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 172, 3), )

    
    termsOfPayment = property(__termsOfPayment.value, __termsOfPayment.set, None, 'This is a flag to show if this is a Sender pays\n\t\t\t\t\t\t(S) or Receiver pays (R) consignment')

    
    # Element totalNumberOfPieces uses Python identifier totalNumberOfPieces
    __totalNumberOfPieces = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'totalNumberOfPieces'), 'totalNumberOfPieces', '__AbsentNamespace0_labelConsignmentsType_totalNumberOfPieces', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 179, 3), )

    
    totalNumberOfPieces = property(__totalNumberOfPieces.value, __totalNumberOfPieces.set, None, 'The total number of pieces this consignment\n\t\t\t\t\t\tcontains. This\n\t\t\t\t\t\tis used to print the sequence numbers on the labels,\n\t\t\t\t\t\te.g.\n\t\t\t\t\t\t1 of x, where x is the value provided here.\n\t\t\t\t\t')

    
    # Element pieceLine uses Python identifier pieceLine
    __pieceLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pieceLine'), 'pieceLine', '__AbsentNamespace0_labelConsignmentsType_pieceLine', True, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 190, 3), )

    
    pieceLine = property(__pieceLine.value, __pieceLine.set, None, 'One pieceLine XML block to be provided per type\n\t\t\t\t\t\tof package in the\n\t\t\t\t\t\tconsignment. Each pieceLine defines the common\n\t\t\t\t\t\tattributes that\n\t\t\t\t\t\tone or more actual pieces share. For example, if\n\t\t\t\t\t\tgreen boxes and\n\t\t\t\t\t\tblue boxes are required to be shipped, then one\n\t\t\t\t\t\tpiece line per box\n\t\t\t\t\t\ttype needs to be provided, i.e one pieceLine for\n\t\t\t\t\t\tgreen box\n\t\t\t\t\t\tattributes\n\t\t\t\t\t\tand one for blue box attributes. At least one\n\t\t\t\t\t\tpieceLine per\n\t\t\t\t\t\tconsignment\n\t\t\t\t\t\tmust be provided. Individual pieces are\n\t\t\t\t\t\tdefined within the piece line.\n\t\t\t\t\t')

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__AbsentNamespace0_labelConsignmentsType_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 213, 2)
    __key._UseLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 213, 2)
    
    key = property(__key.value, __key.set, None, None)

    _ElementMap.update({
        __consignmentIdentity.name() : __consignmentIdentity,
        __collectionDateTime.name() : __collectionDateTime,
        __sender.name() : __sender,
        __delivery.name() : __delivery,
        __contact.name() : __contact,
        __product.name() : __product,
        __account.name() : __account,
        __cashAmount.name() : __cashAmount,
        __cashCurrency.name() : __cashCurrency,
        __cashType.name() : __cashType,
        __ncolNumber.name() : __ncolNumber,
        __specialInstructions.name() : __specialInstructions,
        __bulkShipment.name() : __bulkShipment,
        __customControlled.name() : __customControlled,
        __termsOfPayment.name() : __termsOfPayment,
        __totalNumberOfPieces.name() : __totalNumberOfPieces,
        __pieceLine.name() : __pieceLine
    })
    _AttributeMap.update({
        __key.name() : __key
    })
Namespace.addCategoryObject('typeBinding', 'labelConsignmentsType', labelConsignmentsType)


# Complex type productType with content type ELEMENT_ONLY
class productType (pyxb.binding.basis.complexTypeDefinition):
    """Information relating to the TNT product chosen for
				this consignment.
				Example products are next day, before 10, etc"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'productType')
    _XSDLocation = pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 215, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lineOfBusiness uses Python identifier lineOfBusiness
    __lineOfBusiness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lineOfBusiness'), 'lineOfBusiness', '__AbsentNamespace0_productType_lineOfBusiness', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 222, 3), )

    
    lineOfBusiness = property(__lineOfBusiness.value, __lineOfBusiness.set, None, None)

    
    # Element groupId uses Python identifier groupId
    __groupId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groupId'), 'groupId', '__AbsentNamespace0_productType_groupId', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 223, 3), )

    
    groupId = property(__groupId.value, __groupId.set, None, None)

    
    # Element subGroupId uses Python identifier subGroupId
    __subGroupId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subGroupId'), 'subGroupId', '__AbsentNamespace0_productType_subGroupId', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 224, 3), )

    
    subGroupId = property(__subGroupId.value, __subGroupId.set, None, None)

    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_productType_id', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 225, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_productType_type', False, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 226, 3), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'option'), 'option', '__AbsentNamespace0_productType_option', True, pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 227, 3), )

    
    option = property(__option.value, __option.set, None, None)

    _ElementMap.update({
        __lineOfBusiness.name() : __lineOfBusiness,
        __groupId.name() : __groupId,
        __subGroupId.name() : __subGroupId,
        __id.name() : __id,
        __type.name() : __type,
        __option.name() : __option
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'productType', productType)


brokenRules = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'brokenRules'), CTD_ANON, documentation='List of business rules that have been breached by the input and that will\n                require the user to correct in order to print labels on resubmission of\n                XML input file.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 366, 4))
Namespace.addCategoryObject('elementBinding', brokenRules.name().localName(), brokenRules)

fault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fault'), CTD_ANON_, documentation='List of faults that have occured during teh processign of multiple requests', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 393, 4))
Namespace.addCategoryObject('elementBinding', fault.name().localName(), fault)

labelRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labelRequest'), CTD_ANON_2, documentation='The root XML element for a LabelRequest message\n\t\t\t\tsent to\n\t\t\t\tExpressLabel in order to produce a routing label per piece.\n\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', labelRequest.name().localName(), labelRequest)



consignmentIdentityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'consignmentNumber'), pyxb.binding.datatypes.string, scope=consignmentIdentityType, documentation='The TNT consignment number in legacy (Global Link) format.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 15, 12)))

consignmentIdentityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'customerReference'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=consignmentIdentityType, documentation='Contains the optional customer reference for the consignment. \n                        A customer reference is a way for a customer to designate a name \n                        for the consignment.\n                        \n                        This value can be used to track the consignment at a later date.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 20, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(consignmentIdentityType._UseForTag(pyxb.namespace.ExpandedName(None, 'consignmentNumber')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(consignmentIdentityType._UseForTag(pyxb.namespace.ExpandedName(None, 'customerReference')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 20, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
consignmentIdentityType._Automaton = _BuildAutomaton()




nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), stringMaxLength40, scope=nameAndAddressRequestType, documentation='Either the name of the company as recognised by TNT, or the \n                        contact name at the address', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 45, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine1'), stringMaxLength30, scope=nameAndAddressRequestType, documentation='This address line is the most commonly used of the three \n                        address lines and is therefore mandatory.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 51, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine2'), stringMaxLength30, nillable=pyxb.binding.datatypes.boolean(1), scope=nameAndAddressRequestType, documentation='This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 57, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine3'), stringMaxLength30, nillable=pyxb.binding.datatypes.boolean(1), scope=nameAndAddressRequestType, documentation='This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address. \n                        NOTE - this will not appear on any routingLabel produced.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 63, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'town'), stringMaxLength40, scope=nameAndAddressRequestType, documentation='The town name as recognised by TNT', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 70, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'exactMatch'), booleanEnum, scope=nameAndAddressRequestType, documentation="Flag stating if an exact match on the town name should be used. \n                        If this flag is absent then the exact match value is 'Y'.", location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 75, 12), unicode_default='Y'))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'province'), stringMaxLength30, scope=nameAndAddressRequestType, documentation='Optional field to contain the province, county, state, or area \n                        for the given address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 81, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'postcode'), stringMaxLength9, scope=nameAndAddressRequestType, documentation='Postcode or zip code is considered a mandatory field where it is \n                        used in a given country. If the postcode is not provided, it may \n                        not be possible to deliver the consignment as indicated by your\n                        chosen service.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 87, 12)))

nameAndAddressRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'country'), stringMinLength2MaxLength2, scope=nameAndAddressRequestType, documentation='The ISO country code for the country of the given address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 95, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 57, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 63, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 70, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 75, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 81, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 87, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 45, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine1')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 51, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine2')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 57, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine3')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 63, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'town')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 70, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'exactMatch')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 75, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'province')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 81, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'postcode')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 87, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nameAndAddressRequestType._UseForTag(pyxb.namespace.ExpandedName(None, 'country')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 95, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nameAndAddressRequestType._Automaton = _BuildAutomaton_()




nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), stringMaxLength40, scope=nameAndAddressResponseType, documentation='Either the name of the company as recognised by TNT, or the \n                        contact name at the address', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 116, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine1'), stringMaxLength30, scope=nameAndAddressResponseType, documentation='This address line is the most commonly used of the three \n                        address lines and is therefore mandatory.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 122, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine2'), stringMaxLength30, nillable=pyxb.binding.datatypes.boolean(1), scope=nameAndAddressResponseType, documentation='This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 128, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'addressLine3'), stringMaxLength30, nillable=pyxb.binding.datatypes.boolean(1), scope=nameAndAddressResponseType, documentation='This address line may not be used by the supporting system \n                        and therefore should not contain information essential to the address. \n                        NOTE - this will not appear on any routingLabel produced.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 134, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'town'), stringMaxLength40, scope=nameAndAddressResponseType, documentation='The town name as recognised by TNT', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 141, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'province'), stringMaxLength30, scope=nameAndAddressResponseType, documentation='Optional field to contain the province, county, state, or area \n                        for the given address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 146, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'postcode'), stringMaxLength9, scope=nameAndAddressResponseType, documentation='Postcode or zip code is considered a mandatory field where it is \n                        used in a given country. If the postcode is not provided, it may \n                        not be possible to deliver the consignment as indicated by your\n                        chosen service.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 152, 12)))

nameAndAddressResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'country'), stringMinLength2MaxLength2, scope=nameAndAddressResponseType, documentation='The ISO country code for the country of the given address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 160, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 128, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 134, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 146, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 152, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 116, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine1')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 122, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine2')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 128, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'addressLine3')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 134, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'town')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 141, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'province')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 146, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'postcode')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 152, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nameAndAddressResponseType._UseForTag(pyxb.namespace.ExpandedName(None, 'country')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 160, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nameAndAddressResponseType._Automaton = _BuildAutomaton_2()




optionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optionId'), pyxb.binding.datatypes.string, scope=optionType, documentation='Code that defines options for the consignment e.g. insurance, \n                        priority.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 174, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=5, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 174, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(optionType._UseForTag(pyxb.namespace.ExpandedName(None, 'optionId')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 174, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
optionType._Automaton = _BuildAutomaton_3()




measurementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'length'), doubleMaxExclusive100MinInclusive0_01, scope=measurementsType, documentation='The length in metres. The length is the longest dimension \n                        of the piece. (A piece is a box, envelope, or parcel - \n                        i.e. a separate item being shipped.)', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 190, 12)))

measurementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), doubleMaxExclusive100MinInclusive0_01, scope=measurementsType, documentation='The width in metres.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 197, 12)))

measurementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), doubleMaxExclusive100MinInclusive0_01, scope=measurementsType, documentation='The height in metres.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 202, 12)))

measurementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weight'), doubleMaxExclusive100000MinInclusive0_01, scope=measurementsType, documentation='The weight in kilograms.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 207, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measurementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'length')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 190, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measurementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 197, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measurementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 202, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(measurementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'weight')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 207, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
measurementsType._Automaton = _BuildAutomaton_4()




pieceLineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.int, scope=pieceLineType, documentation='Identifier for the pieceLine so that it can be referenced during \n                        processing.  Each pieceLine type should have a unique number, \n                        starting at 1 and incrementing for each piece line type required', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 229, 12)))

pieceLineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'goodsDescription'), stringMaxLength30, scope=pieceLineType, documentation='Full description of goods being shipped (catalogue numbers or \n                        part numbers will not suffice. The Customs Authorities want to \n                        know what each item actually is so please carefully describe the \n                        goods).', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 236, 12)))

pieceLineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'barcodeForCustomer'), booleanEnum, scope=pieceLineType, documentation='A flag to state if a barcode for the customer\n                        reference should be created.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 244, 12)))

pieceLineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pieceMeasurements'), measurementsType, scope=pieceLineType, documentation='Dimension and weight measurements relating to the pieces defined \n                        by this type.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 250, 12)))

pieceLineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pieces'), pieceType, scope=pieceLineType, documentation='At least one of these sections should be provided per consignment \n                        up to a maximum of one per piece.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 256, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 244, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=1, max=99, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 256, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pieceLineType._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 229, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pieceLineType._UseForTag(pyxb.namespace.ExpandedName(None, 'goodsDescription')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 236, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pieceLineType._UseForTag(pyxb.namespace.ExpandedName(None, 'barcodeForCustomer')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 244, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pieceLineType._UseForTag(pyxb.namespace.ExpandedName(None, 'pieceMeasurements')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 250, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pieceLineType._UseForTag(pyxb.namespace.ExpandedName(None, 'pieces')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 256, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pieceLineType._Automaton = _BuildAutomaton_5()




pieceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sequenceNumbers'), pyxb.binding.datatypes.string, scope=pieceType, documentation='List of the piece sequence numbers, i.e. 1,2,5,n out of a total of \n                        n pieces that share the same piece reference.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 272, 12)))

pieceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pieceReference'), pyxb.binding.datatypes.string, scope=pieceType, documentation='Reference for this piece or pieces.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 278, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pieceType._UseForTag(pyxb.namespace.ExpandedName(None, 'sequenceNumbers')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 272, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pieceType._UseForTag(pyxb.namespace.ExpandedName(None, 'pieceReference')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 278, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pieceType._Automaton = _BuildAutomaton_6()




contactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), stringMaxLength30, scope=contactType, documentation='Name of the contact person at the relevant address.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 291, 12)))

contactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'telephoneNumber'), stringMaxLength30, scope=contactType, documentation='The full telephone number for the contact person.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 296, 12)))

contactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emailAddress'), pyxb.binding.datatypes.string, scope=contactType, documentation='Email address for the contact person.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 301, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 291, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 296, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 301, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(contactType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 291, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(contactType._UseForTag(pyxb.namespace.ExpandedName(None, 'telephoneNumber')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 296, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(contactType._UseForTag(pyxb.namespace.ExpandedName(None, 'emailAddress')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 301, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
contactType._Automaton = _BuildAutomaton_7()




accountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accountNumber'), stringMaxLength10, scope=accountType, documentation='TNT legacy (global link) account number, which is the 9 digit \n                        number assigned by the TNT sales person.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 315, 12)))

accountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accountCountry'), stringMinLength2MaxLength2, scope=accountType, documentation='ISO country code for the country the TNT account is in.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 321, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(accountType._UseForTag(pyxb.namespace.ExpandedName(None, 'accountNumber')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 315, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(accountType._UseForTag(pyxb.namespace.ExpandedName(None, 'accountCountry')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 321, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
accountType._Automaton = _BuildAutomaton_8()




depotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'depotCode'), stringMinLength3MaxLength3, scope=depotType, documentation='The three character TNT code for the depot.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 336, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(depotType._UseForTag(pyxb.namespace.ExpandedName(None, 'depotCode')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 336, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
depotType._Automaton = _BuildAutomaton_9()




marketType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'originCountryCode'), stringMinLength2MaxLength2, scope=marketType, documentation='The ISO country code for the origin country of the consignment.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 351, 12)))

marketType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'marketSpecification'), pyxb.binding.datatypes.string, scope=marketType, documentation='The market for the consignment - i.e. whether it is being shipped\n                        domestically or internationally, and, if the latter, in which trade\n                        block, e.g. EU, ROW, etc.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 356, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(marketType._UseForTag(pyxb.namespace.ExpandedName(None, 'originCountryCode')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 351, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(marketType._UseForTag(pyxb.namespace.ExpandedName(None, 'marketSpecification')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 356, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
marketType._Automaton = _BuildAutomaton_10()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'errorCode'), pyxb.binding.datatypes.int, scope=CTD_ANON, documentation='Error code returned by the system to identify the error message.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 374, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'errorDescription'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Error description returned by the system to signify the data\n                            that needs to be corrected in order to print labels.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 379, 16)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'errorCode')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 374, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'errorDescription')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/commonDefinitions.xsd', 379, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_11()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'consignment'), labelConsignmentsType, scope=CTD_ANON_2, documentation='Data for up to 5 consignments may be supplied\n\t\t\t\t\t\t\tin one request.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 19, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=5, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 19, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'consignment')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 19, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_12()




labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'consignmentIdentity'), consignmentIdentityType, scope=labelConsignmentsType, documentation='This element contains a consignment number and\n\t\t\t\t\t\toptional\n\t\t\t\t\t\tcustomer reference. These values are used to identify a\n\t\t\t\t\t\tconsignment from any other consignment.\n\n\t\t\t\t\t\tThis value appears on a\n\t\t\t\t\t\trouting label and is used as\n\t\t\t\t\t\tthe key for a consignment.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 43, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collectionDateTime'), pyxb.binding.datatypes.dateTime, scope=labelConsignmentsType, documentation="The date that the consignment will be collected,\n\t\t\t\t\t\tto be\n\t\t\t\t\t\tsupplied as CCYY-MM-DD'T'hh:mm:ss e.g 5:30 p.m. on\n\t\t\t\t\t\t30th\n\t\t\t\t\t\tDecember 2008 will be supplied as 2008-12-30T17:30:00.\n\t\t\t\t\t\tThis\n\t\t\t\t\t\tdatatype describes instances identified by the\n\t\t\t\t\t\tcombination of a\n\t\t\t\t\t\tdate and a time. Its value space is\n\t\t\t\t\t\tdescribed as a combination of\n\t\t\t\t\t\tdate and time of day in\n\t\t\t\t\t\tChapter 5.4 of ISO 8601 and the W3C XML\n\t\t\t\t\t\tSchema\n\t\t\t\t\t\tRecommendation . Its lexical space is the extended format:\n\t\t\t\t\t\t[-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]", location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 57, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sender'), nameAndAddressRequestType, scope=labelConsignmentsType, documentation='The origin is the address the consignment is\n\t\t\t\t\t\tphysically collected\n\t\t\t\t\t\tfrom. This will be used to obtain a route for\n\t\t\t\t\t\tthe consignment and\n\t\t\t\t\t\twill also appear on the label.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 77, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'delivery'), nameAndAddressRequestType, scope=labelConsignmentsType, documentation='The delivery is the address the consignment is\n\t\t\t\t\t\tphysically sent\n\t\t\t\t\t\tto. This will be used to obtain a route for the\n\t\t\t\t\t\tconsignment and\n\t\t\t\t\t\twill also appear on the label.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 88, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), contactType, scope=labelConsignmentsType, documentation='This is the contact information for this\n\t\t\t\t\t\tdelivery consignment.\n\t\t\t\t\t\tThis information only appears on some labels\n\t\t\t\t\t\tbut is present in the xml\n\t\t\t\t\t\tresponse.\n                    ', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 98, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'product'), productType, scope=labelConsignmentsType, documentation='Information relating to the TNT product chosen for this\n                        consignment. Example products are next day, before 10, etc.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 109, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'account'), accountType, scope=labelConsignmentsType, documentation='The TNT account paying for this consignment to\n\t\t\t\t\t\tbe transported.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 115, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cashAmount'), doubleTwoDecimalPlaces, scope=labelConsignmentsType, documentation='The cost of the consignment. This will only\n\t\t\t\t\t\tappear on some labels\n\t\t\t\t\t\tand only then if it is cash on delivery\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 121, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cashCurrency'), pyxb.binding.datatypes.string, scope=labelConsignmentsType, documentation='The currency of the cost of the consignment.\n\t\t\t\t\t\tThis is part of the 2D Barcode.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 130, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cashType'), cashTypeEnum, scope=labelConsignmentsType, documentation='The cashType of the consignment. This is part of\n\t\t\t\t\t\tthe 2D Barcode.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 137, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ncolNumber'), pyxb.binding.datatypes.string, scope=labelConsignmentsType, documentation='The ncol number. This is part of the 2D Barcode.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 144, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specialInstructions'), pyxb.binding.datatypes.string, scope=labelConsignmentsType, documentation='Any special instructions required to appear on\n\t\t\t\t\t\tthe label.', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 151, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bulkShipment'), booleanEnum, scope=labelConsignmentsType, documentation='This is a flag to show if this is a bulk\n\t\t\t\t\t\tshipment or not', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 158, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'customControlled'), booleanEnum, scope=labelConsignmentsType, documentation='This is a flag to show if this is a custom\n\t\t\t\t\t\tcontrolled consignment or not', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 165, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'termsOfPayment'), senderReceiverEnum, scope=labelConsignmentsType, documentation='This is a flag to show if this is a Sender pays\n\t\t\t\t\t\t(S) or Receiver pays (R) consignment', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 172, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'totalNumberOfPieces'), pyxb.binding.datatypes.int, scope=labelConsignmentsType, documentation='The total number of pieces this consignment\n\t\t\t\t\t\tcontains. This\n\t\t\t\t\t\tis used to print the sequence numbers on the labels,\n\t\t\t\t\t\te.g.\n\t\t\t\t\t\t1 of x, where x is the value provided here.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 179, 3)))

labelConsignmentsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pieceLine'), pieceLineType, scope=labelConsignmentsType, documentation='One pieceLine XML block to be provided per type\n\t\t\t\t\t\tof package in the\n\t\t\t\t\t\tconsignment. Each pieceLine defines the common\n\t\t\t\t\t\tattributes that\n\t\t\t\t\t\tone or more actual pieces share. For example, if\n\t\t\t\t\t\tgreen boxes and\n\t\t\t\t\t\tblue boxes are required to be shipped, then one\n\t\t\t\t\t\tpiece line per box\n\t\t\t\t\t\ttype needs to be provided, i.e one pieceLine for\n\t\t\t\t\t\tgreen box\n\t\t\t\t\t\tattributes\n\t\t\t\t\t\tand one for blue box attributes. At least one\n\t\t\t\t\t\tpieceLine per\n\t\t\t\t\t\tconsignment\n\t\t\t\t\t\tmust be provided. Individual pieces are\n\t\t\t\t\t\tdefined within the piece line.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 190, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 98, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 121, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 130, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 137, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 144, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 151, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 158, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 165, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 172, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=1, max=99, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 190, 3))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'consignmentIdentity')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 43, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'collectionDateTime')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 57, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'sender')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 77, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'delivery')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 88, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 98, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'product')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 109, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'account')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 115, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'cashAmount')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 121, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'cashCurrency')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 130, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'cashType')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 137, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'ncolNumber')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 144, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'specialInstructions')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 151, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'bulkShipment')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 158, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'customControlled')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 165, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'termsOfPayment')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 172, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'totalNumberOfPieces')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 179, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(labelConsignmentsType._UseForTag(pyxb.namespace.ExpandedName(None, 'pieceLine')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 190, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
labelConsignmentsType._Automaton = _BuildAutomaton_13()




productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lineOfBusiness'), integerMin0Max9, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 222, 3)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groupId'), integerMin0Max9, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 223, 3)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subGroupId'), integerMin0Max9, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 224, 3)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), stringMaxLength4, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 225, 3)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), productTypeEnum, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 226, 3)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'option'), stringMaxLength4, scope=productType, location=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 227, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=5, metadata=pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 227, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'lineOfBusiness')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 222, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'groupId')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 223, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'subGroupId')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 224, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 225, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 226, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'option')), pyxb.utils.utility.Location('https://express.tnt.com/expresswebservices-website/xsd/routing/labelRequest.xsd', 227, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
productType._Automaton = _BuildAutomaton_14()

