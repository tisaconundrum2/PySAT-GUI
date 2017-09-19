from PyQt5 import QtWidgets
from sklearn.svm.classes import SVR

from point_spectra_gui.ui.SVR import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, SVR, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.cDoubleSpinBox.setValue(self.C)
        self.epsilonDoubleSpinBox.setValue(self.epsilon)
        self.defaultComboItem(self.kernelComboBox, self.kernel)
        self.degreeSpinBox.setValue(self.degree)
        self.defaultComboItem(self.gammaComboBox, self.gamma)
        self.coeff0DoubleSpinBox.setValue(self.coef0)
        self.shrinkingCheckBox.setChecked(self.shrinking)
        self.toleranceDoubleSpinBox.setValue(self.tol)
        self.cacheSizeSpinBox.setValue(self.cache_size)
        self.verboseCheckBox.setChecked(self.verbose)
        self.maxIterationsSpinBox.setValue(self.max_iter)

    def function(self):
        gamma_index = self.gammaComboBox.currentIndex()
        kernel_index = self.kernelComboBox.currentIndex()
        params = {'C': [self.cDoubleSpinBox.value()],
                  'epsilon': [self.epsilonDoubleSpinBox.value()],
                  'kernel': [self.kernelComboBox.itemText(kernel_index)],
                  'degree': [self.degreeSpinBox.value()],
                  'gamma': [self.gammaComboBox.itemText(gamma_index)],
                  'coef0': [self.coeff0DoubleSpinBox.value()],
                  'shrinking': [self.shrinkingCheckBox.isChecked()],
                  'tol': [self.toleranceDoubleSpinBox.value()],
                  'cache_size': [self.cacheSizeSpinBox.value()],
                  'verbose': [self.verboseCheckBox.isChecked()],
                  'max_iter': [int(self.maxIterationsSpinBox.value())]}
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
