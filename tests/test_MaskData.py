from unittest import TestCase

from PyQt5 import QtWidgets

from point_spectra_gui.core.MaskData import MaskData


class TestUi_Form(TestCase):
    def test_get_widget(self):
        Form = QtWidgets.QWidget()
        ui = MaskData()
        ui.setupUi(Form)
        self.assertIsInstance(ui.get_widget(), QtWidgets.QGroupBox)
