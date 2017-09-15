from PyQt5 import QtWidgets
from sklearn.linear_model.ridge import Ridge
from sklearn.linear_model.ridge import RidgeCV

from point_spectra_gui.ui.Ridge import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Ridge, RidgeCV, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        ridgecv = RidgeCV()

        self.alphasLineEdit_cv.setText(str(ridgecv.alphas))
        self.fitInterceptCheckBox_cv.setChecked(ridgecv.fit_intercept)
        self.normalizeCheckBox_cv.setChecked(ridgecv.normalize)
        self.defaultComboItem(self.scoringComboBox_cv, ridgecv.scoring)
        self.cvLineEdit_cv.setText(str(ridgecv.cv))
        self.defaultComboItem(self.gCVModeComboBox_cv, ridgecv.gcv_mode)
        self.storeCVValuesCheckBox_cv.setChecked(ridgecv.store_cv_values)

        ridge = Ridge()

        self.alphaDoubleSpinBox.setValue(ridge.alpha)
        self.fitInterceptCheckBox.setChecked(ridge.fit_intercept)
        self.normalizeCheckBox.setChecked(ridge.normalize)
        self.copyXCheckBox.setChecked(ridge.copy_X)
        self.defaultComboItem(self.solverComboBox, (ridge.solver))
        self.toleranceDoubleSpinBox.setValue(ridge.tol)
        self.randomStateLineEdit.setText(str(ridge.random_state))

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

        if self.crossValidateCheckBox:
            params = {'alphas': [self.alphasLineEdit_cv],
                      'fit_intercept': [self.fitInterceptCheckBox_cv],
                      'normalize': [self.normalizeCheckBox_cv],
                      'scoring': [self.scoringComboBox_cv],
                      'cv': [self.cvLineEdit_cv],
                      'gcv_mode': [self.gCVModeComboBox_cv],
                      'store_cv_values': [self.storeCVValuesCheckBox_cv]}
        else:
            params = {'alpha': [self.alphaDoubleSpinBox.value()],
                      'copy_X': [self.copyXCheckBox.isChecked()],
                      'fit_intercept': [self.fitInterceptCheckBox.isChecked()],
                      'max_iter': [m_state],
                      'normalize': [self.normalizeCheckBox.isChecked()],
                      'solver': [self.solverComboBox.currentText()],
                      'tol': [self.toleranceDoubleSpinBox.value()],
                      'random_state': [r_state]}
            modelkey = str(params)
            return params, modelkey

    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
