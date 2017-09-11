from point_spectra_gui.ui.BayesianRidge import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'n_iter': self.br.numOfIterationsSpinBox.value(),
                  'tol': self.br.toleranceDoubleSpinBox.value(),
                  'alpha_1': self.br.alpha1DoubleSpinBox.value(),
                  'alpha_2': self.br.alpha2DoubleSpinBox.value(),
                  'lambda_1': self.br.lambdaDoubleSpinBox.value(),
                  'lambda_2': self.br.lambdaDoubleSpinBox.value(),
                  'compute_score': self.br.computerScoreCheckBox.isChecked(),
                  'fit_intercept': self.br.fitInterceptCheckBox.isChecked(),
                  'normalize': self.br.normalizeCheckBox.isChecked(),
                  'copy_X': self.br.copyXCheckBox.isChecked(),
                  'verbose': self.br.verboseCheckBox.isChecked()}
        return (params)
