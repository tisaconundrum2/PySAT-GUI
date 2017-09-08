from PyQt5 import QtWidgets

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.MaskData import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.maskFileLineEdit))

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        maskfile = self.maskFileLineEdit.text()
        maskvar = 'wvl'
        try:
            self.data[datakey].mask(maskfile, maskvar=maskvar)
            print("Mask applied")
        except Exception as e:
            print(e)
