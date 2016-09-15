import avrXMLparser
from qtpy.QtWidgets import (QWidget,QLabel, QVBoxLayout,QComboBox,QApplication, QCheckBox)

fuseRegisterDict = avrXMLparser.enumerateFuseregister('sample.xml')


class QtRegisterView():
    def __init__(self):
        pass
        

fuseReg = fuseRegisterDict['LOW']
print fuseReg


'''TESTING UI '''
if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)

    qtBitfieldViewList = []
    for _,bitfield in fuseReg.bitfields.items():
        print _,bitfield.isSingleBit()
        if bitfield.isSingleBit():
            checkBox = QCheckBox(bitfield.caption)
            qtBitfieldViewList.append(checkBox)
        else:
            comboBox = QComboBox()
            comboBox.name = bitfield.name
            comboBox.addItems([ x['caption'] for x in bitfield.values])
            qtBitfieldViewList.append(comboBox)




    w = QWidget()   
    w.setGeometry(500,500,100,150)
    w.setWindowTitle("testing UI")
    w.show()
    vbox = QVBoxLayout(w)
    for i in qtBitfieldViewList:
        vbox.addWidget(i)
        i.show()
        print i
    w.setLayout(vbox)
    sys.exit(app.exec_())