# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\WriteToCSV.ui'
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
        self.chooseDataSetLabel = QtWidgets.QLabel(Form)
        self.chooseDataSetLabel.setObjectName("chooseDataSetLabel")
        self.verticalLayout.addWidget(self.chooseDataSetLabel)
        self.chooseDataSetComboBox = QtWidgets.QComboBox(Form)
        self.chooseDataSetComboBox.setObjectName("chooseDataSetComboBox")
        self.verticalLayout.addWidget(self.chooseDataSetComboBox)
        self.variablesToWriteLabel = QtWidgets.QLabel(Form)
        self.variablesToWriteLabel.setObjectName("variablesToWriteLabel")
        self.verticalLayout.addWidget(self.variablesToWriteLabel)
        self.variablesToWriteListWidget = QtWidgets.QListWidget(Form)
        self.variablesToWriteListWidget.setObjectName("variablesToWriteListWidget")
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        self.verticalLayout.addWidget(self.variablesToWriteListWidget)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chooseDataSetLabel.setText(_translate("Form", "Choose data set to write to *.csv"))
        self.variablesToWriteLabel.setText(_translate("Form", "Variables to write:"))
        __sortingEnabled = self.variablesToWriteListWidget.isSortingEnabled()
        self.variablesToWriteListWidget.setSortingEnabled(False)
        item = self.variablesToWriteListWidget.item(0)
        item.setText(_translate("Form", "comp"))
        item = self.variablesToWriteListWidget.item(1)
        item.setText(_translate("Form", "meta"))
        item = self.variablesToWriteListWidget.item(2)
        item.setText(_translate("Form", "wvl"))
        self.variablesToWriteListWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "Specify a filename:"))
        self.lineEdit.setText(_translate("Form", "output.csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

