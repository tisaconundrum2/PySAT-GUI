import sys

from PyQt5 import QtWidgets

from point_spectra_gui.future_.ui import *

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = MainWindow.Ui_MainWindow()
mainW.setupUi(mw)

regression_train = RegressionTrain.RegressionTrain()
regression_train.setupUi(mainW.centralwidget)
mainW.widgetLayout.addWidget(regression_train.get_widget())

dim_red = DimenstionalityReduction.DimenstionalityReduction()
dim_red.setupUi(mainW.centralwidget)
mainW.widgetLayout.addWidget(dim_red.get_widget())



mw.show()
sys.exit(app.exec_())