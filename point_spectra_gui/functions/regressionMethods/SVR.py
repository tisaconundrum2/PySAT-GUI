from point_spectra_gui.ui.SVR import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        gamma_index = self.gammaComboBox.currentIndex()
        kernel_index = self.kernelComboBox.currentIndex()
        params = {'C': self.cDoubleSpinBox.value(),
                  'epsilon': self.epsilonDoubleSpinBox.value(),
                  'kernel': self.kernelComboBox.itemText(kernel_index),
                  'degree': self.degreeSpinBox.value(),
                  'gamma': self.gammaComboBox.itemText(gamma_index),
                  'coef0': self.coeff0DoubleSpinBox.value(),
                  'shrinking': self.shrinkingCheckBox.isChecked(),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'cache_size': self.cacheSizeSpinBox.value(),
                  'verbose': self.verboseCheckBox.isChecked(),
                  'max_iter': int(self.maxIterationsSpinBox.value())}
        return params
