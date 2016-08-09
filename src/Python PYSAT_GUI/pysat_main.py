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
        self.actionLoad_Unknown_Data.triggered.connect(lambda: pysat_ui.files(self, MainWindow))
        self.actionNormalization.triggered.connect(lambda: pysat_ui.normalization(self, MainWindow))
        self.actionCreate_New_Workflow.triggered.connect(lambda: self.new())
        # pysat_ui.setup(self, MainWindow)
        # pysat_ui.compranges(self, MainWindow)
        # pysat_ui.createmodels(self, MainWindow)
        pysat_ui.menu_item_shortcuts(self)
        pysat_ui.ok(self, MainWindow)

    def new(self):
        # TODO create a new window to work in. The old window does not disappear
        window = Main(self)
        window.show()


    def save(self):
        # TODO save the current window's data into a save file
        pass


    def open(self):
        # TODO open file dialog
        self.filename = QFileDialog.getOpenFileName(self, "Open a Workflow File", '.', "(*.wrf)")


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