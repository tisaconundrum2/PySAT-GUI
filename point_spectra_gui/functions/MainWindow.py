import pickle
import sys
import time

from PyQt5 import QtCore, QtWidgets, QtGui

from point_spectra_gui import functions
from point_spectra_gui.ui import MainWindow
from point_spectra_gui.util import delete
from point_spectra_gui.util.BasicFunctionality import Basics


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class Ui_MainWindow(MainWindow.Ui_MainWindow, QtCore.QThread, Basics):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widgetList = []
        self.leftOff = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.menu_item_shortcuts()  # set up the shortcuts
        self.connectWidgets()
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

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
        self.okPushButton.setShortcut("Ctrl+Return")

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
            self.deleteModulePushButton.clicked.connect(lambda: self.on_delete_module_clicked())
            self.okPushButton.clicked.connect(lambda: self.on_okButton_clicked())
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
                                                                      self.outpath,
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump(self.getWidgetItems(), fp)
        except:
            print("File not loaded")

    def on_delete_module_clicked(self):
        try:
            if self.widgetList[-1].isEnabled():
                del self.widgetList[-1]
                delete.del_layout(self.verticalLayout_3)
            else:
                print("Cannot delete")
        except:
            print("Cannot delete")

    def on_okButton_clicked(self):
        self.onStart()
        self.taskFinished.connect(self.onFinished)

    def onStart(self):  # onStart function
        self.progressBar.setRange(0, 0)  # make the bar pulse green
        self.start()  # TaskThread.start()
        # This is multithreading thus run() == start()

    def onFinished(self):  # onFinished function
        self.progressBar.setRange(0, 1)  # stop the bar pulsing green
        self.progressBar.setValue(1)  # displays 100% after process is finished.

    def run(self):
        try:
            for modules in range(self.leftOff, len(self.widgetList)):
                s = time.time()
                self.widgetList[modules].setProgressBar(self.progressBar)
                self.widgetList[modules].function()
                e = time.time()
                print("Module executed in: {} seconds".format(e - s))
                self.widgetList[modules].setDisabled(True)
                self.leftOff = modules + 1
            self.taskFinished.emit()
        except Exception as e:
            print(e)
            self.taskFinished.emit()
