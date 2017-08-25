from PyQt5 import QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.ui.LoadData import Ui_loadData


class Ui_Form(Ui_loadData):
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
        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked())

    def on_getDataButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", '.', "(*.csv)")
        self.fileNameLineEdit.setText(filename)
        if self.fileNameLineEdit.text() == "":
            self.fileNameLineEdit.setText("*.csv")
