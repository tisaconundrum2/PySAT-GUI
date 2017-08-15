import sys

from PyQt5 import QtWidgets

from point_spectra_gui.future_.functions import *

sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook
app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = MainWindow.Ui_MainWindow()
mainW.setupUi(mw)

mw.show()
sys.exit(app.exec_())
