from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.PeakAreas import Ui_Form
import numpy as np

class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataComboBox']
        peaks_mins_file = params['[peakMinimaLineEdit']
        if peaks_mins_file == "None (Calculate from avg spectrum)":
            peaks_mins_file = None

        try:
            peaks, mins = self.data[datakey].peak_area(peaks_mins_file=peaks_mins_file)
            print("Peak Areas Calculated")

            np.savetxt(self.outpath + '/peaks.csv', peaks, delimiter=',')
            np.savetxt(self.outpath + '/mins.csv', mins, delimiter=',')

        except Exception as e:
            print(e)
