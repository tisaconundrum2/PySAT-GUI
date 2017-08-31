from PyQt5 import QtWidgets

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.LoadData import Ui_loadData


class Ui_Form(Ui_loadData, Basics):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def connectWidgets(self):
        super().connectWidgets()
        print(Ui_Form.uiID)
        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.fileNameLineEdit))

    def getGuiParams(self):
        return super().getGuiParams()
