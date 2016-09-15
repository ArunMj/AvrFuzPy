import avrXMLparser
from qtpy.QtWidgets import (QWidget,QLabel, QVBoxLayout,QComboBox,QApplication)

fuseRegisterDict = avrXMLparser.enumerateFuseregister('sample.xml')


class QtRegisterView():
    def __init__(self):
        


for register in fuseRegisterDict:




'''TESTING UI '''
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)


    w = QWidget()

    b = QLabel(w)
    b.setText("Hello World!")
    
    w.setGeometry(500,500,100,150)
    b.move(550,520)
    w.setWindowTitle("testing UI")
    w.show()
    ql = QComboBox(w)
    ql.addItems(["sdada",'sadasd','dasdas'])
    ql.show()
    sys.exit(app.exec_())