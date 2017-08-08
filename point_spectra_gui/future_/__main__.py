import sys
from PyQt5 import QtWidgets
from point_spectra_gui.future_ import *

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.form = MainWindow.Ui_MainWindow()
        self.setCentralWidget(self.form)

