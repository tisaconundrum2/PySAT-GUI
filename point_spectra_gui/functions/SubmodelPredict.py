from PyQt5 import QtWidgets

from point_spectra_gui.ui.SubmodelPredict import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        pass

    def isEnabled(self): return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
