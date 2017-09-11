from point_spectra_gui.ui.Lasso import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        params = {'alpha': self.alphaDoubleSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'max_iter': int(self.maxNumOfIterationsSpinBox.value()),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'positive': self.forcePositiveCoefficientsCheckBox.isChecked(),
                  'selection': 'random',
                  'CV': self.optimizeWCrossValidaitonCheckBox.isChecked()}
        return params

