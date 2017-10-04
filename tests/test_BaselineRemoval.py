from unittest import TestCase

from PyQt5 import QtWidgets

from point_spectra_gui.core.BaselineRemoval import BaselineRemoval


class TestUi_Form(TestCase):
    def test_get_widget(self):
        Form = QtWidgets.QWidget()
        ui = BaselineRemoval()
        ui.setupUi(Form)
        assert isinstance(ui.get_widget(), QtWidgets.QGroupBox)
