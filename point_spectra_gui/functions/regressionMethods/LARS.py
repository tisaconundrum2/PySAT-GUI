from point_spectra_gui.ui.LARS import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'n_nonzero_coefs': self.numOfNonzeroCoeffsSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'positive': self.positiveCheckBox.isChecked(),
                  'verbose': self.verboseCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'precompute': self.precomputeComboBox.itemText(self.precomputeComboBox.currentIndex()),
                  'copy_X': self.copyXCheckBox.isChecked(),
                  'eps': self.epsDoubleSpinBox.value(),
                  'fit_path': self.fitPathCheckBox.isChecked(),
                  'CV': self.crossValidateCheckBox.isChecked()}
        self.numOfNonzeroCoeffsSpinBox.setDisabled(params['CV'])
        self.fitPathCheckBox.setDisabled(params['CV'])
        return (params)
