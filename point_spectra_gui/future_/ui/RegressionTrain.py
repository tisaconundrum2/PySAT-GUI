from point_spectra_gui.future_.ui.UI_RegressionTrain import Ui_Form


class RegressionTrain(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.regression
