from point_spectra_gui.ui.KRR import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        k_attrib = {'None': None}
        params = {'alpha': self.alphaSpinBox.value(),
                  'kernel': self.kernelLineEdit.text(),
                  'gamma': self.gammaLineEdit.text(),
                  'degree': self.degreeDoubleSpinBox.value(),
                  'coef0': self.coeff0DoubleSpinBox.value(),
                  'kernel_params': k_attrib[self.kernelParametersLineEdit.text()]}
        return (params)
