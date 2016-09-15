import sys
from qtpy.QtCore import Qt
from qtpy.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lambda x:lcd.display(2**x))
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())