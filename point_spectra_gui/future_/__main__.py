import sys

from PyQt5 import QtWidgets

from point_spectra_gui.future_.util import *
from point_spectra_gui.ui import MainWindow


class Ui_MainWindow(MainWindow.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

    def addWidget(self, object):
        widget = object.Ui_Form()
        widget.setupUi(self.scrollArea)
        self.verticalLayout_3.addWidget(widget.get_widget())


app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
mainW = Ui_MainWindow()
mainW.setupUi(mw)

mainW.addWidget(ARD)
mainW.addWidget(BaselineRemoval)
mainW.addWidget(BayesianRidge)
mainW.addWidget(CrossValidation)
mainW.addWidget(DimenstionalityReduction)
mainW.addWidget(ElasticNet)
mainW.addWidget(GP)
mainW.addWidget(Interpolation)
mainW.addWidget(KRR)
mainW.addWidget(LARS)
mainW.addWidget(Lasso)
mainW.addWidget(LassoLARS)
mainW.addWidget(LoadData)
mainW.addWidget(MaskData)
mainW.addWidget(MultiplyByVector)
mainW.addWidget(Normalization)
mainW.addWidget(OLS)
mainW.addWidget(OMP)
mainW.addWidget(OutputFolder)
mainW.addWidget(PeakAreas)
mainW.addWidget(Plot)
mainW.addWidget(Plot_ICA_PCA)
mainW.addWidget(PlotSpectra)
mainW.addWidget(PLS)
mainW.addWidget(ReadChemCamData)
mainW.addWidget(RegressionPredict)
mainW.addWidget(RegressionTrain)
mainW.addWidget(RemoveRows)
mainW.addWidget(Ridge)
mainW.addWidget(SplitDataset)
mainW.addWidget(StratifiedFolds)
mainW.addWidget(SubmodelPredict)
mainW.addWidget(SVR)

mw.show()
sys.exit(app.exec_())
