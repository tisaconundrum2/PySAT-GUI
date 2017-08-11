# -*- coding: utf-8 -*-

# Form implementation generated from reading util file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\util\OMP.util'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.numOfNonZeroCoeffsLabel = QtWidgets.QLabel(self.groupBox)
        self.numOfNonZeroCoeffsLabel.setObjectName("numOfNonZeroCoeffsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numOfNonZeroCoeffsLabel)
        self.numOfNonZeroCoeffsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numOfNonZeroCoeffsSpinBox.setEnabled(False)
        self.numOfNonZeroCoeffsSpinBox.setMaximum(999999999)
        self.numOfNonZeroCoeffsSpinBox.setProperty("value", 615)
        self.numOfNonZeroCoeffsSpinBox.setObjectName("numOfNonZeroCoeffsSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numOfNonZeroCoeffsSpinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.optimizeWCrossValidationLabel = QtWidgets.QLabel(self.groupBox)
        self.optimizeWCrossValidationLabel.setObjectName("optimizeWCrossValidationLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.optimizeWCrossValidationLabel)
        self.optimizeWCrossValidationCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.optimizeWCrossValidationCheckBox.setChecked(True)
        self.optimizeWCrossValidationCheckBox.setObjectName("optimizeWCrossValidationCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.optimizeWCrossValidationCheckBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        self.optimizeWCrossValidationCheckBox.toggled['bool'].connect(self.numOfNonZeroCoeffsSpinBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numOfNonZeroCoeffsLabel.setText(_translate("Form", "# of non-zero coeffs"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.optimizeWCrossValidationLabel.setText(_translate("Form", "Optimize w/ Cross Validation (Ignores # of Coeffs)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

