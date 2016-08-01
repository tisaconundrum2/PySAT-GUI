from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import compranges
from pysat_ui import mainframe
from pysat_ui import files
from pysat_ui import normalization
from pysat_ui import setup
from pysat_ui import createmodels
from pysat_ui import ok
import antigravity


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        mainframe(self, MainWindow)
        files(self, MainWindow)
        normalization(self, MainWindow)
        setup(self, MainWindow)
        compranges(self, MainWindow)
        createmodels(self, MainWindow)
        ok(self, MainWindow)



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