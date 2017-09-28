# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rbanderson\Documents\Projects\LIBS PDART\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\Lasso.ui'
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
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.alphaDoubleSpinBox.setMaximum(999999999.0)
        self.alphaDoubleSpinBox.setProperty("value", 1.0)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupBox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maxNumOfIterationsSpinBox.setMaximum(999999999)
        self.maxNumOfIterationsSpinBox.setProperty("value", 1000)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(self.groupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.forcePositiveCoefficientsLabel = QtWidgets.QLabel(self.groupBox)
        self.forcePositiveCoefficientsLabel.setObjectName("forcePositiveCoefficientsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.forcePositiveCoefficientsLabel)
        self.forcePositiveCoefficientsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.forcePositiveCoefficientsCheckBox.setObjectName("forcePositiveCoefficientsCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.forcePositiveCoefficientsCheckBox)
        self.optimizeWCrossValidaitonLabel = QtWidgets.QLabel(self.groupBox)
        self.optimizeWCrossValidaitonLabel.setObjectName("optimizeWCrossValidaitonLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.optimizeWCrossValidaitonLabel)
        self.optimizeWCrossValidaitonCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.optimizeWCrossValidaitonCheckBox.setChecked(True)
        self.optimizeWCrossValidaitonCheckBox.setObjectName("optimizeWCrossValidaitonCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.optimizeWCrossValidaitonCheckBox)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.toleranceDoubleSpinBox.setDecimals(5)
        self.toleranceDoubleSpinBox.setMaximum(999999999.0)
        self.toleranceDoubleSpinBox.setProperty("value", 0.0001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alphaLabel.setText(_translate("Form", "Alpha"))
        self.maxNumOfIterationsLabel.setText(_translate("Form", "Max # of iterations"))
        self.toleranceLabel.setText(_translate("Form", "Tolerance"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.forcePositiveCoefficientsLabel.setText(_translate("Form", "Force positive coefficients"))
        self.optimizeWCrossValidaitonLabel.setText(_translate("Form", "Optimize w/ Cross Validaiton (Ignores alpha)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

