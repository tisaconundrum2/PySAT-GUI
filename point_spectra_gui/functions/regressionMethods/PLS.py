from point_spectra_gui.ui.PLS import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        nc = self.numOfComponentsLineEdit.text().split(',')
        nc = [int(i) for i in nc]
        params = {'n_components': nc,
                  'scale': [False]}
        modelkey = '(nc=' + str(params['n_components']) + ')'
        return params, modelkey
