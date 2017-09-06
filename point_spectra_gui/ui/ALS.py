# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\ALS.ui'
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
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.asymmetryLabel = QtWidgets.QLabel(Form)
        self.asymmetryLabel.setObjectName("asymmetryLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.asymmetryLabel)
        self.asymmetryDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.asymmetryDoubleSpinBox.setObjectName("asymmetryDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.asymmetryDoubleSpinBox)
        self.smoothnessLabel = QtWidgets.QLabel(Form)
        self.smoothnessLabel.setObjectName("smoothnessLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.smoothnessLabel)
        self.smoothnessDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.smoothnessDoubleSpinBox.setObjectName("smoothnessDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.smoothnessDoubleSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(Form)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(Form)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.convergenceThresholdLabel = QtWidgets.QLabel(Form)
        self.convergenceThresholdLabel.setObjectName("convergenceThresholdLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.convergenceThresholdLabel)
        self.convergenceThresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.convergenceThresholdDoubleSpinBox.setObjectName("convergenceThresholdDoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.convergenceThresholdDoubleSpinBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.asymmetryLabel.setText(_translate("Form", "Asymmetry"))
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

