# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\Documents\GitHub\PYSAT\src\New PYSAT_Gui\mainwindow.ui'
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

class setup(object):
    def setupUi(self, MainWindow):
        self.CrossValidation = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CrossValidation.setFont(font)
        self.CrossValidation.setObjectName(_fromUtf8("CrossValidation"))
        self.CrossValid = QtGui.QVBoxLayout(self.CrossValidation)
        self.CrossValid.setMargin(11)
        self.CrossValid.setSpacing(6)
        self.CrossValid.setObjectName(_fromUtf8("CrossValid"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setMargin(11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_14 = QtGui.QLabel(self.CrossValidation)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_11.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.CrossValidation)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_11.addWidget(self.label_15)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setMargin(11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.elementNameLine = QtGui.QLineEdit(self.CrossValidation)
        self.elementNameLine.setObjectName(_fromUtf8("elementNameLine"))
        self.verticalLayout_12.addWidget(self.elementNameLine)
        self.nfolds_test = QtGui.QSpinBox(self.CrossValidation)
        self.nfolds_test.setObjectName(_fromUtf8("nfolds_test"))
        self.verticalLayout_12.addWidget(self.nfolds_test)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.CrossValid.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addWidget(self.CrossValidation)
        self.CrossValidation.setTitle(_translate("MainWindow", "Setup", None))
        self.label_14.setText(_translate("MainWindow", "Element Name", None))
        self.label_15.setText(_translate("MainWindow", "nfolds_test", None))
