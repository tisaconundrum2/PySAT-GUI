from point_spectra_gui.ui.CCAM import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formLayout_2

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'scale1': self.lowestWaveletScaleSpinBox.value(),
                            'scale2': self.largestWaveletScaleSpinBox.value()}

        int_flag = self.interpolationMethodComboBox.currentText()
        if int_flag == 'Linear':
            methodParameters['int_flag'] = 0
        elif int_flag == 'Quadratic':
            methodParameters['int_flag'] = 1
        elif int_flag == 'Spline':
            methodParameters['int_flag'] = 2
