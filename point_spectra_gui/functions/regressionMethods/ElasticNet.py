from point_spectra_gui.ui.ElasticNet import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        p_attrib = {'False': False, 'True': True, 'Array-like': 'array-like'}
        r_attrib = {'None': None}
        try:
            r_state = int(self.randomStateLineEdit.text())
        except:
            r_state = r_attrib[self.randomStateLineEdit.text()]

        index = self.precomputeComboBox.currentIndex()
        precomputeComboBox = self.precomputeComboBox.itemText(index)

        params = {'alpha': self.alphaDoubleSpinBox.value(),
                  'l1_ratio': self.l1RatioDoubleSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'precompute': p_attrib[precomputeComboBox],
                  'max_iter': int(self.maxNumOfIterationsSpinBox.value()),
                  'copy_X': self.copyXCheckBox.isChecked(),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'warm_start': self.warmStartCheckBox.isChecked(),
                  'positive': self.positiveCheckBox.isChecked(),
                  'selection': self.selectionLineEdit.text(),
                  'random_state': r_state,
                  'CV': self.crossValidateCheckBox.isChecked()}
        return (params)