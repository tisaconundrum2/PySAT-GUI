# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chooseDataSetLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataSetLabel.setObjectName("chooseDataSetLabel")
        self.verticalLayout_2.addWidget(self.chooseDataSetLabel)
        self.chooseDataSetComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataSetComboBox.setObjectName("chooseDataSetComboBox")
        self.verticalLayout_2.addWidget(self.chooseDataSetComboBox)
        self.variablesToWriteLabel = QtWidgets.QLabel(self.groupBox)
        self.variablesToWriteLabel.setObjectName("variablesToWriteLabel")
        self.verticalLayout_2.addWidget(self.variablesToWriteLabel)
        self.variablesToWriteListWidget = QtWidgets.QListWidget(self.groupBox)
        self.variablesToWriteListWidget.setObjectName("variablesToWriteListWidget")
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.variablesToWriteListWidget)
        self.specifyAFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.specifyAFilenameLabel.setObjectName("specifyAFilenameLabel")
        self.verticalLayout_2.addWidget(self.specifyAFilenameLabel)
        self.specifyAFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.specifyAFilenameLineEdit.setObjectName("specifyAFilenameLineEdit")
        self.verticalLayout_2.addWidget(self.specifyAFilenameLineEdit)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Write to CSV"))
        self.chooseDataSetLabel.setText(("Choose data set to write to *.csv:"))
        self.variablesToWriteLabel.setText(("Variables to write:"))
        __sortingEnabled = self.variablesToWriteListWidget.isSortingEnabled()
        self.variablesToWriteListWidget.setSortingEnabled(False)
        item = self.variablesToWriteListWidget.item(0)
        item.setText(("comp"))
        item = self.variablesToWriteListWidget.item(1)
        item.setText(("meta"))
        item = self.variablesToWriteListWidget.item(2)
        item.setText(("wvl"))
        self.variablesToWriteListWidget.setSortingEnabled(__sortingEnabled)
        self.specifyAFilenameLabel.setText(("Specify a filename:"))
        self.specifyAFilenameLineEdit.setText(("output.csv"))

