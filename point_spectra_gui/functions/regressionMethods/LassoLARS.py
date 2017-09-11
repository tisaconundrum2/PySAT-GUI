from point_spectra_gui.ui.LassoLARS import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        p_attrib = {'Auto': 'auto', 'True': True, 'False': False, 'Array-like': 'array-like'}
        index = self.precomputeComboBox.currentIndex()
        precomputeComboBox = self.precomputeComboBox.itemText(index)

        params = {'alpha': self.alphaDoubleSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'positive': self.positiveCheckBox.isChecked(),
                  'verbose': self.verboseCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'copy_X': self.copyXCheckBox.isChecked(),
                  'precompute': p_attrib[precomputeComboBox],
                  'max_iter': int(self.maxIterationsSpinBox.value()),
                  'eps': self.epsDoubleSpinBox.value(),
                  'fit_path': self.fitInterceptCheckBox.isChecked(),
                  'model': self.modelComboBox.currentIndex()}
        return (params)
