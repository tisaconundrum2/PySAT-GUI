from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.functions.baselineRemovalMethods import *
from point_spectra_gui.ui.BaselineRemoval import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.chooseAlgorithmList = ['FABC',
                                    'KK',
                                    'Mario',
                                    'Median',
                                    'Rubberband',
                                    'CCAM',
                                    ]
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseAlgorithmComboBox, self.chooseAlgorithmList)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        method = params['chooseAlgorithmComboBox']
        datakey = params['chooseDataComboBox']

        try:


        except:
            pass

        datakey_new = self.datakeys + '-Baseline Removed-' + method + str(methodParameters)
        datakey_baseline = datakey + '-Baseline-' + method + str(methodParameters)
        self.datakeys.append(datakey_new)
        self.datakeys.append(datakey_baseline)
        self.data[datakey_new].remove_baseline(method, segment=True, params=methodParameters)
        self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)

    def baselineMethods(self):
        self.alg = []
        list_forms = []
        list_forms.append(FABC)
        list_forms.append(KK)
        list_forms.append(Mario)
        list_forms.append(Median)
        list_forms.append(Rubberband)
        list_forms.append(CCAM)
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.algorithmLayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)
