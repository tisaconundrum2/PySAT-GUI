from point_spectra_gui.future_.functions.BasicFunctionality import Basics
from point_spectra_gui.ui.SplitDataset import Ui_Form


class Ui_Form(Ui_Form, Basics):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        super().connectWidgets()
        print(Ui_Form.uiID)

    def getGuiParams(self):
        return super().getGuiParams()
