from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def Menubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction(self.LoadRDataAction)
        file.addAction(self.LoadUDataAction)
        file.addSeparator()
        file.addAction(self.SaveCPlotAction)
        file.addAction(self.SaveCDataAction)
        file.addSeparator()
        file.addAction(self.CreaNWorkAction)
        file.addAction(self.SaveCWorkAction)
        file.addAction(self.OpenNWorkAction)
        file.addSeparator()
        file.addAction(self.ExitAction)

        prep = menubar.addMenu("Preprocessing")
        prep.addAction(self.NormalizaAction)
        prep.addAction(self.NoiseReduAction)
        prep.addAction(self.ApplyMaskAction)

        prep.addAction(self.InterpolaAction)
        prep.addAction(self.InstruResAction)
        prep.addAction(self.CalibratiAction)
        prep.addAction(self.BaselineRAction)

        visu = menubar.addMenu("Visualization")
        visu.addAction(self.PCAAction)
        visu.addAction(self.ICAAction)
        visu.addAction(self.ClusterinAction)

        regr = menubar.addMenu("Regression")
        regr.addAction(self.PLSAction)
        regr.addAction(self.SMPLSAction)
        regr.addAction(self.ICARegresAction)
        regr.addAction(self.GaussProcAction)
        regr.addAction(self.MLPAction)
        regr.addAction(self.SVMAction)
        regr.addAction(self.OthersAction)

        help = menubar.addMenu("Help")
        help.addAction(self.IndexAction)
        help.addAction(self.ContentAction)
        help.addSeparator()
        help.addAction(self.AboutAction)
        help.addAction(self.AboutQTAction)





    def Filebar(self):
        self.LoadRDataAction = QAction("Load Reference Data", self)

        self.LoadUDataAction = QAction("Load Unknown Data", self)

        self.SaveCPlotAction = QAction("Save Current Plots", self)
        self.SaveCDataAction = QAction("Save Current Data", self)

        self.CreaNWorkAction = QAction("Create New Worwflow", self)
        self.CreaNWorkAction.triggered.connect(self.new)
        self.CreaNWorkAction.setShortcut("ctrl+N")

        self.SaveCWorkAction = QAction("Save Current Workflow", self)
        self.SaveCWorkAction.triggered.connect(self.save)
        self.SaveCWorkAction.setShortcut("ctrl+S")

        self.OpenNWorkAction = QAction("Open A Workflow", self)
        self.OpenNWorkAction.triggered.connect(self.open)
        self.OpenNWorkAction.setShortcut("ctrl+O")

        self.ExitAction = QAction("Exit", self)
        self.ExitAction.triggered.connect(self.exit)
        self.ExitAction.setShortcut("ctrl+W")

        self.NormalizaAction = QAction("Normalization", self)
        self.NoiseReduAction = QAction("Noise Reduction", self)
        self.ApplyMaskAction = QAction("Apply Mask", self)
        self.InterpolaAction = QAction("Interpolate", self)
        self.InstruResAction = QAction("Instrument Response", self)
        self.CalibratiAction = QAction("Calibration Transfer", self)
        self.BaselineRAction = QAction("Baseline Removal", self)

        self.PCAAction       = QAction("PCA", self)
        self.ICAAction       = QAction("ICA", self)
        self.ClusterinAction = QAction("Clustering", self)

        self.PLSAction       = QAction("PLS", self)
        self.SMPLSAction     = QAction("SM-PLS", self)
        self.ICARegresAction = QAction("ICA", self)
        self.GaussProcAction = QAction("Gaussian Process", self)
        self.MLPAction       = QAction("MLP", self)
        self.SVMAction       = QAction("SVM", self)
        self.OthersAction    = QAction("Others...", self)

        self.IndexAction     = QAction("Index", self)
        self.ContentAction   = QAction("Content", self)
        self.AboutAction     = QAction("About", self)
        self.AboutQTAction   = QAction("About QT Creator", self)




    def new(self):
        #TODO create a new window to work in. The old window does not disappear
        window = Main(self)
        window.show()

    def save(self):
        #TODO save the current window's data into a save file
        pass

    def open(self):
        #TODO open file dialog
        self.filename = QFileDialog.getOpenFileName(self, "Open a Workflow File", '.', "(*.wrf)")

    def exit(self):
        #TODO close the current window
        self.close()

    def InitUi(self):
        ## Start With The GUI
        #TODO Add all functions here that need to be seen on the UI
        self.Filebar()
        self.Menubar()
        self.setWindowTitle('PYSAT Editor')
        self.setGeometry(100, 100, 900, 600)



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
