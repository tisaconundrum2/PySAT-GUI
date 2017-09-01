from PyQt5 import QtWidgets

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.CrossValidation import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.regression

    def make_reg_widget(self, alg, params=None):
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtWidgets.QWidget()
        if alg == 'PLS':
            pass
        if alg == 'GP':
            pass
        if alg == 'OLS':
            pass
        if alg == 'OMP':
            pass
        if alg == 'Lasso':
            pass
        if alg == 'Elastic Net':
            pass
        if alg == 'Ridge':
            pass
        if alg == 'Bayesian Ridge':
            pass
        if alg == 'ARD':
            pass
        if alg == 'LARS':
            pass
        if alg == 'Lasso LARS':
            pass
        if alg == 'SVR':
            pass
        if alg == 'KRR':
            pass

        self.reg_widget.setObjectName("self.reg_widget")
        self.cv_vlayout.addWidget(self.reg_widget)
        self.get_cv_parameters()

    def connectWidgets(self):
        super().connectWidgets()

    def getGuiParams(self):
        return super().getGuiParams()

    def setDisabled(self, bool):
        self.groupBox.setDisabled(bool)
