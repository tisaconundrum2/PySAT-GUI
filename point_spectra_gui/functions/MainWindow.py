import multiprocessing as mp
import os.path
import warnings
import pickle
import sys
import time

try:
    import qtmodern.styles

    q = True
except:
    q = False
    warnings.warn("You're missing the qtmodern package."
                  "to install it use pip install qtmodern")

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSettings

from point_spectra_gui import functions
from point_spectra_gui.ui import MainWindow
from point_spectra_gui.util import delete
from point_spectra_gui.util.BasicFunctionality import Basics
from point_spectra_gui.util.excepthook import my_exception_hook


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class TitleWindow:
    def __init__(self, mainName):
        self.mainName = mainName
        self.fileName = ''
        self.debugName = ''

    def setMainName(self, name):
        self.mainName = name

    def setFileName(self, name):
        self.fileName = name

    def setDebugName(self, bool):
        if bool:
            self.debugName = "Debug Mode"
        else:
            self.debugName = ''

    def display(self):
        if self.fileName == '' and self.debugName == '':
            return "{}".format(self.mainName)
        elif self.fileName == '':
            return "{} - {}".format(self.mainName, self.debugName)
        elif self.debugName == '':
            return "{} - {}".format(self.mainName, self.fileName)
        else:
            return "{} - {} - {}".format(self.mainName, self.fileName, self.debugName)


