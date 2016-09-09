import xml.etree.ElementTree  as Et
from registerDef import *
def getValueGroupDict(node,path):
    valueGroups = {}
    for valueGroupnode in node.findall(path):
        values = []
        for valueNode in valueGroupnode.findall("./value"):
            values.append(valueNode.attrib)
        valueGroups[valueGroupnode.attrib['name']] = values
    return valueGroups

registersDict = {}

if __name__ == '__main__':
    xmltree = Et.parse('sample.xml')
    root =  xmltree.getroot()
    #fuse Module
    valueGroupDict = getValueGroupDict(root, "./modules/module/[@name='FUSE']//value-group")
    
    fuseRegisters_node =   root.findall("./modules/module/[@name='FUSE']//register")
    
    for registerNode in fuseRegisters_node:
        reg = register(registerNode.attrib)
        bitFields = []
        for bitfieldNode in registerNode.findall('./bitfield'):
            attr = bitfieldNode.attrib
            if attr.has_key('values') and valueGroupDict.has_key(attr['values']):
                bf = bitfeild(reg, attr, valueGroupDict[attr['values']])
            else:
                bf = bitfeild(reg,attr)
            bitFields.append(bf)
print GlobalregisterDict