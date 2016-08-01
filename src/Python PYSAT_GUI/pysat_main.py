from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from mainwindow_compranges import compranges
from mainwindow_createmodels import createmodels
from mainwindow_files import files
from mainwindow_normalization import normalization
from mainwindow_setup import setup
from mainwindow_ import Ui_MainWindow
from mainwindow_ok import ok





class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        files.setupUi(self, MainWindow)
        normalization.setupUi(self, MainWindow)
        setup.setupUi(self, MainWindow)
        compranges.setupUi(self, MainWindow)
        createmodels.setupUi(self, MainWindow)
        ok.setupUi(self, MainWindow)



def main():
    app = QApplication(sys.argv)

    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(1.3)

    main_window = Main()
    main_window.show()
    splash.finish(main_window)
    app.exec_()

if __name__ == "__main__":
    main()