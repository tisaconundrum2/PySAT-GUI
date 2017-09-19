# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\KK.ui'
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
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupbox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.topWidthLabel = QtWidgets.QLabel(self.groupbox)
        self.topWidthLabel.setObjectName("topWidthLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.topWidthLabel)
        self.topWidthSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.topWidthSpinBox.setObjectName("topWidthSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.topWidthSpinBox)
        self.bottomWidthLabel = QtWidgets.QLabel(self.groupbox)
        self.bottomWidthLabel.setObjectName("bottomWidthLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bottomWidthLabel)
        self.bottomWidthSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.bottomWidthSpinBox.setObjectName("bottomWidthSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bottomWidthSpinBox)
        self.exponentLabel = QtWidgets.QLabel(self.groupbox)
        self.exponentLabel.setObjectName("exponentLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.exponentLabel)
        self.exponentSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.exponentSpinBox.setObjectName("exponentSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.exponentSpinBox)
        self.tangentLabel = QtWidgets.QLabel(self.groupbox)
        self.tangentLabel.setObjectName("tangentLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tangentLabel)
        self.tangentCheckBox = QtWidgets.QCheckBox(self.groupbox)
        self.tangentCheckBox.setObjectName("tangentCheckBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tangentCheckBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.topWidthLabel.setText(_translate("Form", "Top Width"))
        self.bottomWidthLabel.setText(_translate("Form", "Bottom Width"))
        self.exponentLabel.setText(_translate("Form", "Exponent"))
        self.tangentLabel.setText(_translate("Form", "Tangent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

