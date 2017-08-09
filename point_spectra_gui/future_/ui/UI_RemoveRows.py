# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\UI_RemoveRows.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.isLabel = QtWidgets.QLabel(self.groupBox)
        self.isLabel.setMaximumSize(QtCore.QSize(10, 16777215))
        self.isLabel.setObjectName("isLabel")
        self.gridLayout.addWidget(self.isLabel, 1, 2, 1, 1)
        self.removeRowsWhereLabel = QtWidgets.QLabel(self.groupBox)
        self.removeRowsWhereLabel.setObjectName("removeRowsWhereLabel")
        self.gridLayout.addWidget(self.removeRowsWhereLabel, 1, 0, 1, 1)
        self.isComboBox = QtWidgets.QComboBox(self.groupBox)
        self.isComboBox.setObjectName("isComboBox")
        self.gridLayout.addWidget(self.isComboBox, 1, 3, 1, 1)
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.isComboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.isComboBox_2.setObjectName("isComboBox_2")
        self.gridLayout.addWidget(self.isComboBox_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Remove Rows"))
        self.isLabel.setText(_translate("Form", "is "))
        self.removeRowsWhereLabel.setText(_translate("Form", "Remove rows where"))
        self.chooseDataLabel.setText(_translate("Form", "Choose Data:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

