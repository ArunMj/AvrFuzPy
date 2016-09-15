from avrXMLparser import enumerateFuseregister


fuseRegisterDict = enumerateFuseregister('sample.xml')
#print fuseRegisterDict

# print fuseRegisterDict['LOW']

# for fusereg in fuseRegisterList:
#     print fusereg.name,fusereg.bitfields
#     break

for _,i in fuseRegisterDict['LOW'].bitfields.items():
   # print i,fuseRegisterDict['LOW'].bitfields[i].mask
   print i  
   pass