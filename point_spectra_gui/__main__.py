import multiprocessing as mp
import os.path
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from point_spectra_gui.frontEndProcessing import *

try:
    mp.set_start_method('spawn')
except:
    pass


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.org_name = "USGS"
        self.app_name = "PYSAT"
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        pysat = frontEndProc()
        pysat.main_window(MainWindow)  # Set up the mainwindow. This is the backbone of the UI it IS REQUIRED
        pysat.menu_item_shortcuts()  # The shortcuts for making things happen in the UI
        pysat.menu_item_functions()  # These are the various functions that make the UI work
        self.ui = pysat.scrollAreaWidgetContents_2

        #### These are the triggers for exit and new
        pysat.actionExit.triggered.connect(lambda: self.exit())  # Exit out of the current workflow
        pysat.actionCreate_New_Workflow.triggered.connect(lambda: self.new())  # Create a new window. It will be blank
        # pysat.actionSave_Current_Workflow.triggered.connect(lambda: self.write_settings())

    def new(self):
        # TODO create a new window to work in. The old window does not disappear
        # try:
        #     # If opening a seperate process fails. Open it up
        #     window = Main(self)
        #     window.show()
        # except:
            p = mp.Process(target=main, args=())
            p.start()

    def exit(self):
        # TODO close the current window
        self.close()


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def main():
    # this code provides more informative errors when PyQt crashes. Based on the answer at:
    # https://stackoverflow.com/questions/34363552/python-process-finished-with-exit-code-1-when-using-pycharm-and-pyqt5/37837374
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QApplication(sys.argv)
    splash_pix = QPixmap('splash.png')  # default
    app_icon = QtGui.QIcon('icon.png')

    if os.path.exists('point_spectra_gui/splash.png'):
        splash_pix = QPixmap('point_spectra_gui/splash.png')
        app_icon = QtGui.QIcon('images/icon.png')

    app.setWindowIcon(app_icon)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()

    main_window = Main()
    main_window.show()
    splash.finish(main_window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
