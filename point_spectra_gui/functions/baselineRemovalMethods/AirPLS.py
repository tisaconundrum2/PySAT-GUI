from point_spectra_gui.ui.AirPLS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formLayout_2

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'smoothness_param': self.smoothnessSpinBox.value(),
                            'conv_thresh': self.convergenceThresholdDoubleSpinBox.value(),
                            'max_iters': self.maxNumOfIterationsSpinBox.value()}
        return methodParameters
