from PyQt5 import QtWidgets
from sklearn.linear_model.least_angle import LassoLars

from point_spectra_gui.ui.LassoLARS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, LassoLars, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.p_attrib = {'auto': 'auto', 'True': True, 'False': False, 'array-like': 'array-like'}
        self.alphaDoubleSpinBox.setValue(self.alpha)
        self.fitInterceptCheckBox.setChecked(self.fit_intercept)
        self.maxIterationsSpinBox.setValue(self.max_iter)
        self.verboseCheckBox.setChecked(self.verbose)
        self.normalizeCheckBox.setChecked(self.normalize)
        self.positiveCheckBox.setChecked(self.positive)
        self.setComboBox(self.precomputeComboBox, self.p_attrib)
        self.defaultComboItem(self.precomputeComboBox, self.precompute)
        print(self.precompute)
        self.copyXCheckBox.setChecked(self.copy_X)
        self.epsDoubleSpinBox.setValue(self.eps)
        self.fitPathCheckBox.setChecked(self.fit_path)

    def function(self):
        index = self.precomputeComboBox.currentIndex()
        precomputeComboBox = self.precomputeComboBox.itemText(index)

        params = {'alpha': [self.alphaDoubleSpinBox.value()],
                  'fit_intercept': [self.fitInterceptCheckBox.isChecked()],
                  'positive': [self.positiveCheckBox.isChecked()],
                  'verbose': [self.verboseCheckBox.isChecked()],
                  'normalize': [self.normalizeCheckBox.isChecked()],
                  'copy_X': [self.copyXCheckBox.isChecked()],
                  'precompute': [self.p_attrib[precomputeComboBox]],
                  'max_iter': [int(self.maxIterationsSpinBox.value())],
                  'eps': [self.epsDoubleSpinBox.value()],
                  'fit_path': [self.fitInterceptCheckBox.isChecked()],
                  'model': [self.modelComboBox.currentIndex()]}
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
