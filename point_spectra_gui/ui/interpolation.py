# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\interpolation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.interpolateDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.interpolateDataLabel.setObjectName("interpolateDataLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.interpolateDataLabel)
        self.interpolateDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.interpolateDataComboBox.setObjectName("interpolateDataComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.interpolateDataComboBox)
        self.referenceDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.referenceDataLabel.setObjectName("referenceDataLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.referenceDataLabel)
        self.referenceDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.referenceDataComboBox.setObjectName("referenceDataComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.referenceDataComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "Interpolation"))
        self.interpolateDataLabel.setText(_translate("Form", "Choose data to interpolate"))
        self.referenceDataLabel.setText(_translate("Form", "Choose data to use as reference"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

