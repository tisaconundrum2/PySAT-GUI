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
        self.largestWaveletScaleLabel = QtWidgets.QLabel(Form)
        self.largestWaveletScaleLabel.setObjectName("largestWaveletScaleLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.largestWaveletScaleLabel)
        self.largestWaveletScaleSpinBox = QtWidgets.QSpinBox(Form)
        self.largestWaveletScaleSpinBox.setObjectName("largestWaveletScaleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.largestWaveletScaleSpinBox)
        self.lowestWaveletScaleLabel = QtWidgets.QLabel(Form)
        self.lowestWaveletScaleLabel.setObjectName("lowestWaveletScaleLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lowestWaveletScaleLabel)
        self.lowestWaveletScaleSpinBox = QtWidgets.QSpinBox(Form)
        self.lowestWaveletScaleSpinBox.setObjectName("lowestWaveletScaleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lowestWaveletScaleSpinBox)
        self.interpolationMethodLabel = QtWidgets.QLabel(Form)
        self.interpolationMethodLabel.setObjectName("interpolationMethodLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.interpolationMethodLabel)
        self.interpolationMethodComboBox = QtWidgets.QComboBox(Form)
        self.interpolationMethodComboBox.setObjectName("interpolationMethodComboBox")
        self.interpolationMethodComboBox.addItem("")
        self.interpolationMethodComboBox.addItem("")
        self.interpolationMethodComboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interpolationMethodComboBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("Form"))
        self.largestWaveletScaleLabel.setText(_("Largest Wavelet Scale"))
        self.lowestWaveletScaleLabel.setText(_("Lowest Wavelet Scale"))
        self.interpolationMethodLabel.setText(_("Interpolation Method"))
        self.interpolationMethodComboBox.setItemText(0, _("Spline"))
        self.interpolationMethodComboBox.setItemText(1, _("Quadratic"))
        self.interpolationMethodComboBox.setItemText(2, _("Linear"))

