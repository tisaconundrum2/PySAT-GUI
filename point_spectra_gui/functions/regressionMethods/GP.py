from point_spectra_gui.ui.GP import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        index = self.chooseDimensionalityReductionMethodComboBox.currentIndex()
        params = {'reduce_dim': self.chooseDimensionalityReductionMethodComboBox.itemText(index),
                  'n_components': self.numOfComponentsSpinBox.value(),
                  'random_start': self.numOfRandomStartsSpinBox.value(),
                  'theta0': self.startingThetaDoubleSpinBox.value(),
                  'thetaL': self.lowerBoundOnThetaDoubleSpinBox.value(),
                  'thetaU': self.upperBoundOnThetaDoubleSpinBox.value()}

        modelkey = str(params)
        return params, modelkey
