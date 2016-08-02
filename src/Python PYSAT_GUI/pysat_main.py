from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        pysat_ui.mainframe(self, MainWindow)
        pysat_ui.files(self, MainWindow)
        pysat_ui.normalization(self, MainWindow)
        pysat_ui.setup(self, MainWindow)
        pysat_ui.compranges(self, MainWindow)
        pysat_ui.createmodels(self, MainWindow)
        pysat_ui.ok(self, MainWindow)
        pysat_ui.buttonFunctions(self)


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