from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from mainwindow_compranges import CompRanges
from mainwindow_createmodels import CreateModels

class main(QMainWindow, CompRanges):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()