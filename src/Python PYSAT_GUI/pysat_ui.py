from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import sys
from pysat_function import pysat_func
from functools import partial
from PyQt4.QtGui import QMessageBox
from PythonUI.mainframe_ import mainframe_
from PythonUI.file_out_ import file_outpath_
from PythonUI.get_data_ import *
from PythonUI.regression_ import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class pysat_ui(object):
    def __init__(self):
        self.pysat_fun = pysat_func()
        self.addFunc = []
        self.addPara = []

    def mainframe(self, MainWindow):
        mainframe_.mainframe(self, MainWindow)

    def file_outpath(self, MainWindow):
        file_outpath_.file_outpath(self, MainWindow)

    def get_unknown_data(self, MainWindow):
        get_data_.get_data_u(self, MainWindow)

    def get_known_data(self, MainWindow):
        get_data_.get_data_u(self, MainWindow)

    def do_mask(self, MainWindow):
        pass

    def submodel_ranges(self, MainWindow):
        pass

    def do_strat_folds(self, MainWindow):
        pass

    def do_regression_train(self, MainWindow):
        regression_.regression_train(self, MainWindow)

    def do_scatter_plot(self, MainWindow):
        pass