from point_spectra_gui.future_.ui.UI_DimenstionalityReduction import Ui_Form


class DimenstionalityReduction(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox
