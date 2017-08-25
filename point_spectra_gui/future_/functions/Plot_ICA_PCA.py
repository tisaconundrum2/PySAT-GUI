from Qtickle import Qtickle
from point_spectra_gui.ui.Plot_ICA_PCA import Ui_Form


class Ui_Form(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)
        print(Ui_Form.uiID)
