from avrXMLparser import enumerateFuseregister


fuseRegisterDict = enumerateFuseregister('sample.xml')
print fuseRegisterDict


# for fusereg in fuseRegisterList:
#     print fusereg.name,fusereg.bitfields
#     break

for i in fuseRegisterDict['LOW'].bitfields:
    print i,fuseRegisterDict['LOW'].bitfields[i].mask
