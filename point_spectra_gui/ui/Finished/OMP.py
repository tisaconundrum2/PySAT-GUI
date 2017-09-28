


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
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
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))


    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

