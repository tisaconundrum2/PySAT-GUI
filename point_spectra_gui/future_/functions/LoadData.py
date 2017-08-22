from PyQt5 import QtWidgets

from point_spectra_gui.future_.functions import MainWindow
from point_spectra_gui.ui.LoadData import Ui_loadData


class Ui_Form(Ui_loadData):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        mw = MainWindow.Ui_MainWindow()
        Form.resize(mw.getScrollAreaWidgetSize())

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked())
        # self.get_data_line_edit.textChanged.connect(lambda: self.get_data_params())
        # self.dataname.textChanged.connect(lambda: self.get_data_params())

    def on_getDataButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", '.', "(*.csv)")
        self.fileNameLineEdit.setText(filename)
        if self.fileNameLineEdit.text() == "":
            self.fileNameLineEdit.setText("*.csv")
