
class flag:
    def __init__(self,name,pos,parentFuse,defaultValue = None):
        self.pos = 0
        self.name = name
        self.parrentRegister = parentRegister
        self.defaultValue = defaultValue

class Fuse():

    def __init__(self,avrFusereg):
         bits = ()
         self.defaultValue = 0
         self._value = 0

        for _,bitfield in avrFusereg.bitfields:
            if bitfield.isSingleBit:
                flag(bitfield.name,self,bitField.mask)



            



    def reset(self):
         #self.setvalue(self,self.defaultValue)
         self.value =  self.defaultValue

    @property
    def value(self):
        return self._value

    @value.setter
    def setvalue(self,value):
         self._value = value
    




if __name__ == '__main__':
    import avrXMLparser
    avrXMLparser.parseAndUpdate()
    import DeviceInfo



    l = DeviceInfo.fuseRegisters['LOW']
    print l
    f = Fuse(None)
    print f.value

    f.value = 1
    f.reset()
    print f.value