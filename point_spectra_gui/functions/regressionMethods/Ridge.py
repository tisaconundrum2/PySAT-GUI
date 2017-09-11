from point_spectra_gui.ui.Ridge import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        m_attrib = {'None': None}
        r_attrib = {'None': None}
        try:
            m_state = int(self.maxNumOfIterationslineEdit.text())
        except:
            m_state = m_attrib[self.maxNumOfIterationslineEdit.text()]
        try:
            r_state = int(self.randomStateLineEdit.text())
        except:
            r_state = r_attrib[self.randomStateLineEdit.text()]

        index = self.solverComboBox.currentIndex()
        if self.crossValidateCheckBox:
            params = {'alphas': self.alphasLineEdit_cv,
                      'fit_intercept': self.fitInterceptCheckBox_cv,
                      'normalize': self.normalizeCheckBox_cv,
                      'scoring': self.scoringComboBox_cv,
                      'cv': self.cvLineEdit_cv,
                      'gcv_mode': self.gCVModeComboBox_cv,
                      'store_cv_values': self.storeCVValuesCheckBox_cv}
        else:
            params = {'alpha': self.alphaDoubleSpinBox.value(),
                      'copy_X': self.copyXCheckBox.isChecked(),
                      'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                      'max_iter': m_state,
                      'normalize': self.normalizeCheckBox.isChecked(),
                      'solver': self.solverComboBox.itemText(index),
                      'tol': self.toleranceDoubleSpinBox.value(),
                      'random_state': r_state}
        return (params)
