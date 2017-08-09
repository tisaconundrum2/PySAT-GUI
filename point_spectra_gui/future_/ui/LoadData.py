from point_spectra_gui.future_.ui.UI_LoadData import Ui_loadData


class Ui_Form(Ui_loadData):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox
