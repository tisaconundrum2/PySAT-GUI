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
        self.vboxlayout = QtWidgets.QVBoxLayout(Form)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(self.groupbox)
        self.formGroupBox.setEnabled(False)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.alphaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.alphaDoubleSpinBox.setProperty("value", 1.0)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.copyXLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copyXLabel.setObjectName("copyXLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.copyXLabel)
        self.copyXCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copyXCheckBox.setChecked(True)
        self.copyXCheckBox.setObjectName("copyXCheckBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.copyXCheckBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationslineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.maxNumOfIterationslineEdit.setObjectName("maxNumOfIterationslineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationslineEdit)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.solverLabel = QtWidgets.QLabel(self.formGroupBox)
        self.solverLabel.setObjectName("solverLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.solverLabel)
        self.solverComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.solverComboBox.setObjectName("solverComboBox")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.solverComboBox)
        self.toleranceLabel = QtWidgets.QLabel(self.formGroupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.randomStateLabel = QtWidgets.QLabel(self.formGroupBox)
        self.randomStateLabel.setObjectName("randomStateLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.randomStateLabel)
        self.randomStateLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.randomStateLineEdit.setObjectName("randomStateLineEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.randomStateLineEdit)
        self.verticalLayout.addWidget(self.formGroupBox)
        self.formGroupBox_CV = QtWidgets.QGroupBox(self.groupbox)
        self.formGroupBox_CV.setObjectName("formGroupBox_CV")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formGroupBox_CV)
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.alphasLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.alphasLabel_cv.setObjectName("alphasLabel_cv")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphasLabel_cv)
        self.alphasLineEdit_cv = QtWidgets.QLineEdit(self.formGroupBox_CV)
        self.alphasLineEdit_cv.setObjectName("alphasLineEdit_cv")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphasLineEdit_cv)
        self.fitInterceptLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.fitInterceptLabel_cv.setObjectName("fitInterceptLabel_cv")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel_cv)
        self.fitInterceptCheckBox_cv = QtWidgets.QCheckBox(self.formGroupBox_CV)
        self.fitInterceptCheckBox_cv.setChecked(True)
        self.fitInterceptCheckBox_cv.setObjectName("fitInterceptCheckBox_cv")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox_cv)
        self.normalizeLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.normalizeLabel_cv.setObjectName("normalizeLabel_cv")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel_cv)
        self.normalizeCheckBox_cv = QtWidgets.QCheckBox(self.formGroupBox_CV)
        self.normalizeCheckBox_cv.setObjectName("normalizeCheckBox_cv")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox_cv)
        self.scoringLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.scoringLabel_cv.setObjectName("scoringLabel_cv")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.scoringLabel_cv)
        self.scoringComboBox_cv = QtWidgets.QComboBox(self.formGroupBox_CV)
        self.scoringComboBox_cv.setObjectName("scoringComboBox_cv")
        self.scoringComboBox_cv.addItem("")
        self.scoringComboBox_cv.addItem("")
        self.scoringComboBox_cv.addItem("")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.scoringComboBox_cv)
        self.gCVModeLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.gCVModeLabel_cv.setObjectName("gCVModeLabel_cv")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gCVModeLabel_cv)
        self.gCVModeComboBox_cv = QtWidgets.QComboBox(self.formGroupBox_CV)
        self.gCVModeComboBox_cv.setObjectName("gCVModeComboBox_cv")
        self.gCVModeComboBox_cv.addItem("")
        self.gCVModeComboBox_cv.addItem("")
        self.gCVModeComboBox_cv.addItem("")
        self.gCVModeComboBox_cv.addItem("")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gCVModeComboBox_cv)
        self.storeCVValuesLabel_cv = QtWidgets.QLabel(self.formGroupBox_CV)
        self.storeCVValuesLabel_cv.setObjectName("storeCVValuesLabel_cv")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.storeCVValuesLabel_cv)
        self.storeCVValuesCheckBox_cv = QtWidgets.QCheckBox(self.formGroupBox_CV)
        self.storeCVValuesCheckBox_cv.setObjectName("storeCVValuesCheckBox_cv")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.storeCVValuesCheckBox_cv)
        self.verticalLayout.addWidget(self.formGroupBox_CV)
        self.formGroupBox_2 = QtWidgets.QGroupBox(self.groupbox)
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.formLayout_5.setObjectName("formLayout_5")
        self.crossValidateLabel = QtWidgets.QLabel(self.formGroupBox_2)
        self.crossValidateLabel.setObjectName("crossValidateLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.crossValidateLabel)
        self.crossValidateCheckBox = QtWidgets.QCheckBox(self.formGroupBox_2)
        self.crossValidateCheckBox.setChecked(True)
        self.crossValidateCheckBox.setObjectName("crossValidateCheckBox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.crossValidateCheckBox)
        self.verticalLayout.addWidget(self.formGroupBox_2)
        self.vboxlayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        self.crossValidateCheckBox.toggled['bool'].connect(self.formGroupBox_CV.setEnabled)
        self.crossValidateCheckBox.toggled['bool'].connect(self.formGroupBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.alphaLabel.setText(("Alpha"))
        self.copyXLabel.setText(("Copy X"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.maxNumOfIterationsLabel.setText(("Max num of Iterations"))
        self.maxNumOfIterationslineEdit.setText(("None"))
        self.normalizeLabel.setText(("Normalize"))
        self.solverLabel.setText(("Solver"))
        self.solverComboBox.setItemText(0, ("auto"))
        self.solverComboBox.setItemText(1, ("svd"))
        self.solverComboBox.setItemText(2, ("cholesky"))
        self.solverComboBox.setItemText(3, ("lsqr"))
        self.solverComboBox.setItemText(4, ("sparse_cg"))
        self.solverComboBox.setItemText(5, ("sag"))
        self.toleranceLabel.setText(("Tolerance"))
        self.randomStateLabel.setText(("Random State"))
        self.randomStateLineEdit.setText(("None"))
        self.alphasLabel_cv.setText(("alphas"))
        self.alphasLineEdit_cv.setText(("0.1, 1.0, 10.0"))
        self.fitInterceptLabel_cv.setText(("Fit intercept "))
        self.normalizeLabel_cv.setText(("Normalize "))
        self.scoringLabel_cv.setText(("Scoring"))
        self.scoringComboBox_cv.setItemText(0, ("None"))
        self.scoringComboBox_cv.setItemText(1, ("string"))
        self.scoringComboBox_cv.setItemText(2, ("callable"))
        self.gCVModeLabel_cv.setText(("GCV mode"))
        self.gCVModeComboBox_cv.setItemText(0, ("None"))
        self.gCVModeComboBox_cv.setItemText(1, ("auto"))
        self.gCVModeComboBox_cv.setItemText(2, ("svd"))
        self.gCVModeComboBox_cv.setItemText(3, ("eigen"))
        self.storeCVValuesLabel_cv.setText(("Store CV Values           "))
        self.crossValidateLabel.setText(("Cross Validate              "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

