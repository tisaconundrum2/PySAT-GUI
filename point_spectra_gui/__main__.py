import multiprocessing as mp
import os.path
import sys
import time
import warnings

try:
    import qtmodern.styles

    q = True
except:
    q = False
    warnings.warn("You're missing the qtmodern package."
                  "to install it use pip install qtmodern")
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from point_spectra_gui.functions import MainWindow
from point_spectra_gui.util.excepthook import my_exception_hook

theme = False


def new():
    p = mp.Process(target=main, args=())
    p.start()


def darkmode():
    global theme, q
    theme = True
    new()


def connectWidgets(ui):
    ui.actionCreate_New_Workflow.triggered.connect(lambda: new())
    ui.actionQtmodern.triggered.connect(lambda: darkmode())


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
    if q and theme:
        qtmodern.styles.dark(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow.Ui_MainWindow()
    ui.setupUi(mainWindow)
    connectWidgets(ui)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
