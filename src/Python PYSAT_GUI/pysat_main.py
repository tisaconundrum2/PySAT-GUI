from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        arr = [None]*10
        pysat_ui.mainframe(self, MainWindow)
        pysat_ui.menu_item_shortcuts(self)
        pysat_ui.menu_item_functions(self, MainWindow)
        #TODO Figure out what is happening below!
        pysat_ui.std_norm(self, MainWindow)
        pysat_ui.val_norm(self, MainWindow, 5)
        pysat_ui.val_norm(self, MainWindow, 6)
        pysat_ui.val_norm(self, MainWindow, 7)
        pysat_ui.ok(self, MainWindow)


    def new(self):
        # TODO create a new window to work in. The old window does not disappear
        window = Main(self)
        window.show()


    def exit(self):
        # TODO close the current window
        self.close()

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