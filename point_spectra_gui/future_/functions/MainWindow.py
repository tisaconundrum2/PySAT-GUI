import sys
from PyQt5 import QtWidgets

from point_spectra_gui.future_.__main__ import new
from point_spectra_gui.future_.functions import *
from point_spectra_gui.ui import MainWindow


class Ui_MainWindow(MainWindow.Ui_MainWindow):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        super().setupUi(MainWindow)  # Run the basic window UI
        self.menu_item_shortcuts()  # set up the shortcuts
        self.menuItemFunctions()

    def addWidget(self, object):
        widget = object.Ui_Form()
        widget.setupUi(self.scrollArea)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(widget.get_widget())

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionRestore_Workflow.setShortcut("ctrl+R")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")

    def menuItemFunctions(self):
        self.actionRead_ChemCam_Data.triggered.connect(lambda: self.addWidget(ReadChemCamData))
        self.actionRemove_Baseline.triggered.connect(lambda: self.addWidget(BaselineRemoval))
        self.actionCross_Validation.triggered.connect(lambda: self.addWidget(CrossValidation))
        self.actionDimensionality_Reduction.triggered.connect(lambda: self.addWidget(DimensionalityReduction))
        self.actionInterpolate.triggered.connect(lambda: self.addWidget(Interpolation))
        self.actionLoad_Data.triggered.connect(lambda: self.addWidget(LoadData))
        self.actionApply_Mask.triggered.connect(lambda: self.addWidget(MaskData))
        self.actionMultiply_by_Vector.triggered.connect(lambda: self.addWidget(MultiplyByVector))
        self.actionNormalization.triggered.connect(lambda: self.addWidget(Normalization))
        self.actionSet_Output_Path.triggered.connect(lambda: self.addWidget(OutputFolder))
        self.actionPeak_Areas.triggered.connect(lambda: self.addWidget(PeakAreas))
        self.actionPlot.triggered.connect(lambda: self.addWidget(Plot))
        self.actionPlot_ICA_PCA.triggered.connect(lambda: self.addWidget(Plot_ICA_PCA))
        self.actionPlot_Spectra.triggered.connect(lambda: self.addWidget(PlotSpectra))
        self.actionTrain.triggered.connect(lambda: self.addWidget(RegressionTrain))
        self.actionRemove_Rows.triggered.connect(lambda: self.addWidget(RemoveRows))
        self.actionSplit_Data.triggered.connect(lambda: self.addWidget(SplitDataset))
        self.actionStratified_Folds.triggered.connect(lambda: self.addWidget(StratifiedFolds))
        self.actionSubmodel_Predict.triggered.connect(lambda: self.addWidget(SubmodelPredict))
        self.actionCreate_New_Workflow.triggered.connect(lambda: new())
        # self.deleteModulePushButton.clicked.connect(lambda: del_qwidget(self.w))

