from PyQt5 import QtWidgets
from sklearn.linear_model import ElasticNet

from point_spectra_gui.ui.ElasticNet import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, ElasticNet, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        self.checkMinAndMax()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.alphaDoubleSpinBox.setValue(self.alpha),
        self.l1RatioDoubleSpinBox.setValue(self.l1_ratio),
        self.fitInterceptCheckBox.setChecked(self.fit_intercept),
        self.normalizeCheckBox.setChecked(self.normalize),
        self.maxNumOfIterationsSpinBox.setValue(self.max_iter),
        self.copyXCheckBox.setChecked(self.copy_X),
        self.toleranceDoubleSpinBox.setValue(self.tol),
        self.positiveCheckBox.setChecked(self.positive),

    def function(self):
        p_attrib = {'False': False, 'True': True, 'Array-like': 'array-like'}
        r_attrib = {'None': None}
        try:
            r_state = int(self.randomStateLineEdit.text())
        except:
            r_state = r_attrib[self.randomStateLineEdit.text()]

        index = self.precomputeComboBox.currentIndex()
        precomputeComboBox = self.precomputeComboBox.itemText(index)

        params = {
            'alpha': [self.alphaDoubleSpinBox.value()],
            'l1_ratio': [self.l1RatioDoubleSpinBox.value()],
            'fit_intercept': [self.fitInterceptCheckBox.isChecked()],
            'normalize': [self.normalizeCheckBox.isChecked()],
            'precompute': [p_attrib[precomputeComboBox]],
            'max_iter': [int(self.maxNumOfIterationsSpinBox.value())],
            'copy_X': [self.copyXCheckBox.isChecked()],
            'tol': [self.toleranceDoubleSpinBox.value()],
            'positive': [self.positiveCheckBox.isChecked()],
            'selection': [self.selectionLineEdit.text()],
            'random_state': [r_state],
            'CV': [self.crossValidateCheckBox.isChecked()]}
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
