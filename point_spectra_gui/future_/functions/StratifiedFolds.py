from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.StratifiedFolds import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataToStratifyComboBox, self.datakeys)

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataToStratifyComboBox']
        nfolds = params['nFoldsSpinBox']
        try:
            testfold = int(params['testFoldsSpinBox'])
        except:
            testfold = 1
        colname = ('comp', params['chooseVarComboBox'])
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys = self.data.keys()

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)
