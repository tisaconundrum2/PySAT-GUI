import unittest

from PyQt5.QtWidgets import *

from point_spectra_gui.ui.MainWindow import Ui_MainWindow

class TestSet(unittest.TestCase):
    def test_MainWindow(self):
        mainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        assert isinstance(ui.centralwidget, QWidget)
