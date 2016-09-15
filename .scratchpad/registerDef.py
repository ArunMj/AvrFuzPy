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


    def __str__(self):
        strpat = 'invalid'
        if not self.values:
        # bitfield is a single bitfield
            strpat =  '| {}\t[{}]\t{}\n'.format(self.name,'x',self.caption)
        else:
        #  is a group of valuse'
            strpat = '| {}\t{}\n'.format(self.name,self.caption)
            for value in self.values:
                strpat += '|\t\t > {}\t{}\t[{}]\n'.format(value['name'],value['caption'],value['value'])
        return strpat + '| ' + '-' * 70 + '\n'

    def isSingleBit(self):
        return self.values == None

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

    def __str__(self):
        strVal = '{} {}\t{} {} \n'.format('='*50 ,self.name,self.caption,'='*50)
        for _,bitfield in self.bitfields.items():
            strVal += str(bitfield).replace('|','\t|')
        return strVal + '_'*100 + '\n'

