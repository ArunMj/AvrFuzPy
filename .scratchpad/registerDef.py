GlobalregisterDict = {}
class bitfeild:
    def __init__(self, parrentRegister, attrib, fields = []):
        self.parrentRegister = parrentRegister
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.mask = attrib['mask']
        '''Empy field means single bit'''
        self.fields = fields

        parrentRegister.fields[self.name] = self

class register:
    def __init__(self,attrib):
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.offset = attrib['offset']
        self.size = attrib['size']
        self.fields = {}

        GlobalregisterDict[self.name] = self



    
