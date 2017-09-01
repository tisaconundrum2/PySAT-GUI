from PyQt5 import QtWidgets

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.OutputFolder import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def on_outPutLocationButton_clicked(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        self.folderNameLineEdit.setText(filename)
        if self.folderNameLineEdit.text() == "":
            self.folderNameLineEdit.setText("*/")

    def connectWidgets(self):
        super().connectWidgets()

        self.pushButton.clicked.connect(lambda: self.on_outPutLocationButton_clicked())

    def getGuiParams(self):
        return super().getGuiParams()

    def function(self):
        params = self.getGuiParams()
        outpath = params['folderNameLineEdit']
        try:
            self.outpath = outpath
            print("Output path folder has been set to " + outpath)
        except Exception as e:
            print("Error: {}; using default outpath: {}".format(e, self.outpath))

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)
