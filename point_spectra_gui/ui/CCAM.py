# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\CCAM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.largestWaveletScaleLabel.setText(_translate("Form", "Largest Wavelet Scale"))
        self.lowestWaveletScaleLabel.setText(_translate("Form", "Lowest Wavelet Scale"))
        self.interpolationMethodLabel.setText(_translate("Form", "Interpolation Method"))
        self.interpolationMethodComboBox.setItemText(0, _translate("Form", "Spline"))
        self.interpolationMethodComboBox.setItemText(1, _translate("Form", "Quadratic"))
        self.interpolationMethodComboBox.setItemText(2, _translate("Form", "Linear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

