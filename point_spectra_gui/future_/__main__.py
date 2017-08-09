import sys

from PyQt5 import QtWidgets

from point_spectra_gui.future_.ui import MainWindow, UI_RegressionTrain, RegressionTrain

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = MainWindow.Ui_MainWindow()
mainW.setupUi(mw)

widget1 = RegressionTrain.RegressionTrain()
widget1.setupUi(mainW.centralwidget)
mainW.widgetLayout.addWidget(widget1.get_widget())



mw.show()
sys.exit(app.exec_())