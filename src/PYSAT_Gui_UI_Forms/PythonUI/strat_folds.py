# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'strat_folds.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_strat_folds(object):
    def setupUi(self, strat_folds):
        strat_folds.setObjectName(_fromUtf8("strat_folds"))
        strat_folds.resize(602, 150)
        strat_folds.setMinimumSize(QtCore.QSize(600, 150))
        strat_folds.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(strat_folds)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout()
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_data.setObjectName(_fromUtf8("strat_folds_choose_data"))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_element = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_element.setObjectName(_fromUtf8("strat_folds_choose_element"))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_element)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_spin = QtGui.QSpinBox(strat_folds)
        self.test_fold_spin.setObjectName(_fromUtf8("test_fold_spin"))
        self.strat_folds_hlayout.addWidget(self.test_fold_spin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(spacerItem)
        self.create_folds = QtGui.QPushButton(strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout_2.addLayout(self.strat_folds_vlayout)

        self.retranslateUi(strat_folds)
        QtCore.QMetaObject.connectSlotsByName(strat_folds)

    def retranslateUi(self, strat_folds):
        strat_folds.setWindowTitle(_translate("strat_folds", "Stratified Folds", None))
        strat_folds.setTitle(_translate("strat_folds", "Stratified Folds", None))
        self.strat_folds_choose_data.setItemText(0, _translate("strat_folds", "Choose Data", None))
        self.strat_folds_choose_data.setItemText(1, _translate("strat_folds", "Unknown Data", None))
        self.strat_folds_choose_data.setItemText(2, _translate("strat_folds", "Known Data", None))
        self.strat_folds_choose_element.setItemText(0, _translate("strat_folds", "Choose Element to Stratify On", None))
        self.strat_folds_choose_element.setItemText(1, _translate("strat_folds", "SiO2", None))
        self.strat_folds_choose_element.setItemText(2, _translate("strat_folds", "TiO2", None))
        self.strat_folds_choose_element.setItemText(3, _translate("strat_folds", "Al2O3", None))
        self.strat_folds_choose_element.setItemText(4, _translate("strat_folds", "FeOT", None))
        self.strat_folds_choose_element.setItemText(5, _translate("strat_folds", "MgO", None))
        self.strat_folds_choose_element.setItemText(6, _translate("strat_folds", "CaO", None))
        self.strat_folds_choose_element.setItemText(7, _translate("strat_folds", "Na2O", None))
        self.strat_folds_choose_element.setItemText(8, _translate("strat_folds", "K2O", None))
        self.nfolds_label.setText(_translate("strat_folds", "N folds", None))
        self.test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    strat_folds = QtGui.QGroupBox()
    ui = Ui_strat_folds()
    ui.setupUi(strat_folds)
    strat_folds.show()
    sys.exit(app.exec_())

