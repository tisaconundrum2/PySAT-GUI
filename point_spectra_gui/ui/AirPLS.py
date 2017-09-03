# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\AirPLS.ui'
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
        self.smoothnessLabel = QtWidgets.QLabel(Form)
        self.smoothnessLabel.setObjectName("smoothnessLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.smoothnessLabel)
        self.smoothnessSpinBox = QtWidgets.QSpinBox(Form)
        self.smoothnessSpinBox.setObjectName("smoothnessSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.smoothnessSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(Form)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(Form)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.convergenceThresholdLabel = QtWidgets.QLabel(Form)
        self.convergenceThresholdLabel.setObjectName("convergenceThresholdLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.convergenceThresholdLabel)
        self.convergenceThresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.convergenceThresholdDoubleSpinBox.setObjectName("convergenceThresholdDoubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.convergenceThresholdDoubleSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.smoothnessLabel.setText(_translate("Form", "Smoothness"))
        self.maxNumOfIterationsLabel.setText(_translate("Form", "Max Num of Iterations"))
        self.convergenceThresholdLabel.setText(_translate("Form", "Convergence Threshold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