class Ui_MainWindow(MainWindow.Ui_MainWindow, QtCore.QThread, Basics):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widgetList = []
        self.leftOff = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.MainWindow = MainWindow
        self.title = TitleWindow(self.MainWindow.windowTitle())
        if self.settings.value("debug"): self.debug_mode()
        self.menu_item_shortcuts()  # set up the shortcuts
        self.connectWidgets()
        self.normal_mode()

    def normal_mode(self):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = sys.__stderr__
        # sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
        self.actionOn.setDisabled(False)
        self.actionOff.setDisabled(True)
        self.debug = False
        self.settings.setValue("debug", self.debug)
        self.title.setDebugName(self.debug)
        self.MainWindow.setWindowTitle(self.title.display())

    def debug_mode(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        self.actionOn.setDisabled(True)
        self.actionOff.setDisabled(False)
        self.debug = True
        self.settings.setValue("debug", self.debug)
        self.title.setDebugName(self.debug)
        self.MainWindow.setWindowTitle(self.title.display())

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
        self.widgetList[-1].setupUi(self.scrollArea)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(self.widgetList[-1].get_widget())

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionRestore_Workflow.setShortcut("ctrl+O")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")
        self.okPushButton.setShortcut("Ctrl+Return")

    def connectWidgets(self):
        """
        Connect all the widgets associated with the MainWindow UI
        :return:
        """
        # TODO figure out how to get this code into `MainWindow.py`
        try:
            self.actionRead_ChemCam_Data.triggered.connect(
                lambda: self.addWidget(functions.ReadChemCamData.ReadChemCamData))
            self.actionRemove_Baseline.triggered.connect(
                lambda: self.addWidget(functions.BaselineRemoval.BaselineRemoval))
            self.actionCross_Validation.triggered.connect(
                lambda: self.addWidget(functions.CrossValidation.CrossValidation))
            self.actionDimensionality_Reduction.triggered.connect(
                lambda: self.addWidget(functions.DimensionalityReduction.DimensionalityReduction))
            self.actionInterpolate.triggered.connect(
                lambda: self.addWidget(functions.Interpolation.Interpolation))
            self.actionLoad_Data.triggered.connect(
                lambda: self.addWidget(functions.LoadData.LoadData))
            self.actionSave_Current_Data.triggered.connect(
                lambda: self.addWidget(functions.WriteToCSV.WriteToCSV))
            self.actionRename_Data.triggered.connect(
                lambda: self.addWidget(functions.RenameData.RenameData))
            self.actionApply_Mask.triggered.connect(
                lambda: self.addWidget(functions.MaskData.MaskData))
            self.actionMultiply_by_Vector.triggered.connect(
                lambda: self.addWidget(functions.MultiplyByVector.MultiplyByVector))
            self.actionNormalization.triggered.connect(
                lambda: self.addWidget(functions.Normalization.Normalization))
            self.actionSet_Output_Path.triggered.connect(
                lambda: self.addWidget(functions.OutputFolder.OutputFolder))
            self.actionPeak_Areas.triggered.connect(
                lambda: self.addWidget(functions.PeakAreas.PeakAreas))
            self.actionPlot.triggered.connect(
                lambda: self.addWidget(functions.Plot.Plot))
            self.actionPlot_ICA_PCA.triggered.connect(
                lambda: self.addWidget(functions.Plot_ICA_PCA.Plot_ICA_PCA))
            self.actionPlot_Spectra.triggered.connect(
                lambda: self.addWidget(functions.PlotSpectra.PlotSpectra))
            self.actionTrain.triggered.connect(
                lambda: self.addWidget(functions.RegressionTrain.RegressionTrain))
            self.actionPredict.triggered.connect(
                lambda: self.addWidget(functions.RegressionPredict.RegressionPredict))
            self.actionRemove_Rows.triggered.connect(
                lambda: self.addWidget(functions.RemoveRows.RemoveRows))
            self.actionSplit_Data.triggered.connect(
                lambda: self.addWidget(functions.SplitDataset.SplitDataset))
            self.actionStratified_Folds.triggered.connect(
                lambda: self.addWidget(functions.StratifiedFolds.StratifiedFolds))
            self.actionSubmodel_Predict.triggered.connect(
                lambda: self.addWidget(functions.SubmodelPredict.SubmodelPredict))
            self.actionCreate_New_Workflow.triggered.connect(self.new)
            self.actionSave_Current_Workflow.triggered.connect(self.on_save_clicked)
            self.actionRestore_Workflow.triggered.connect(self.on_restore_clicked)
            self.deleteModulePushButton.clicked.connect(self.on_delete_module_clicked)
            self.okPushButton.clicked.connect(self.on_okButton_clicked)
            self.undoModulePushButton.clicked.connect(self.on_undoButton_clicked)
            self.stopPushButton.clicked.connect(self.on_stopButton_clicked)
            self.actionOn.triggered.connect(self.debug_mode)
            self.actionOff.triggered.connect(self.normal_mode)
            self.actionExit.triggered.connect(lambda: sys.exit())

        except Exception as e:
            print(e)

    def closeEvent(self, e):
        # Write window size and position to config file
        print("Closing application")
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())
        e.accept()

    def getWidgetItems(self):
        """
        This function iterates through widgetList
        gets the name of all the fuctions
        and then all of the parameters in the UI
        and write it to a list to be returned

        Iterate through widgetList
        get the names of functions, add it to a temp l
        add f list to be the first item in ui_items
        """
        f = []
        ui_items = []
        for f_items in self.widgetList:
            f.append(type(f_items).__name__)
        ui_items.append(f)

        for dat in self.widgetList:
            ui_items.append(dat.getGuiParams())
        return ui_items

    def setWidgetItems(self, dict):
        """
        This function iterates through a `dict`
        and restores the UI
        :param dict:
        :return:
        """
        for f_items in dict[0]:
            """
            Really complex way of running essentially this:
            `self.addWidget(functions.SplitDataset.SplitDataset))`
            Part of the reason why we're doing this is because we're saving function
            names to a list, you can't save function instances. So this is the next
            best thing.
            """
            self.addWidget(getattr(getattr(functions, f_items), f_items))

        for i in range(1, len(dict)):
            self.widgetList[i - 1].setGuiParams(dict[i])

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
            self.title.setFileName(filename.split('/')[-1])
            self.MainWindow.setWindowTitle(self.title.display())
        except Exception as e:
            print("File not loaded {}".format(e))

    def on_restore_clicked(self):
        try:
            filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                      "Open Workflow File",
                                                                      self.outpath,
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'rb') as fp:
                self.setWidgetItems(pickle.load(fp))
            self.title.setFileName(filename.split('/')[-1])
            self.MainWindow.setWindowTitle(self.title.display())
        except Exception as e:
            print("File not loaded: {}".format(e))

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

    def on_undoButton_clicked(self):
        try:
            if not self.widgetList[-1].isEnabled():
                self.leftOff -= 1
                self.widgetList[self.leftOff].setDisabled(False)
        except:
            pass

    def on_stopButton_clicked(self):
        if self.isRunning():
            self.terminate()
            self.taskFinished.emit()
        else:
            print("There is nothing running right now")

    def onStart(self):  # onStart function
        self.progressBar.setRange(0, 0)  # make the bar pulse green
        self.start()  # TaskThread.start()
        # This is multithreading thus run() == start()

    def onFinished(self):  # onFinished function
        self.progressBar.setRange(0, 1)  # stop the bar pulsing green
        self.progressBar.setValue(1)  # displays 100% after process is finished.

    def new(self):
        p = mp.Process(target=main, args=())
        p.start()

    def run(self):
        if self.debug:
            for modules in range(self.leftOff, len(self.widgetList)):
                name_ = type(self.widgetList[modules]).__name__
                s = time.time()
                print("{} Module is Running...".format(name_))
                self.widgetList[modules].setProgressBar(self.progressBar)
                self.widgetList[modules].function()
                e = time.time()
                print("Module {} executed in: {} seconds".format(name_, e - s))
                self.widgetList[modules].setDisabled(True)
                self.leftOff = modules + 1
            self.taskFinished.emit()

        else:
            try:
                for modules in range(self.leftOff, len(self.widgetList)):
                    name_ = type(self.widgetList[modules]).__name__
                    s = time.time()
                    print("{} Module is Running...".format(name_))
                    self.widgetList[modules].setProgressBar(self.progressBar)
                    self.widgetList[modules].function()
                    e = time.time()
                    print("Module {} executed in: {} seconds".format(name_, e - s))
                    self.widgetList[modules].setDisabled(True)
                    self.leftOff = modules + 1
                self.taskFinished.emit()
            except Exception as e:
                print("Your module broke: please fix.", e)
                self.widgetList[self.leftOff].setDisabled(False)
                self.taskFinished.emit()


def get_splash(app):
    """
    Get the splash screen for the application
    But check to see if the image even exists
    :param app:
    :return:
    """
    dir = '../images/'
    if os.path.exists(dir + 'splash.png'):
        splash_pix = QPixmap(dir + 'splash.png')  # default
        app_icon = QtGui.QIcon(dir + 'icon.png')
        app.setWindowIcon(app_icon)
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.show()
        time.sleep(0.5)
        app.processEvents()


def main():
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
