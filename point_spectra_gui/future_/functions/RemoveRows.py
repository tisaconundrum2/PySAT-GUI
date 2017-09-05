from spectral.spectral_data import spectral_data
import numpy as np
from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.RemoveRows import Ui_Form


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

    def functions(self):
        params = self.getGuiParams()

        datakey = params['chooseDataComboBox']
        colname = params['colNameComboBox']
        value = params['valueComboBox']

        try:
            print(self.data[datakey].df.shape)
            vars_level0 = self.data[datakey].df.columns.get_level_values(0)
            vars_level1 = self.data[datakey].df.columns.get_level_values(1)
            vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
            vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
            colname = (vars_level0[vars_level1.index(colname)], colname)

            if value == 'Null':
                self.data[datakey] = spectral_data(self.data[datakey].df.ix[-self.data[datakey].df[colname].isnull()])
            else:
                # find where the values in the specified column match the value to be removed
                coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
                match = coldata == value
                # keep everything except where match is true
                self.data[datakey] = spectral_data(self.data[datakey].df.ix[~match])
            print(self.data[datakey].df.shape)

        except Exception as e:
            print(e)