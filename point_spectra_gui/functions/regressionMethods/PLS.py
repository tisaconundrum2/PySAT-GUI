from point_spectra_gui.ui.PLS import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'n_components': self.numOfComponentsSpinBox.value(),
                  'scale': False}
        modelkey = '(nc=' + str(params['n_components']) + ')'
        return params, modelkey
