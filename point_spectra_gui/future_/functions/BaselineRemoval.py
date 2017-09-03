from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.BaselineRemoval import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        pass


    def getGuiParams(self):
        return super().getGuiParams()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        datakey_new = Basics.datakeys + '-Baseline Removed-' + method + str(params)
        datakey_baseline = datakey + '-Baseline-' + method + str(params)
        self.datakeys.append(datakey_new)
        self.datakeys.append(datakey_baseline)
        self.data[datakey_new] = spectral_data(self.data[datakey].df.copy(deep=True))
        self.data[datakey_new].remove_baseline(method, segment=True, params=params)
        self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)