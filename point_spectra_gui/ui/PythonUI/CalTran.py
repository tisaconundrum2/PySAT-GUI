# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rbanderson\Documents\Projects\LIBS PDART\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\CalTran.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalTran(object):
    def setupUi(self, CalTran):
        CalTran.setObjectName("CalTran")
        CalTran.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(CalTran)
        self.formLayoutWidget.setGeometry(QtCore.QRect(22, 40, 351, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.CalTran_dataSetRefLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.CalTran_dataSetRefLabel.setObjectName("CalTran_dataSetRefLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetRefLabel)
        self.CalTran_dataSetRefLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.CalTran_dataSetRefLineEdit.setObjectName("CalTran_dataSetRefLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetRefLineEdit)
        self.CalTran_dataSetTransformLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.CalTran_dataSetTransformLabel.setObjectName("CalTran_dataSetTransformLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetTransformLabel)
        self.CalTran_dataSetTransformLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.CalTran_dataSetTransformLineEdit.setObjectName("CalTran_dataSetTransformLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetTransformLineEdit)
        self.CalTran_columnToMatchLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.CalTran_columnToMatchLabel.setObjectName("CalTran_columnToMatchLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CalTran_columnToMatchLabel)
        self.CalTran_columnToMatchComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.CalTran_columnToMatchComboBox.setObjectName("CalTran_columnToMatchComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CalTran_columnToMatchComboBox)
        self.methodLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.methodLabel.setObjectName("methodLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.methodLabel)
        self.methodComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.methodComboBox)

        self.retranslateUi(CalTran)
        QtCore.QMetaObject.connectSlotsByName(CalTran)

    def retranslateUi(self, CalTran):
        _translate = QtCore.QCoreApplication.translate
        CalTran.setWindowTitle(_translate("CalTran", "Calibration Transfer"))
        CalTran.setTitle(_translate("CalTran", "GroupBox"))
        self.CalTran_dataSetRefLabel.setText(_translate("CalTran", "Reference Data Set:"))
        self.CalTran_dataSetTransformLabel.setText(_translate("CalTran", "Data Set to Transform:"))
        self.CalTran_columnToMatchLabel.setText(_translate("CalTran", "Column to Match:"))
        self.methodLabel.setText(_translate("CalTran", "Method:"))
        self.methodComboBox.setItemText(0, _translate("CalTran", "LRA - Low Rank Alignment"))
        self.methodComboBox.setItemText(1, _translate("CalTran", "PDS - Piecewise Direct Standardization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalTran = QtWidgets.QGroupBox()
    ui = Ui_CalTran()
    ui.setupUi(CalTran)
    CalTran.show()
    sys.exit(app.exec_())

