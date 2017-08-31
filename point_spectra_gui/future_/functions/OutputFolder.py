from PyQt5 import QtWidgets

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.OutputFolder import Ui_Form


class Ui_Form(Ui_Form, Basics):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.groupBox

    def on_outPutLocationButton_clicked(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        self.folderNameLineEdit.setText(filename)
        if self.folderNameLineEdit.text() == "":
            self.folderNameLineEdit.setText("*/")

    def connectWidgets(self):
        super().connectWidgets()
        print(Ui_Form.uiID)
        self.pushButton.clicked.connect(lambda: self.on_outPutLocationButton_clicked())

    def getGuiParams(self):
        return super().getGuiParams()
