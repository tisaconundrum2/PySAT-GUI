# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\PlotSpectra.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 437)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout_2.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.figureNameLabel = QtWidgets.QLabel(self.groupbox)
        self.figureNameLabel.setObjectName("figureNameLabel")
        self.gridLayout_2.addWidget(self.figureNameLabel, 1, 0, 1, 1)
        self.plotTitleLabel = QtWidgets.QLabel(self.groupbox)
        self.plotTitleLabel.setObjectName("plotTitleLabel")
        self.gridLayout_2.addWidget(self.plotTitleLabel, 2, 0, 1, 1)
        self.xVariableLabel = QtWidgets.QLabel(self.groupbox)
        self.xVariableLabel.setObjectName("xVariableLabel")
        self.gridLayout_2.addWidget(self.xVariableLabel, 3, 0, 1, 1)
        self.xVariableListView = QtWidgets.QListView(self.groupbox)
        self.xVariableListView.setObjectName("xVariableListView")
        self.gridLayout_2.addWidget(self.xVariableListView, 3, 1, 1, 2)
        self.chooseColumnLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseColumnLabel.setObjectName("chooseColumnLabel")
        self.gridLayout_2.addWidget(self.chooseColumnLabel, 4, 0, 1, 1)
        self.chooseRowsLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseRowsLabel.setObjectName("chooseRowsLabel")
        self.gridLayout_2.addWidget(self.chooseRowsLabel, 5, 0, 1, 1)
        self.chooseRowsListView = QtWidgets.QListView(self.groupbox)
        self.chooseRowsListView.setObjectName("chooseRowsListView")
        self.gridLayout_2.addWidget(self.chooseRowsListView, 5, 1, 1, 2)
        self.colorLabel = QtWidgets.QLabel(self.groupbox)
        self.colorLabel.setObjectName("colorLabel")
        self.gridLayout_2.addWidget(self.colorLabel, 7, 0, 1, 1)
        self.lineLabel = QtWidgets.QLabel(self.groupbox)
        self.lineLabel.setObjectName("lineLabel")
        self.gridLayout_2.addWidget(self.lineLabel, 8, 0, 1, 1)
        self.alphaLabel = QtWidgets.QLabel(self.groupbox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.gridLayout_2.addWidget(self.alphaLabel, 9, 0, 1, 1)
        self.lineWidthLabel = QtWidgets.QLabel(self.groupbox)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.gridLayout_2.addWidget(self.lineWidthLabel, 10, 0, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupbox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.gridLayout_2.addWidget(self.plotFilenameLabel, 11, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupbox)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.gridLayout_2.addWidget(self.plotFilenameLineEdit, 11, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupbox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 11, 2, 1, 1)
        self.figureNameLineEdit = QtWidgets.QLineEdit(self.groupbox)
        self.figureNameLineEdit.setObjectName("figureNameLineEdit")
        self.gridLayout_2.addWidget(self.figureNameLineEdit, 1, 1, 1, 2)
        self.plotTitleLineEdit = QtWidgets.QLineEdit(self.groupbox)
        self.plotTitleLineEdit.setObjectName("plotTitleLineEdit")
        self.gridLayout_2.addWidget(self.plotTitleLineEdit, 2, 1, 1, 2)
        self.chooseColumnComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseColumnComboBox.setObjectName("chooseColumnComboBox")
        self.gridLayout_2.addWidget(self.chooseColumnComboBox, 4, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minLabel = QtWidgets.QLabel(self.groupbox)
        self.minLabel.setObjectName("minLabel")
        self.horizontalLayout.addWidget(self.minLabel)
        self.minSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox.setObjectName("minSpinBox")
        self.horizontalLayout.addWidget(self.minSpinBox)
        self.maxLabel = QtWidgets.QLabel(self.groupbox)
        self.maxLabel.setObjectName("maxLabel")
        self.horizontalLayout.addWidget(self.maxLabel)
        self.maxSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.horizontalLayout.addWidget(self.maxSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        self.colorComboBox = QtWidgets.QComboBox(self.groupbox)
        self.colorComboBox.setObjectName("colorComboBox")
        self.gridLayout_2.addWidget(self.colorComboBox, 7, 1, 1, 2)
        self.lineComboBox = QtWidgets.QComboBox(self.groupbox)
        self.lineComboBox.setObjectName("lineComboBox")
        self.gridLayout_2.addWidget(self.lineComboBox, 8, 1, 1, 2)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.gridLayout_2.addWidget(self.alphaDoubleSpinBox, 9, 1, 1, 2)
        self.lineWidthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.lineWidthDoubleSpinBox.setObjectName("lineWidthDoubleSpinBox")
        self.gridLayout_2.addWidget(self.lineWidthDoubleSpinBox, 10, 1, 1, 2)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout_2.addWidget(self.chooseDataComboBox, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupbox.setTitle(_translate("Form", "Plot Spectra"))
        self.chooseDataLabel.setText(_translate("Form", "Choose Data"))
        self.figureNameLabel.setText(_translate("Form", "Figure Name"))
        self.plotTitleLabel.setText(_translate("Form", "Plot Title"))
        self.xVariableLabel.setText(_translate("Form", "X Variable:"))
        self.chooseColumnLabel.setText(_translate("Form", "Choose Column"))
        self.chooseRowsLabel.setText(_translate("Form", "Choose Rows:"))
        self.colorLabel.setText(_translate("Form", "Color"))
        self.lineLabel.setText(_translate("Form", "Line"))
        self.alphaLabel.setText(_translate("Form", "Alpha"))
        self.lineWidthLabel.setText(_translate("Form", "Line width"))
        self.plotFilenameLabel.setText(_translate("Form", "Plot Filename"))
        self.pushButton.setText(_translate("Form", "..."))
        self.minLabel.setText(_translate("Form", "Min"))
        self.maxLabel.setText(_translate("Form", "Max"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

