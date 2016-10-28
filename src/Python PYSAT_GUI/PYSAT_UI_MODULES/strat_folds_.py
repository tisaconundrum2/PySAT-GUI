from PyQt4 import QtCore, QtGui
import pysat_func
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


def strat_folds(pysat_fun, destination):
    strat_folds_gbox = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    strat_folds_gbox.setFont(font)
    strat_folds_gbox.setObjectName(_fromUtf8("Stratified Folds"))
    strat_folds_vlayout = QtGui.QVBoxLayout(strat_folds_gbox)
    strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
    strat_folds_choose_data_label = QtGui.QLabel(strat_folds_gbox)
    strat_folds_choose_data_label.setObjectName(_fromUtf8("strat_folds_choose_data_label"))
    strat_folds_vlayout.addWidget(strat_folds_choose_data_label)
    datachoices=pysat_fun.datakeys
    if datachoices==[]:
        datachoices=['No data has been loaded!']
    strat_folds_choose_data=make_combobox(datachoices)
    strat_folds_vlayout.addWidget(strat_folds_choose_data)
    strat_folds_choose_var_label = QtGui.QLabel(strat_folds_gbox)
    strat_folds_choose_var_label.setObjectName(_fromUtf8("strat_folds_choose_var_label"))
    strat_folds_vlayout.addWidget(strat_folds_choose_var_label)
    
    varchoices=pysat_fun.data[strat_folds_choose_data.currentText()].df['comp'].columns.values
    strat_folds_choose_var=make_combobox(varchoices)
    strat_folds_vlayout.addWidget(strat_folds_choose_var)
    choices = pysat_fun.data[strat_folds_choose_data.currentText()].df['meta'].columns.values
    
    strat_folds_choose_data.activated[int].connect(lambda: strat_fold_change_vars(strat_folds_choose_var,choices))
    strat_folds_hlayout = QtGui.QHBoxLayout()
    strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
    nfolds_label = QtGui.QLabel(strat_folds_gbox)
    nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
    strat_folds_hlayout.addWidget(nfolds_label)
    nfolds_spin = QtGui.QSpinBox(strat_folds_gbox)
    nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
    nfolds_spin.setMinimum(1)
    strat_folds_hlayout.addWidget(nfolds_spin)
    test_fold_label = QtGui.QLabel(strat_folds_gbox)
    test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
    strat_folds_hlayout.addWidget(test_fold_label)
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