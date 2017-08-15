import os.path
import sys
import time
from PyQt5 import QtGui

from PyQt5 import QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from point_spectra_gui.future_.functions import *
from point_spectra_gui.future_.util.excepthook import my_exception_hook


def get_splash(app):
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


def main():
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    mw = QtWidgets.QMainWindow()
    mainW = MainWindow.Ui_MainWindow()
    mainW.setupUi(mw)

    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
