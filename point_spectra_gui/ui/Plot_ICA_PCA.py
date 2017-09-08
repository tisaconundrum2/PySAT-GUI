# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\PySAT_Point_Spectra_GUI\ui\Plot_ICA_PCA.ui'
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
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseMethodLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseMethodLabel.setObjectName("chooseMethodLabel")
        self.gridLayout.addWidget(self.chooseMethodLabel, 1, 0, 1, 1)
        self.chooseXVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseXVariableLabel.setObjectName("chooseXVariableLabel")
        self.gridLayout.addWidget(self.chooseXVariableLabel, 2, 0, 1, 1)
        self.chooseYVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseYVariableLabel.setObjectName("chooseYVariableLabel")
        self.gridLayout.addWidget(self.chooseYVariableLabel, 3, 0, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.gridLayout.addWidget(self.plotFilenameLabel, 6, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.gridLayout.addWidget(self.plotFilenameLineEdit, 6, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        self.colorCodedVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.colorCodedVariableLabel.setMaximumSize(QtCore.QSize(16777215, 10))
        self.colorCodedVariableLabel.setObjectName("colorCodedVariableLabel")
        self.gridLayout.addWidget(self.colorCodedVariableLabel, 4, 0, 1, 2)
        self.colorCodedVariableComboBox = QtWidgets.QComboBox(self.groupBox)
        self.colorCodedVariableComboBox.setObjectName("colorCodedVariableComboBox")
        self.gridLayout.addWidget(self.colorCodedVariableComboBox, 5, 1, 1, 2)
        self.chooseYVariableComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseYVariableComboBox.setObjectName("chooseYVariableComboBox")
        self.gridLayout.addWidget(self.chooseYVariableComboBox, 3, 1, 1, 2)
        self.chooseXVariableComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseXVariableComboBox.setObjectName("chooseXVariableComboBox")
        self.gridLayout.addWidget(self.chooseXVariableComboBox, 2, 1, 1, 2)
        self.chooseMethodComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseMethodComboBox.setObjectName("chooseMethodComboBox")
        self.gridLayout.addWidget(self.chooseMethodComboBox, 1, 1, 1, 2)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.chooseDataComboBox, self.chooseMethodComboBox)
        Form.setTabOrder(self.chooseMethodComboBox, self.chooseXVariableComboBox)
        Form.setTabOrder(self.chooseXVariableComboBox, self.chooseYVariableComboBox)
        Form.setTabOrder(self.chooseYVariableComboBox, self.colorCodedVariableComboBox)
        Form.setTabOrder(self.colorCodedVariableComboBox, self.plotFilenameLineEdit)
        Form.setTabOrder(self.plotFilenameLineEdit, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Plot ICA/PCA"))
        self.chooseDataLabel.setText(_translate("Form", "Choose data"))
        self.chooseMethodLabel.setText(_translate("Form", "Choose method"))
        self.chooseXVariableLabel.setText(_translate("Form", "Choose X Variable"))
        self.chooseYVariableLabel.setText(_translate("Form", "Choose Y Variable"))
        self.plotFilenameLabel.setText(_translate("Form", "Plot Filename"))
        self.pushButton.setText(_translate("Form", "..."))
        self.colorCodedVariableLabel.setText(_translate("Form", "Choose variable to color code points (optional)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

