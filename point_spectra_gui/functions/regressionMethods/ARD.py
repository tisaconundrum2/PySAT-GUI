from point_spectra_gui.ui.ARD import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'n_iter': self.ard.numOfIterationsSpinBox.value(),
                  'tol': self.ard.toleranceDoubleSpinBox.value(),
                  'alpha_1': self.ard.alpha1DoubleSpinBox.value(),
                  'alpha_2': self.ard.alpha2DoubleSpinBox.value(),
                  'lambda_1': self.ard.lambdaDoubleSpinBox.value(),
                  'lambda_2': self.ard.lambdaDoubleSpinBox.value(),
                  'compute_score': self.ard.computerScoreCheckBox.isChecked(),
                  'threshold_lambda': self.ard.thresholdLambdaSpinBox.value(),
                  'fit_intercept': self.ard.fitInterceptCheckBox.isChecked(),
                  'normalize': self.ard.normalizeCheckBox.isChecked(),
                  'copy_X': self.ard.copyXCheckBox.isChecked(),
                  'verbose': self.ard.verboseCheckBox.isChecked()}
        return (params)
