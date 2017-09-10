# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.halfWindowLabel = QtWidgets.QLabel(Form)
        self.halfWindowLabel.setObjectName("halfWindowLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.halfWindowLabel)
        self.halfWindowSpinBox = QtWidgets.QSpinBox(Form)
        self.halfWindowSpinBox.setObjectName("halfWindowSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.halfWindowSpinBox)
        self.numOfErosionsLabel = QtWidgets.QLabel(Form)
        self.numOfErosionsLabel.setObjectName("numOfErosionsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfErosionsLabel)
        self.numOfErosionsSpinBox = QtWidgets.QSpinBox(Form)
        self.numOfErosionsSpinBox.setObjectName("numOfErosionsSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfErosionsSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("Form"))
        self.halfWindowLabel.setText(_("Half Window:"))
        self.numOfErosionsLabel.setText(_("Num of Erosions:"))

