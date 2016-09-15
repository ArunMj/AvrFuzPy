'''
    contains Bitfeild and register class definitions
'''
class Bitfeild:
    
    def __init__(self, parrentRegister, attrib, values = None):
        self.parrentRegister = parrentRegister
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.mask = attrib['mask']

        '''Empty/None values list indicate single bit'''
        self.values = values

        # updating parent register
        parrentRegister.bitfields[self.name] = self

class AvrRegister:

    '''tracker of all registers initialised '''
    GlobalregisterDict = {}

    '''pass register node  attribute dict in the
     form {'caption': '', 'offset': '0x00', 'name': 'LOW', 'size': '1'}'''
    def __init__(self,attrib):
        self.name = attrib['name']
        self.caption = attrib['caption']
        self.offset = attrib['offset']
        self.size = attrib['size']

        self.bitfields = {}
        
        AvrRegister.GlobalregisterDict[self.name] = self