# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\FABC.ui'
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
        self.smoothnessDoubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.smoothnessDoubleSpinBox.setObjectName("smoothnessDoubleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.smoothnessDoubleSpinBox)
        self.dilationLabel = QtWidgets.QLabel(Form)
        self.dilationLabel.setObjectName("dilationLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dilationLabel)
        self.dilationSpinBox = QtWidgets.QSpinBox(Form)
        self.dilationSpinBox.setObjectName("dilationSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dilationSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.smoothnessLabel.setText(_translate("Form", "Smoothness"))
        self.dilationLabel.setText(_translate("Form", "Dilation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

