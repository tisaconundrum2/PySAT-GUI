from point_spectra_gui.ui.ARD import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'n_iter': self.numOfIterationsSpinBox.value(),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'alpha_1': self.alpha1DoubleSpinBox.value(),
                  'alpha_2': self.alpha2DoubleSpinBox.value(),
                  'lambda_1': self.lambdaDoubleSpinBox.value(),
                  'lambda_2': self.lambdaDoubleSpinBox.value(),
                  'compute_score': self.computerScoreCheckBox.isChecked(),
                  'threshold_lambda': self.thresholdLambdaSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'copy_X': self.copyXCheckBox.isChecked(),
                  'verbose': self.verboseCheckBox.isChecked()}
        return params
