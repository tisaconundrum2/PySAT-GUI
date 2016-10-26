# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_submodel.ui'
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

class Ui_submodel(object):
    def setupUi(self, submodel):
        submodel.setObjectName(_fromUtf8("submodel"))
        submodel.resize(644, 238)
        submodel.setMinimumSize(QtCore.QSize(600, 150))
        submodel.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtGui.QVBoxLayout(submodel)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.submodel_vlayout = QtGui.QVBoxLayout()
        self.submodel_vlayout.setObjectName(_fromUtf8("submodel_vlayout"))
        self.submodel_choosedata_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosedata_hlayout.setObjectName(_fromUtf8("submodel_choosedata_hlayout"))
        self.submodel_choosedata = QtGui.QComboBox(submodel)
        self.submodel_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosedata.setObjectName(_fromUtf8("submodel_choosedata"))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata_hlayout.addWidget(self.submodel_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosedata_hlayout.addItem(spacerItem)
        self.submodel_vlayout.addLayout(self.submodel_choosedata_hlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(submodel)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(submodel)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(submodel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(submodel)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.submodel_vlayout.addLayout(self.horizontalLayout)
        self.submodel_choosealg_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosealg_hlayout.setObjectName(_fromUtf8("submodel_choosealg_hlayout"))
        self.submodel_choosealg = QtGui.QComboBox(submodel)
        self.submodel_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosealg.setObjectName(_fromUtf8("submodel_choosealg"))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg_hlayout.addWidget(self.submodel_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosealg_hlayout.addItem(spacerItem2)
        self.submodel_vlayout.addLayout(self.submodel_choosealg_hlayout)
        self.regression_ransac_checkbox = QtGui.QCheckBox(submodel)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.submodel_vlayout.addWidget(self.regression_ransac_checkbox)
        self.submodel_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.submodel_trainbutton_hlayout.setObjectName(_fromUtf8("submodel_trainbutton_hlayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_trainbutton_hlayout.addItem(spacerItem3)
        self.submodel_trainbutton = QtGui.QPushButton(submodel)
        self.submodel_trainbutton.setObjectName(_fromUtf8("submodel_trainbutton"))
        self.submodel_trainbutton_hlayout.addWidget(self.submodel_trainbutton)
        self.submodel_vlayout.addLayout(self.submodel_trainbutton_hlayout)
        self.verticalLayout_2.addLayout(self.submodel_vlayout)

        self.retranslateUi(submodel)
        QtCore.QMetaObject.connectSlotsByName(submodel)

    def retranslateUi(self, submodel):
        submodel.setWindowTitle(_translate("submodel", "Regression", None))
        submodel.setTitle(_translate("submodel", "Regression", None))
        self.submodel_choosedata.setItemText(0, _translate("submodel", "Choose Data", None))
        self.submodel_choosedata.setItemText(1, _translate("submodel", "Known Data", None))
        self.label.setText(_translate("submodel", "Min", None))
        self.label_2.setText(_translate("submodel", "Max", None))
        self.submodel_choosealg.setItemText(0, _translate("submodel", "Choose Algorithm", None))
        self.submodel_choosealg.setItemText(1, _translate("submodel", "PLS", None))
        self.submodel_choosealg.setItemText(2, _translate("submodel", "GP", None))
        self.submodel_choosealg.setItemText(3, _translate("submodel", "Others coming soon...", None))
        self.regression_ransac_checkbox.setText(_translate("submodel", "RANSAC", None))
        self.submodel_trainbutton.setText(_translate("submodel", "Train Submodels", None))

