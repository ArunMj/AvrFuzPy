
class bitfeild:
    def __init__(self, parrentRegister, attrib, fields = []):
        self.parrentRegister = parrentRegister
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.mask = attrib['mask']

        '''Empty values list indicate single bit'''
        self.values = fields

        # updating parent register
        parrentRegister.bitfields[self.name] = self

class avrRegister:

    '''pass register node  attribute dict in the
     form {'caption': '', 'offset': '0x00', 'name': 'LOW', 'size': '1'}'''
    def __init__(self,attrib):
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.offset = attrib['offset']
        self.size = attrib['size']

        self.bitfields = {}

        GlobalregisterDict[self.name] = self

'''tracker of all registers initialised '''
GlobalregisterDict = {}

    
