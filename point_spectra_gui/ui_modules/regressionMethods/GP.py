# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\GP.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.chooseDimensionalityReductionMethodLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDimensionalityReductionMethodLabel.setObjectName("chooseDimensionalityReductionMethodLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDimensionalityReductionMethodLabel)
        self.chooseDimensionalityReductionMethodComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDimensionalityReductionMethodComboBox.setObjectName("chooseDimensionalityReductionMethodComboBox")
        self.chooseDimensionalityReductionMethodComboBox.addItem("")
        self.chooseDimensionalityReductionMethodComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDimensionalityReductionMethodComboBox)
        self.numOfComponentsLabel = QtWidgets.QLabel(self.groupBox)
        self.numOfComponentsLabel.setObjectName("numOfComponentsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfComponentsLabel)
        self.numOfComponentsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numOfComponentsSpinBox.setObjectName("numOfComponentsSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfComponentsSpinBox)
        self.numOfRandomStartsLabel = QtWidgets.QLabel(self.groupBox)
        self.numOfRandomStartsLabel.setObjectName("numOfRandomStartsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numOfRandomStartsLabel)
        self.numOfRandomStartsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numOfRandomStartsSpinBox.setMaximum(999999999)
        self.numOfRandomStartsSpinBox.setProperty("value", 1)
        self.numOfRandomStartsSpinBox.setObjectName("numOfRandomStartsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numOfRandomStartsSpinBox)
        self.startingThetaLabel = QtWidgets.QLabel(self.groupBox)
        self.startingThetaLabel.setObjectName("startingThetaLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.startingThetaLabel)
        self.startingThetaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.startingThetaDoubleSpinBox.setMaximum(999999999.0)
        self.startingThetaDoubleSpinBox.setProperty("value", 1.0)
        self.startingThetaDoubleSpinBox.setObjectName("startingThetaDoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.startingThetaDoubleSpinBox)
        self.lowerBoundOnThetaLabel = QtWidgets.QLabel(self.groupBox)
        self.lowerBoundOnThetaLabel.setObjectName("lowerBoundOnThetaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lowerBoundOnThetaLabel)
        self.lowerBoundOnThetaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.lowerBoundOnThetaDoubleSpinBox.setSingleStep(0.01)
        self.lowerBoundOnThetaDoubleSpinBox.setProperty("value", 0.1)
        self.lowerBoundOnThetaDoubleSpinBox.setObjectName("lowerBoundOnThetaDoubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lowerBoundOnThetaDoubleSpinBox)
        self.upperBoundOnThetaLabel = QtWidgets.QLabel(self.groupBox)
        self.upperBoundOnThetaLabel.setObjectName("upperBoundOnThetaLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.upperBoundOnThetaLabel)
        self.upperBoundOnThetaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.upperBoundOnThetaDoubleSpinBox.setMaximum(9999.0)
        self.upperBoundOnThetaDoubleSpinBox.setProperty("value", 100.0)
        self.upperBoundOnThetaDoubleSpinBox.setObjectName("upperBoundOnThetaDoubleSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.upperBoundOnThetaDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chooseDimensionalityReductionMethodLabel.setText(
            _translate("Form", "Choose dimensionality reduction method:"))
        self.chooseDimensionalityReductionMethodComboBox.setItemText(0, _translate("Form", "PCA"))
        self.chooseDimensionalityReductionMethodComboBox.setItemText(1, _translate("Form", "ICA"))
        self.numOfComponentsLabel.setText(_translate("Form", "# of components"))
        self.numOfRandomStartsLabel.setText(_translate("Form", "# of random starts"))
        self.startingThetaLabel.setText(_translate("Form", "Starting Theta"))
        self.lowerBoundOnThetaLabel.setText(_translate("Form", "Lower bound on Theta"))
        self.upperBoundOnThetaLabel.setText(_translate("Form", "Upper bound on theta"))
