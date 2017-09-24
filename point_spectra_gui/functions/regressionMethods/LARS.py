from PyQt5 import QtWidgets
from sklearn.linear_model.least_angle import Lars
from sklearn.linear_model.least_angle import LarsCV

from point_spectra_gui.ui.LARS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Lars, LarsCV, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        # LARS
        lars = Lars()
        lars.fit_intercept
        lars.verbose
        lars.normalize
        lars.precompute
        lars.n_nonzero_coefs
        lars.eps
        lars.copy_X
        lars.fit_path
        lars.positive

        # LARSCV
        larscv = LarsCV()
        larscv.max_iter
        larscv.max_n_alphas
        larscv.n_jobs

    def function(self):
        params = {'n_nonzero_coefs': self.numOfNonzeroCoeffsSpinBox.value(),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'positive': self.positiveCheckBox.isChecked(),
                  'verbose': self.verboseCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'precompute': {'True': True, 'False': False, 'array': 'array'}.get(
                      self.precomputeComboBox.currentText()),
                  'copy_X': self.copyXCheckBox.isChecked(),
                  'eps': float(self.epsDoubleLineEdit.text()),
                  'fit_path': self.fitPathCheckBox.isChecked(),
                  'CV': self.crossValidateCheckBox.isChecked()}

        self.numOfNonzeroCoeffsSpinBox.setDisabled(params['CV'])
        self.fitPathCheckBox.setDisabled(params['CV'])
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
