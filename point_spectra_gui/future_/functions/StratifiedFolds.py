from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.StratifiedFolds import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):

        pass

    def getGuiParams(self):
        return super().getGuiParams()

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
        Basics.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        Basics.data[datakey + '-Train'] = Basics.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        Basics.data[datakey + '-Test'] = Basics.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        Basics.datakeys = Basics.data.keys()

        print(Basics.data.keys())
        print(Basics.data[datakey + '-Test'].df.index.shape)
        print(Basics.data[datakey + '-Train'].df.index.shape)