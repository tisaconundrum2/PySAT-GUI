import unittest

from PyQt5.QtWidgets import *

from point_spectra_gui.functions.MainWindow import Ui_MainWindow

class TestSet(unittest.TestCase):
    def test_(self):
        mainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow)
        assert isinstance(ui.centralwidget, QWidget)
