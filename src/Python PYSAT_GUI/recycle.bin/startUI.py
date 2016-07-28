from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
from mainwindow import Ui_MainWindow


class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()