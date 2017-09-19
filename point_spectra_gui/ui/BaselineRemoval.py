# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\BaselineRemoval.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.formGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.chooseAlgorithmLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseAlgorithmLabel.setObjectName("chooseAlgorithmLabel")
        self.gridLayout.addWidget(self.chooseAlgorithmLabel, 1, 0, 1, 1)
        self.chooseAlgorithmComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseAlgorithmComboBox.setObjectName("chooseAlgorithmComboBox")
        self.gridLayout.addWidget(self.chooseAlgorithmComboBox, 1, 1, 1, 1)
        self.algorithmLayout = QtWidgets.QVBoxLayout()
        self.algorithmLayout.setObjectName("algorithmLayout")
        self.gridLayout.addLayout(self.algorithmLayout, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "Baseline Removal"))
        self.chooseDataLabel.setText(_translate("Form", "Choose data"))
        self.chooseAlgorithmLabel.setText(_translate("Form", "Choose algorithm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

