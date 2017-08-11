import sys

from PyQt5 import QtWidgets

from point_spectra_gui.future_.util import *
from point_spectra_gui.ui import MainWindow

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = MainWindow.Ui_MainWindow()
mainW.setupUi(mw)



def addWidget(object):
    widget = object.Ui_Form()
    widget.setupUi(mainW.scrollArea)
    mainW.widgetLayout.addWidget(widget.get_widget())


addWidget(ARD)
addWidget(BaselineRemoval)
addWidget(BayesianRidge)
addWidget(CrossValidation)
addWidget(DimenstionalityReduction)
addWidget(ElasticNet)
addWidget(GP)
addWidget(Interpolation)
addWidget(KRR)
addWidget(LARS)
addWidget(Lasso)
addWidget(LassoLARS)
addWidget(LoadData)
addWidget(MaskData)
addWidget(MultiplyByVector)
addWidget(Normalization)
addWidget(OLS)
addWidget(OMP)
addWidget(OutputFolder)
addWidget(PeakAreas)
addWidget(Plot)
addWidget(Plot_ICA_PCA)
addWidget(PlotSpectra)
addWidget(PLS)
addWidget(ReadChemCamData)
addWidget(RegressionPredict)
addWidget(RegressionTrain)
addWidget(RemoveRows)
addWidget(Ridge)
addWidget(SplitDataset)
addWidget(StratifiedFolds)
addWidget(SubmodelPredict)
addWidget(SVR)

mw.show()
sys.exit(app.exec_())
