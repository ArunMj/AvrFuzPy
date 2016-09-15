"""
    parses avr xml file and generate a dictionary
"""


import xml.etree.ElementTree  as Et
from registerDef import *

'''returns value-group as dictionary from given path glob
    format {groupname: [{caption:,name:,value:},,,]}'''
def getValueGroupDict(node,path):
    valueGroups = {}
    for valueGroupnode in node.findall(path):
        values = []
        for valueNode in valueGroupnode.findall("./value"):
            values.append(valueNode.attrib)
            # attrib is in format {'caption': 'Brown-out', 'name': '4V3', 'value': '0x04'}
        valueGroups[valueGroupnode.attrib['name']] = values
    # print valueGroups
    return valueGroups

#--------------------------------------------------------------------------
#  enumerating Fuse Register

''' returns list of fuse register decribed in xml file'''
def enumerateFuseregister(xmlFilePath):

    xmltree = Et.parse(xmlFilePath)
    root =  xmltree.getroot()

    fuseRegisterList = {}

    # fuse Module
    valueGroupDict = getValueGroupDict(root, "./modules/module/[@name='FUSE']//value-group")

    # fuse register nodes in xml file
    fuseRegisters_nodes =   root.findall("./modules/module/[@name='FUSE']//register")

    for registerNode in fuseRegisters_nodes:
        # print registerNode.attrib
        newFuseRegister = AvrRegister(registerNode.attrib)

        bitFieldList = []
        for bitfieldNode in registerNode.findall('./bitfield'):
            bitFieldAttrib = bitfieldNode.attrib
            if bitFieldAttrib.has_key('values') and valueGroupDict.has_key(bitFieldAttrib['values']):
                # bitfield is a group value
                bitFieldList.append(Bitfeild(newFuseRegister, bitFieldAttrib, valueGroupDict[bitFieldAttrib['values']]))
            else:
                # bitfield is single bit
                bitFieldList.append(Bitfeild(newFuseRegister,bitFieldAttrib))
        
        fuseRegisterList[newFuseRegister.name] = newFuseRegister

    return fuseRegisterList

#-----------------------------------------------------------------------------