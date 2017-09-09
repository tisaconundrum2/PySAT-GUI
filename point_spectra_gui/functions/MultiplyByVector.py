from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.MultiplyByVector import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataComboBox']
        vectorfile = params['vectorFileLineEdit']

        try:
            self.data[datakey].multiply_vector(vectorfile)
        except Exception as e:
            print(e)
