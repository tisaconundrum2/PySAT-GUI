from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.Interpolation import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        pass

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        datakey_to_interp = params['interpolateDataComboBox']
        datakey_ref = params['referenceDataComboBox']
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            print(e)
