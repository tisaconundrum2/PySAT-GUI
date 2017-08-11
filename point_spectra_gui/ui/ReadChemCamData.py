# -*- coding: utf-8 -*-

# Form implementation generated from reading util file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\util\ReadChemCamData.util'
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
        self.searchStringLabel = QtWidgets.QLabel(self.groupBox)
        self.searchStringLabel.setObjectName("searchStringLabel")
        self.gridLayout.addWidget(self.searchStringLabel, 0, 0, 1, 1)
        self.searchStringLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.searchStringLineEdit.setObjectName("searchStringLineEdit")
        self.gridLayout.addWidget(self.searchStringLineEdit, 0, 1, 1, 1)
        self.searchDirectoryLabel = QtWidgets.QLabel(self.groupBox)
        self.searchDirectoryLabel.setObjectName("searchDirectoryLabel")
        self.gridLayout.addWidget(self.searchDirectoryLabel, 1, 0, 1, 1)
        self.searchDirectoryLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.searchDirectoryLineEdit.setObjectName("searchDirectoryLineEdit")
        self.gridLayout.addWidget(self.searchDirectoryLineEdit, 1, 1, 1, 1)
        self.searchDirectorypushButton = QtWidgets.QPushButton(self.groupBox)
        self.searchDirectorypushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.searchDirectorypushButton.setObjectName("searchDirectorypushButton")
        self.gridLayout.addWidget(self.searchDirectorypushButton, 1, 2, 1, 1)
        self.metadataFileSLabel = QtWidgets.QLabel(self.groupBox)
        self.metadataFileSLabel.setObjectName("metadataFileSLabel")
        self.gridLayout.addWidget(self.metadataFileSLabel, 2, 0, 1, 1)
        self.metadataFileSLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.metadataFileSLineEdit.setObjectName("metadataFileSLineEdit")
        self.gridLayout.addWidget(self.metadataFileSLineEdit, 2, 1, 1, 1)
        self.metadatapushButton = QtWidgets.QPushButton(self.groupBox)
        self.metadatapushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.metadatapushButton.setObjectName("metadatapushButton")
        self.gridLayout.addWidget(self.metadatapushButton, 2, 2, 1, 1)
        self.outputFileNameLabel = QtWidgets.QLabel(self.groupBox)
        self.outputFileNameLabel.setObjectName("outputFileNameLabel")
        self.gridLayout.addWidget(self.outputFileNameLabel, 3, 0, 1, 1)
        self.outputFileNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.outputFileNameLineEdit.setObjectName("outputFileNameLineEdit")
        self.gridLayout.addWidget(self.outputFileNameLineEdit, 3, 1, 1, 1)
        self.averagesLabel = QtWidgets.QLabel(self.groupBox)
        self.averagesLabel.setObjectName("averagesLabel")
        self.gridLayout.addWidget(self.averagesLabel, 4, 0, 1, 1)
        self.averagesradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.averagesradioButton.setText("")
        self.averagesradioButton.setChecked(True)
        self.averagesradioButton.setObjectName("averagesradioButton")
        self.gridLayout.addWidget(self.averagesradioButton, 4, 1, 1, 1)
        self.singleShotsLabel = QtWidgets.QLabel(self.groupBox)
        self.singleShotsLabel.setObjectName("singleShotsLabel")
        self.gridLayout.addWidget(self.singleShotsLabel, 5, 0, 1, 1)
        self.singleShotsradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.singleShotsradioButton.setText("")
        self.singleShotsradioButton.setObjectName("singleShotsradioButton")
        self.gridLayout.addWidget(self.singleShotsradioButton, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Read ChemCam Data"))
        self.searchStringLabel.setText(_translate("Form", "Search String:"))
        self.searchDirectoryLabel.setText(_translate("Form", "Search directory:"))
        self.searchDirectorypushButton.setText(_translate("Form", "..."))
        self.metadataFileSLabel.setText(_translate("Form", "Metadata file(s):"))
        self.metadatapushButton.setText(_translate("Form", "..."))
        self.outputFileNameLabel.setText(_translate("Form", "Output file name:"))
        self.averagesLabel.setText(_translate("Form", "Averages"))
        self.singleShotsLabel.setText(_translate("Form", "Single Shots"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

