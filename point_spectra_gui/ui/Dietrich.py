# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\Dietrich.ui'
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
        self.formLayout_2.setObjectName("formLayout_2")
        self.halfWindowLabel = QtWidgets.QLabel(Form)
        self.halfWindowLabel.setObjectName("halfWindowLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.halfWindowLabel)
        self.halfWindowSpinBox = QtWidgets.QSpinBox(Form)
        self.halfWindowSpinBox.setObjectName("halfWindowSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.halfWindowSpinBox)
        self.numOfErosionsLabel = QtWidgets.QLabel(Form)
        self.numOfErosionsLabel.setObjectName("numOfErosionsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfErosionsLabel)
        self.numOfErosionsSpinBox = QtWidgets.QSpinBox(Form)
        self.numOfErosionsSpinBox.setObjectName("numOfErosionsSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfErosionsSpinBox)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.halfWindowLabel.setText(_translate("Form", "Half Window:"))
        self.numOfErosionsLabel.setText(_translate("Form", "Num of Erosions:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

