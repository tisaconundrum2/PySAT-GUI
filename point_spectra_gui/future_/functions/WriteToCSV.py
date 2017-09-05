from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.WriteToCSV import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        pass

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataSetComboBox']
        filename = params['specifyAFilenameLineEdit']
        selected_cols = self.variablesToWriteListWidget.selectedItems()
        cols = []
        for selection in selected_cols:
            cols.append(selection.text())

        try:
            datatemp = self.data[datakey].df[cols]
        except:
            datatemp = self.data[datakey][cols]

        try:
            datatemp.to_csv(self.outpath + '/' + filename)
        except:
            datatemp.to_csv(filename)

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)
