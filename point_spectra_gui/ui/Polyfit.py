# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\Polyfit.ui'
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
        self.orderLabel = QtWidgets.QLabel(self.groupbox)
        self.orderLabel.setObjectName("orderLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.orderLabel)
        self.orderSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.orderSpinBox.setObjectName("orderSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.orderSpinBox)
        self.numOfStandardDeviationsLabel = QtWidgets.QLabel(self.groupbox)
        self.numOfStandardDeviationsLabel.setObjectName("numOfStandardDeviationsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfStandardDeviationsLabel)
        self.numOfStandardDeviationsSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.numOfStandardDeviationsSpinBox.setObjectName("numOfStandardDeviationsSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfStandardDeviationsSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupbox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.orderLabel.setText(_translate("Form", "Order"))
        self.numOfStandardDeviationsLabel.setText(_translate("Form", "Num of Standard Deviations"))
        self.maxNumOfIterationsLabel.setText(_translate("Form", "Max Num of Iterations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

