from unittest import TestCase

from PyQt5 import QtWidgets

from point_spectra_gui.functions.BaselineRemoval import Ui_Form


class TestUi_Form(TestCase):
    def test_get_widget(self):
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        assert isinstance(ui.get_widget(), QtWidgets.QGroupBox)
