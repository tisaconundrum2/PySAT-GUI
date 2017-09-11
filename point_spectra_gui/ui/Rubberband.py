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
        self.windowSizeLabel = QtWidgets.QLabel(Form)
        self.windowSizeLabel.setObjectName("windowSizeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.windowSizeLabel)
        self.windowSizeSpinBox = QtWidgets.QSpinBox(Form)
        self.windowSizeSpinBox.setObjectName("windowSizeSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.windowSizeSpinBox)
        self.numOfRangesLabel = QtWidgets.QLabel(Form)
        self.numOfRangesLabel.setObjectName("numOfRangesLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfRangesLabel)
        self.numOfRangesSpinBox = QtWidgets.QSpinBox(Form)
        self.numOfRangesSpinBox.setObjectName("numOfRangesSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfRangesSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.windowSizeLabel.setText(("Window Size"))
        self.numOfRangesLabel.setText(("Num of Ranges"))

