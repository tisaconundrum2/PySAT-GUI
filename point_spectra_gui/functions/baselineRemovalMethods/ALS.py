from PyQt5 import QtWidgets

from point_spectra_gui.ui.ALS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'asymmetry_param': float(self.asymmetryDoubleSpinBox.value()),
                            'smoothness_param': float(self.smoothnessDoubleSpinBox.value()),
                            'max_iters': int(self.maxNumOfIterationsSpinBox.value()),
                            'conv_thresh': float(self.convergenceThresholdDoubleSpinBox.value())}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
