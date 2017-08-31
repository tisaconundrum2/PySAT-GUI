from PyQt5 import QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.ui.OutputFolder import Ui_Form


class Ui_Form(Ui_Form):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)
        print(Ui_Form.uiID)
        self.pushButton.clicked.connect(lambda: self.on_outPutLocationButton_clicked())

    def on_outPutLocationButton_clicked(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        self.folderNameLineEdit.setText(filename)
        if self.folderNameLineEdit.text() == "":
            self.folderNameLineEdit.setText("*/")

    def getGuiParams(self):
        # TODO put the parameters inside of a list/dictionary
        # TODO create a function that loads in the necessary module
        print(self.qt.guiSave())
        return self.qt.guiSave()
