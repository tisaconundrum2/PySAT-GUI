import pickle

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui.future_ import functions
from point_spectra_gui.future_.util import delete
from point_spectra_gui.ui import MainWindow


class Ui_MainWindow(MainWindow.Ui_MainWindow, QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widgetList = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.menu_item_shortcuts()  # set up the shortcuts
        self.connectWidgets()

    def addWidget(self, obj):
        """
        Organize our widgets using a list
        Each widget is addressed separately due to being in a list
        This makes deleting easier
        In the future we will want to parse this list and pull
        out necessary data
        :param obj:
        :return:
        """
        self.widgetList.append(obj())
        wl_len = len(self.widgetList) - 1
        self.widgetList[wl_len].setupUi(self.scrollArea)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(self.widgetList[wl_len].get_widget())

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionRestore_Workflow.setShortcut("ctrl+R")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")

    def connectWidgets(self):
        """
        Connect all the widgets associated with the MainWindow UI
        :param ui:
        :return:
        """
        # TODO figure out how to get this code into `MainWindow.py`
        try:
            self.actionRead_ChemCam_Data.triggered.connect(lambda: self.addWidget(functions.ReadChemCamData.Ui_Form))
            self.actionRemove_Baseline.triggered.connect(lambda: self.addWidget(functions.BaselineRemoval.Ui_Form))
            self.actionCross_Validation.triggered.connect(lambda: self.addWidget(functions.CrossValidation.Ui_Form))
            self.actionDimensionality_Reduction.triggered.connect(
                lambda: self.addWidget(functions.DimensionalityReduction.Ui_Form))
            self.actionInterpolate.triggered.connect(lambda: self.addWidget(functions.Interpolation.Ui_Form))
            self.actionLoad_Data.triggered.connect(lambda: self.addWidget(functions.LoadData.Ui_Form))
            self.actionApply_Mask.triggered.connect(lambda: self.addWidget(functions.MaskData.Ui_Form))
            self.actionMultiply_by_Vector.triggered.connect(lambda: self.addWidget(functions.MultiplyByVector.Ui_Form))
            self.actionNormalization.triggered.connect(lambda: self.addWidget(functions.Normalization.Ui_Form))
            self.actionSet_Output_Path.triggered.connect(lambda: self.addWidget(functions.OutputFolder.Ui_Form))
            self.actionPeak_Areas.triggered.connect(lambda: self.addWidget(functions.PeakAreas.Ui_Form))
            self.actionPlot.triggered.connect(lambda: self.addWidget(functions.Plot.Ui_Form))
            self.actionPlot_ICA_PCA.triggered.connect(lambda: self.addWidget(functions.Plot_ICA_PCA.Ui_Form))
            self.actionPlot_Spectra.triggered.connect(lambda: self.addWidget(functions.PlotSpectra.Ui_Form))
            self.actionTrain.triggered.connect(lambda: self.addWidget(functions.RegressionTrain.Ui_Form))
            self.actionRemove_Rows.triggered.connect(lambda: self.addWidget(functions.RemoveRows.Ui_Form))
            self.actionSplit_Data.triggered.connect(lambda: self.addWidget(functions.SplitDataset.Ui_Form))
            self.actionStratified_Folds.triggered.connect(lambda: self.addWidget(functions.StratifiedFolds.Ui_Form))
            self.actionSubmodel_Predict.triggered.connect(lambda: self.addWidget(functions.SubmodelPredict.Ui_Form))
            self.actionSave_Current_Workflow.triggered.connect(lambda: self.on_save_clicked())
            self.deleteModulePushButton.clicked.connect(lambda: delete.del_layout(self.verticalLayout_3))
            self.deleteModulePushButton.clicked.connect(lambda: self.on_delete_module_clicked())
        except Exception as e:
            print(e)

    def getWidgetItems(self):
        """
        return the dictionary from widgetList
        :param index:
        :return:
        """
        ui_items = []
        for dat in self.widgetList:
            ui_items.append(dat.getGuiParams())
        return ui_items

    def on_save_clicked(self):
        """
        Save the workflow to a *.wrf file
        :return:
        """
        try:
            filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                      "Choose where you want save your file",
                                                                      '.',
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump(self.getWidgetItems(), fp)
        except:
            print("File not loaded")

    # def run(self):

    def on_delete_module_clicked(self):
        try:
            del self.widgetList[-1]
        except:
            print("Cannot delete")
