from PyQt5 import QtWidgets
from sklearn.gaussian_process.gaussian_process import GaussianProcess

from point_spectra_gui.ui.GP import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, GaussianProcess, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        self.checkMinAndMax()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.setComboBox(self.regrComboBox, self._regression_types)
        self.defaultComboItem(self.regrComboBox, self.regr)
        self.setComboBox(self.corrComboBox, self._correlation_types)
        self.defaultComboItem(self.corrComboBox, self.corr)
        self.setComboBox(self.storageModeComboBox, ['light', 'full'])
        self.defaultComboItem(self.storageModeComboBox, self.storage_mode)
        self.verboseCheckBox.setChecked(self.verbose)
        self.theta0DoubleSpinBox.setValue(self.theta0)
        self.setComboBox(self.optimizerComboBox, self._optimizer_types)
        self.defaultComboItem(self.optimizerComboBox, self.optimizer)
        self.randomStartSpinBox.setValue(self.random_start)
        self.normalizeCheckBox.setChecked(self.normalize)

    def function(self):
        params = {'reduce_dim': [self.chooseDimensionalityReductionMethodComboBox.currentText().split(',')],
                  'n_components': [self.numOfComponentsLineEdit.text()],
                  'random_start': [self.numOfRandomStartsSpinBox.value()],
                  'theta0': [self.startingThetaDoubleSpinBox.value()],
                  'thetaL': [self.lowerBoundOnThetaDoubleSpinBox.value()],
                  'thetaU': [self.upperBoundOnThetaDoubleSpinBox.value()]}

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
