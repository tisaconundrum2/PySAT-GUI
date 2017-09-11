# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

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
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.numOfNonZeroCoeffsLabel = QtWidgets.QLabel(self.groupBox)
        self.numOfNonZeroCoeffsLabel.setObjectName("numOfNonZeroCoeffsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numOfNonZeroCoeffsLabel)
        self.numOfNonZeroCoeffsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numOfNonZeroCoeffsSpinBox.setEnabled(False)
        self.numOfNonZeroCoeffsSpinBox.setMaximum(999999999)
        self.numOfNonZeroCoeffsSpinBox.setProperty("value", 615)
        self.numOfNonZeroCoeffsSpinBox.setObjectName("numOfNonZeroCoeffsSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numOfNonZeroCoeffsSpinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.optimizeWCrossValidationLabel = QtWidgets.QLabel(self.groupBox)
        self.optimizeWCrossValidationLabel.setObjectName("optimizeWCrossValidationLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.optimizeWCrossValidationLabel)
        self.optimizeWCrossValidationCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.optimizeWCrossValidationCheckBox.setChecked(True)
        self.optimizeWCrossValidationCheckBox.setObjectName("optimizeWCrossValidationCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.optimizeWCrossValidationCheckBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        self.optimizeWCrossValidationCheckBox.toggled['bool'].connect(self.numOfNonZeroCoeffsSpinBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.numOfNonZeroCoeffsLabel.setText(("# of non-zero coeffs"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.optimizeWCrossValidationLabel.setText(("Optimize w/ Cross Validation (Ignores # of Coeffs)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

