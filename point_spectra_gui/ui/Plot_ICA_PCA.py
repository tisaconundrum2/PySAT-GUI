# -*- coding: utf-8 -*-

# Form implementation generated from reading util file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\util\util\UI_Plot_ICA_PCA.util'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseMethodLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseMethodLabel.setObjectName("chooseMethodLabel")
        self.gridLayout.addWidget(self.chooseMethodLabel, 1, 0, 1, 1)
        self.chooseXVariableLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseXVariableLabel.setObjectName("chooseXVariableLabel")
        self.gridLayout.addWidget(self.chooseXVariableLabel, 2, 0, 1, 1)
        self.chooseYVariableLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseYVariableLabel.setObjectName("chooseYVariableLabel")
        self.gridLayout.addWidget(self.chooseYVariableLabel, 3, 0, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupbox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.gridLayout.addWidget(self.plotFilenameLabel, 6, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupbox)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.gridLayout.addWidget(self.plotFilenameLineEdit, 6, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupbox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        self.colorCodedVariableLabel = QtWidgets.QLabel(self.groupbox)
        self.colorCodedVariableLabel.setMaximumSize(QtCore.QSize(16777215, 10))
        self.colorCodedVariableLabel.setObjectName("colorCodedVariableLabel")
        self.gridLayout.addWidget(self.colorCodedVariableLabel, 4, 0, 1, 2)
        self.colorCodedVariableComboBox = QtWidgets.QComboBox(self.groupbox)
        self.colorCodedVariableComboBox.setObjectName("colorCodedVariableComboBox")
        self.gridLayout.addWidget(self.colorCodedVariableComboBox, 5, 1, 1, 2)
        self.chooseYVariableComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseYVariableComboBox.setObjectName("chooseYVariableComboBox")
        self.gridLayout.addWidget(self.chooseYVariableComboBox, 3, 1, 1, 2)
        self.chooseXVariableComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseXVariableComboBox.setObjectName("chooseXVariableComboBox")
        self.gridLayout.addWidget(self.chooseXVariableComboBox, 2, 1, 1, 2)
        self.chooseMethodComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseMethodComboBox.setObjectName("chooseMethodComboBox")
        self.gridLayout.addWidget(self.chooseMethodComboBox, 1, 1, 1, 2)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupbox.setTitle(_translate("Form", "Plot ICA/PCA"))
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

