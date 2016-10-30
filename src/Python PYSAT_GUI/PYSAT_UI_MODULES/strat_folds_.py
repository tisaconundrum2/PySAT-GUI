from PyQt4 import QtCore, QtGui
from pysat.utils.gui_utils import make_combobox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class strat_folds_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8

        font = QtGui.QFont()
        font.setPointSize(10)
        self.strat_folds.setFont(font)
        self.strat_folds.setObjectName(_fromUtf8("Stratified Folds"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout(self.strat_folds)
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_data_label.setObjectName(_fromUtf8("strat_folds_choose_data_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data_label)
        datachoices=self.pysat_fun.datakeys
        if datachoices==[]:
            datachoices=['No data has been loaded!']
        self.strat_folds_choose_data=make_combobox(datachoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_var_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_var_label.setObjectName(_fromUtf8("strat_folds_choose_var_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var_label)
        varchoices=self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        self.strat_folds_choose_var=make_combobox(varchoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var)
        self.strat_folds_choose_data.activated[int].connect(self.strat_fold_change_vars)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(self.strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(self.strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.nfolds_spin.setMinimum(1)
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(self.strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        foldchoices=['1']
        choose_test_fold = make_combobox(foldchoices)
        choose_test_fold.setObjectName(_fromUtf8("choose_test_fold"))
        nfolds_spin.valueChanged.connect(lambda: strat_fold_change_testfolds(choose_test_fold,list(map(str, list(range(1, nfolds_spin.value() + 1))))))
        strat_folds_hlayout.addWidget(choose_test_fold)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        strat_folds_hlayout.addItem(spacerItem)
        create_folds = QtGui.QPushButton(strat_folds_gbox)
        create_folds.setObjectName(_fromUtf8("create_folds"))
        create_folds.setText(_translate("strat_folds", "Create Folds", None))
        strat_folds_hlayout.addWidget(create_folds)
        strat_folds_vlayout.addLayout(strat_folds_hlayout)
        destination.addWidget(strat_folds_gbox)
        strat_folds_gbox.raise_()
        strat_folds_gbox.setTitle(_translate("MainWindow", "Stratified Folds", None))
        nfolds_label.setText(_translate("strat_folds", "N folds", None))
        test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        create_folds.setText(_translate("strat_folds", "Create Folds", None))
        strat_folds_choose_data_label.setText(_translate("strat_folds", "Choose data to stratify:", None))
        strat_folds_choose_var_label.setText(_translate("strat_folds", "Choose variable on which to sort:", None))
        try:
            create_folds.clicked.connect(lambda: pysat_fun.do_strat_folds(datakey=str(strat_folds_choose_data.currentText()),nfolds=int(nfolds_spin.text()),testfold=int(choose_test_fold.currentText()),colname=('comp',strat_folds_choose_var.currentText())))
            # TODO create a working function like the line below
            # create_folds.clicked.connect(lambda: pysat_fun.appendNewFunc(do_strat_folds))
        except:
            print('There was a problem with creating stratified folds...')

    def strat_fold_change_vars(choose_var,choices):
        choose_var.clear()
        print(choices)
        choose_var.addItems(choices)


    def strat_fold_change_testfolds(choose_test_fold,choices):
        choose_test_fold.clear()
        print(choices)
        choose_test_fold.addItems(choices)