from point_spectra_gui.ui.Mario import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formLayout_2

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def function(self):
        methodParameters = {'poly_order': self.polynomialOrderSpinBox.value(),
                            'max_iters': self.maximumNumOfIterationsDoubleSpinBox.value(),
                            'tol': self.toleranceDoubleSpinBox.value()}
        return methodParameters