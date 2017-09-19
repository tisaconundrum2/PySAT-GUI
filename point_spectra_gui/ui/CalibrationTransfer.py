# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\CalibrationTransfer.ui'
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
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.CalTran_dataSetRefLabel = QtWidgets.QLabel(self.formGroupBox)
        self.CalTran_dataSetRefLabel.setObjectName("CalTran_dataSetRefLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetRefLabel)
        self.CalTran_dataSetRefLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.CalTran_dataSetRefLineEdit.setObjectName("CalTran_dataSetRefLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetRefLineEdit)
        self.CalTran_dataSetTransformLabel = QtWidgets.QLabel(self.formGroupBox)
        self.CalTran_dataSetTransformLabel.setObjectName("CalTran_dataSetTransformLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetTransformLabel)
        self.CalTran_dataSetTransformLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.CalTran_dataSetTransformLineEdit.setObjectName("CalTran_dataSetTransformLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetTransformLineEdit)
        self.CalTran_columnToMatchLabel = QtWidgets.QLabel(self.formGroupBox)
        self.CalTran_columnToMatchLabel.setObjectName("CalTran_columnToMatchLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CalTran_columnToMatchLabel)
        self.CalTran_columnToMatchComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.CalTran_columnToMatchComboBox.setObjectName("CalTran_columnToMatchComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CalTran_columnToMatchComboBox)
        self.methodLabel = QtWidgets.QLabel(self.formGroupBox)
        self.methodLabel.setObjectName("methodLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.methodLabel)
        self.methodComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.methodComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "Calibration Transfer"))
        self.CalTran_dataSetRefLabel.setText(_translate("Form", "Reference Data Set:"))
        self.CalTran_dataSetTransformLabel.setText(_translate("Form", "Data Set to Transform:"))
        self.CalTran_columnToMatchLabel.setText(_translate("Form", "Column to Match:"))
        self.methodLabel.setText(_translate("Form", "Method:"))
        self.methodComboBox.setItemText(0, _translate("Form", "LRA - Low Rank Alignment"))
        self.methodComboBox.setItemText(1, _translate("Form", "PDS - Piecewise Direct Standardization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

