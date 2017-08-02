import sys
from PyQt5 import QtWidgets
from point_spectra_gui.future_ import *

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = MainWindow.Ui_MainWindow()
mainW.setupUi(mw)

widget1 = RegressionTrain.Ui_Form()
widget1.setupUi(mainW.scrollArea)
# widget2 = RegressionPredict.Ui_Form()
# widget2.setupUi(mainW.scrollArea)



mw.show()
sys.exit(app.exec_())