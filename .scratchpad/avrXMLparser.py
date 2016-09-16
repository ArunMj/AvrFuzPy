"""
    parses avr xml file and generate a dictionary
"""

import xml.etree.ElementTree  as Et
from RegisterDef import AvrRegister,Bitfeild
import DeviceInfo 



'''returns value-group as dictionary from given path glob
    format {groupname: [{caption:,name:,value:},,,]}'''
def _getValueGroupAsDict(node,path):
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

''' generate list of fuse registers decribed in xml file
    it will update DeviceInfo.fuseRegisters tuple
'''
def _getFuseregisters():

    xmltree = Et.parse(DeviceInfo.xmlFilePath)
    root =  xmltree.getroot()

    fuseRegisterList = {}

    # fuse Module
    valueGroupDict = _getValueGroupAsDict(root, "./modules/module/[@name='FUSE']//value-group")

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

        DeviceInfo.fuseRegisters = fuseRegisterList



def parseAndUpdate():
    _getFuseregisters()
    for fusereg in DeviceInfo.fuseRegisters:
        pass

#-----------------------------------------------------------------------------