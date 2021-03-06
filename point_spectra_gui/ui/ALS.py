# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.formLayout = QtWidgets.QFormLayout(self.groupbox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.asymmetryLabel = QtWidgets.QLabel(self.groupbox)
        self.asymmetryLabel.setObjectName("asymmetryLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.asymmetryLabel)
        self.asymmetryDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.asymmetryDoubleSpinBox.setObjectName("asymmetryDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.asymmetryDoubleSpinBox)
        self.smoothnessLabel = QtWidgets.QLabel(self.groupbox)
        self.smoothnessLabel.setObjectName("smoothnessLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.smoothnessLabel)
        self.smoothnessDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.smoothnessDoubleSpinBox.setObjectName("smoothnessDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.smoothnessDoubleSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupbox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.convergenceThresholdLabel = QtWidgets.QLabel(self.groupbox)
        self.convergenceThresholdLabel.setObjectName("convergenceThresholdLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.convergenceThresholdLabel)
        self.convergenceThresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.convergenceThresholdDoubleSpinBox.setObjectName("convergenceThresholdDoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.convergenceThresholdDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.asymmetryLabel.setText(("Asymmetry"))
        self.smoothnessLabel.setText(("Smoothness"))
        self.maxNumOfIterationsLabel.setText(("Max Num of Iterations"))
        self.convergenceThresholdLabel.setText(("Convergence Threshold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

