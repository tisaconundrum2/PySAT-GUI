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
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.topWidthLabel = QtWidgets.QLabel(Form)
        self.topWidthLabel.setObjectName("topWidthLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.topWidthLabel)
        self.topWidthSpinBox = QtWidgets.QSpinBox(Form)
        self.topWidthSpinBox.setObjectName("topWidthSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.topWidthSpinBox)
        self.bottomWidthLabel = QtWidgets.QLabel(Form)
        self.bottomWidthLabel.setObjectName("bottomWidthLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bottomWidthLabel)
        self.bottomWidthSpinBox = QtWidgets.QSpinBox(Form)
        self.bottomWidthSpinBox.setObjectName("bottomWidthSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bottomWidthSpinBox)
        self.exponentLabel = QtWidgets.QLabel(Form)
        self.exponentLabel.setObjectName("exponentLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.exponentLabel)
        self.exponentSpinBox = QtWidgets.QSpinBox(Form)
        self.exponentSpinBox.setObjectName("exponentSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.exponentSpinBox)
        self.tangentLabel = QtWidgets.QLabel(Form)
        self.tangentLabel.setObjectName("tangentLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tangentLabel)
        self.tangentCheckBox = QtWidgets.QCheckBox(Form)
        self.tangentCheckBox.setObjectName("tangentCheckBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tangentCheckBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("Form"))
        self.topWidthLabel.setText(_("Top Width"))
        self.bottomWidthLabel.setText(_("Bottom Width"))
        self.exponentLabel.setText(_("Exponent"))
        self.tangentLabel.setText(_("Tangent"))

