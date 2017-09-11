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
        self.smoothnessLabel = QtWidgets.QLabel(Form)
        self.smoothnessLabel.setObjectName("smoothnessLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.smoothnessLabel)
        self.smoothnessDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.smoothnessDoubleSpinBox.setObjectName("smoothnessDoubleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.smoothnessDoubleSpinBox)
        self.dilationLabel = QtWidgets.QLabel(Form)
        self.dilationLabel.setObjectName("dilationLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dilationLabel)
        self.dilationSpinBox = QtWidgets.QSpinBox(Form)
        self.dilationSpinBox.setObjectName("dilationSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dilationSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.smoothnessLabel.setText(("Smoothness"))
        self.dilationLabel.setText(("Dilation"))

