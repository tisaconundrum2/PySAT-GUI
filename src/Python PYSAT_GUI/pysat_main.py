import inspect

from PYSAT_UI_MODULES import error_print
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.org_name = "USGS"
        self.app_name = "PYSAT"
        self.read_settings()
        self.runningFunctions(self)

    # def closeEvent(self, event):
    #     self.write_settings()

    def runningFunctions(self, MainWindow):
        pysat = pysat_ui()
        pysat.main_window(MainWindow)  # Set up the mainwindow. This is the backbone of the UI it IS REQUIRED
        pysat.menu_item_shortcuts()  # The shortcuts for making things happen in the UI
        pysat.menu_item_functions(MainWindow)  # These are the various functions that make the UI work
        self.ui = pysat.scrollAreaWidgetContents_2

        #### These are the triggers for exit and new
        pysat.actionExit.triggered.connect(lambda: self.exit())  # Exit out of the current workflow
        pysat.actionCreate_New_Workflow.triggered.connect(lambda: self.new())  # Create a new window. It will be blank
        pysat.actionOpen_Workflow.triggered.connect(lambda: self.read_settings())  # trigger the loading of workflow.
        # pysat.actionSave_Current_Workflow.triggered.connect(lambda: self.write_settings())

    # void MainWindow::writeSettings() {
    #   QSettings settings("reaffer Soft", "reafferApp");
    #   settings.beginGroup("MainWindow");
    #   settings.setValue("size", size());
    #   settings.setValue("pos", pos());
    #   settings.endGroup();
    # }
    # def write_settings(self):
    #     for name, obj in inspect.getmembers(self.ui):
    #
    #         if isinstance(obj, QComboBox):
    #             index = obj.currentIndex()
    #             name = obj.objectName()
    #             value = self.settings.value(name)
    #
    #             if value == "":
    #                 continue
    #
    #             index = obj.findText(value)
    #
    #             if index == -1:
    #                 obj.insertItems(0, [value])
    #                 index = obj.findText(value)
    #                 obj.setCurrentIndex(index)
    #             else:
    #                 obj.setCurrentIndex(index)
    #
    #         if isinstance(obj, QLineEdit):
    #             name = obj.objectName()
    #             value = self.settings.value(name)  # get stored value from registry
    #             obj.setText(value)  # restore lineEditFile
    #
    #         if isinstance(obj, QCheckBox):
    #             name = obj.objectName()
    #             value = self.settings.value(name)  # get stored value from registry
    #             if value != None:
    #                 obj.setChecked(value)  # restore checkbox
    #
    #         if isinstance(obj, QRadioButton):
    #             name = obj.objectName()
    #             value = self.settings.value(name)  # get stored value from registry
    #             if value != None:
    #                 obj.setChecked(value)
    #
    #         if isinstance(obj, QSlider):
    #             name = obj.objectName()
    #             value = self.settings.value(name)  # get stored value from registry
    #             if value != None:
    #                 obj.setValue(int(value))  # restore value from registry
    #
    #         if isinstance(obj, QSpinBox):
    #             name = obj.objectName()
    #             value = self.settings.value(name)  # get stored value from registry
    #             if value != None:
    #                 # obj.setValue(int(value))  # restore value from registry

    #
    # void MainWindow::readSettings(){
    #   QSettings  settings("reaffer Soft", "reafferApp");
    #   settings.beginGroup("MainWindow");
    #   resize(settings.value("size", QSize(400, 400)).toSize());
    #   move(settings.value("pos", QPoint(200, 200)).toPoint());
    #   settings.endGroup();
    # }
    def read_settings(self):
        try:
            for i in range(len(pysat_func.ui_list)):
                pysat_func.ui_list[i]()

        except Exception as e:
            error_print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()

    main_window = Main()
    main_window.show()
    splash.finish(main_window)
    app.exec_()
