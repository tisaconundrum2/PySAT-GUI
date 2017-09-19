# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\LoadData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadData(object):
    def setupUi(self, loadData):
        loadData.setObjectName("loadData")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loadData.sizePolicy().hasHeightForWidth())
        loadData.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(loadData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(loadData)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.groupBox)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.gridLayout.addWidget(self.fileNameLineEdit, 0, 1, 1, 1)
        self.newFilePushButton = QtWidgets.QPushButton(self.groupBox)
        self.newFilePushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.newFilePushButton.setObjectName("newFilePushButton")
        self.gridLayout.addWidget(self.newFilePushButton, 0, 2, 1, 1)
        self.dataSetNameLabel = QtWidgets.QLabel(self.groupBox)
        self.dataSetNameLabel.setObjectName("dataSetNameLabel")
        self.gridLayout.addWidget(self.dataSetNameLabel, 1, 0, 1, 1)
        self.dataSetNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.dataSetNameLineEdit.setObjectName("dataSetNameLineEdit")
        self.gridLayout.addWidget(self.dataSetNameLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(loadData)
        QtCore.QMetaObject.connectSlotsByName(loadData)

    def retranslateUi(self, loadData):
        _translate = QtCore.QCoreApplication.translate
        loadData.setWindowTitle(_translate("loadData", "Form"))
        self.groupBox.setTitle(_translate("loadData", "Load Data"))
        self.fileNameLabel.setText(_translate("loadData", "File Name"))
        self.fileNameLineEdit.setText(_translate("loadData", "*.csv"))
        self.newFilePushButton.setText(_translate("loadData", "..."))
        self.dataSetNameLabel.setText(_translate("loadData", "Data Set Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loadData = QtWidgets.QWidget()
    ui = Ui_loadData()
    ui.setupUi(loadData)
    loadData.show()
    sys.exit(app.exec_())

