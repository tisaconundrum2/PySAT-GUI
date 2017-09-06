# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\Mario.ui'
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.polynomialOrderLabel.setText(_translate("Form", "Polynomial Order"))
        self.maximumNumOfIterationsLabel.setText(_translate("Form", "Maximum num of Iterations"))
        self.toleranceLabel.setText(_translate("Form", "Tolerance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

