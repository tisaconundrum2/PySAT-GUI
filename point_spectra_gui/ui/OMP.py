# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\OMP.ui'
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
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.cVLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cVLabel.setObjectName("cVLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cVLabel)
        self.cVCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.cVCheckBox.setObjectName("cVCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cVCheckBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.normalizeLabel.setText(_translate("Form", "Normalize"))
        self.precomputeLabel.setText(_translate("Form", "Precompute"))
        self.precomputeComboBox.setItemText(0, _translate("Form", "auto"))
        self.precomputeComboBox.setItemText(1, _translate("Form", "True"))
        self.precomputeComboBox.setItemText(2, _translate("Form", "False"))
        self.cVLabel.setText(_translate("Form", "CV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

