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
        self.polynomialOrderLabel = QtWidgets.QLabel(Form)
        self.polynomialOrderLabel.setObjectName("polynomialOrderLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.polynomialOrderLabel)
        self.polynomialOrderSpinBox = QtWidgets.QSpinBox(Form)
        self.polynomialOrderSpinBox.setObjectName("polynomialOrderSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.polynomialOrderSpinBox)
        self.maximumNumOfIterationsLabel = QtWidgets.QLabel(Form)
        self.maximumNumOfIterationsLabel.setObjectName("maximumNumOfIterationsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maximumNumOfIterationsLabel)
        self.maximumNumOfIterationsDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.maximumNumOfIterationsDoubleSpinBox.setObjectName("maximumNumOfIterationsDoubleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maximumNumOfIterationsDoubleSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(Form)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.polynomialOrderLabel.setText(("Polynomial Order"))
        self.maximumNumOfIterationsLabel.setText(("Maximum num of Iterations"))
        self.toleranceLabel.setText(("Tolerance"))

