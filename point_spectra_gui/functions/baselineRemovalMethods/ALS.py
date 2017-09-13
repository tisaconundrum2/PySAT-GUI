from point_spectra_gui.ui.ALS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formLayout

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'asymmetry_param': self.asymmetryDoubleSpinBox.value(),
                            'smoothness_param': self.smoothnessDoubleSpinBox.value(),
                            'max_iters': self.maxNumOfIterationsSpinBox.value(),
                            'conv_thresh': self.convergenceThresholdDoubleSpinBox.value()}
        return methodParameters
