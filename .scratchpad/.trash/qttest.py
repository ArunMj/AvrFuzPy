import sys,time
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QComboBox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    
    w.setGeometry(500,500,700,750)
    b.move(550,520)
    w.setWindowTitle("PyQt")
    w.show()
    ql = QComboBox(w)
    ql.addItem("sdada")
    ql.addItem("sdada")
    ql.addItem("sdada")
    ql.show()
    sys.exit(app.exec_())


    sys.exit(app.exec_())