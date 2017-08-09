# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\UI_SplitDataset.ui'
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
        self.chooseDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDataComboBox)
        self.splitOnUniqueValuesOfLabel = QtWidgets.QLabel(self.formGroupBox)
        self.splitOnUniqueValuesOfLabel.setObjectName("splitOnUniqueValuesOfLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.splitOnUniqueValuesOfLabel)
        self.splitOnUniqueValuesOfComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.splitOnUniqueValuesOfComboBox.setObjectName("splitOnUniqueValuesOfComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.splitOnUniqueValuesOfComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "Split Dataset"))
        self.chooseDataLabel.setText(_translate("Form", "Choose Data"))
        self.splitOnUniqueValuesOfLabel.setText(_translate("Form", "Split on unique values of"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

