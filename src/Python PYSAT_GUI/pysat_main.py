from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from mainwindow_compranges import CompRanges
from mainwindow_createmodels import CreateModels
from mainwindow_files import Files
from mainwindow_normalization import Normalization
from mainwindow_setup import  SetUp

class main(QMainWindow, CreateModels):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()