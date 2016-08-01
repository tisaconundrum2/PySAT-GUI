from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import mainwindow_normalization




class Main(QMainWindow, pysat_ui.compranges):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        mainwindow_normalization.pysat_ui.normalization(self, MainWindow)
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