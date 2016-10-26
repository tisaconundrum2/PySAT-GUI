from PyQt4 import QtCore
import PythonUI



class pysat_ui(object):
    def __init__(self):

    def mainframe(self, MainWindow):
        PythonUI.mainframe_.mainframe(self, MainWindow)

    def file_outpath(self, MainWindow):
        PythonUI.file_outpath_.file_outpath(self, MainWindow)

    def get_unknown_data(self, MainWindow):
        PythonUI.get_data_.get_data_u(self, MainWindow)

    def get_known_data(self, MainWindow):
        PythonUI.get_data_.get_data_k(self, MainWindow)

    def do_mask(self, MainWindow):
        pass

    def submodel_ranges(self, MainWindow):
        PythonUI.submodel_.submodel(self, MainWindow)


    def do_strat_folds(self, MainWindow):


    def do_regression_train(self, MainWindow):
        PythonUI.regression_.regression_train(self, MainWindow)

    def do_scatter_plot(self, MainWindow):
        pass