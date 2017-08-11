# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\PLS.ui'
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
        self.numOfComponentsLabel = QtWidgets.QLabel(self.groupBox)
        self.numOfComponentsLabel.setObjectName("numOfComponentsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numOfComponentsLabel)
        self.numOfComponentsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numOfComponentsSpinBox.setObjectName("numOfComponentsSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numOfComponentsSpinBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numOfComponentsLabel.setText(_translate("Form", "num of components"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

