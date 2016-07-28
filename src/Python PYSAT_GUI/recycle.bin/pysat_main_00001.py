# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\PycharmProjects\Udemy\src\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(457, 192)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.files_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.files_groupBox.setObjectName(_fromUtf8("files_groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.files_groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.maskfile_label = QtGui.QLabel(self.files_groupBox)
        self.maskfile_label.setObjectName(_fromUtf8("maskfile_label"))
        self.verticalLayout_3.addWidget(self.maskfile_label)
        self.unknowndata_label = QtGui.QLabel(self.files_groupBox)
        self.unknowndata_label.setObjectName(_fromUtf8("unknowndata_label"))
        self.verticalLayout_3.addWidget(self.unknowndata_label)
        self.fulldatabase_label = QtGui.QLabel(self.files_groupBox)
        self.fulldatabase_label.setObjectName(_fromUtf8("fulldatabase_label"))
        self.verticalLayout_3.addWidget(self.fulldatabase_label)
        self.outputlocation_label = QtGui.QLabel(self.files_groupBox)
        self.outputlocation_label.setObjectName(_fromUtf8("outputlocation_label"))
        self.verticalLayout_3.addWidget(self.outputlocation_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.maskfile_lineEdit = QtGui.QLineEdit(self.files_groupBox)
        self.maskfile_lineEdit.setObjectName(_fromUtf8("maskfile_lineEdit"))
        self.verticalLayout_2.addWidget(self.maskfile_lineEdit)
        self.unknowndata_lineEdit = QtGui.QLineEdit(self.files_groupBox)
        self.unknowndata_lineEdit.setObjectName(_fromUtf8("unknowndata_lineEdit"))
        self.verticalLayout_2.addWidget(self.unknowndata_lineEdit)
        self.fulldatabase_lineEdit = QtGui.QLineEdit(self.files_groupBox)
        self.fulldatabase_lineEdit.setObjectName(_fromUtf8("fulldatabase_lineEdit"))
        self.verticalLayout_2.addWidget(self.fulldatabase_lineEdit)
        self.outputlocation_lineEdit = QtGui.QLineEdit(self.files_groupBox)
        self.outputlocation_lineEdit.setObjectName(_fromUtf8("outputlocation_lineEdit"))
        self.verticalLayout_2.addWidget(self.outputlocation_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.maskfile_toolButton = QtGui.QToolButton(self.files_groupBox)
        self.maskfile_toolButton.setObjectName(_fromUtf8("maskfile_toolButton"))
        self.verticalLayout.addWidget(self.maskfile_toolButton)
        self.unknowndata_toolButton = QtGui.QToolButton(self.files_groupBox)
        self.unknowndata_toolButton.setObjectName(_fromUtf8("unknowndata_toolButton"))
        self.verticalLayout.addWidget(self.unknowndata_toolButton)
        self.fulldatabase_toolButton = QtGui.QToolButton(self.files_groupBox)
        self.fulldatabase_toolButton.setObjectName(_fromUtf8("fulldatabase_toolButton"))
        self.verticalLayout.addWidget(self.fulldatabase_toolButton)
        self.outputlocation_toolButton = QtGui.QToolButton(self.files_groupBox)
        self.outputlocation_toolButton.setObjectName(_fromUtf8("outputlocation_toolButton"))
        self.verticalLayout.addWidget(self.outputlocation_toolButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.files_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.files_groupBox.setTitle(_translate("MainWindow", "Files", None))
        self.maskfile_label.setText(_translate("MainWindow", "Maskfile", None))
        self.unknowndata_label.setText(_translate("MainWindow", "Unknown Data", None))
        self.fulldatabase_label.setText(_translate("MainWindow", "Full Database", None))
        self.outputlocation_label.setText(_translate("MainWindow", "Output Location", None))
        self.maskfile_toolButton.setText(_translate("MainWindow", "...", None))
        self.unknowndata_toolButton.setText(_translate("MainWindow", "...", None))
        self.fulldatabase_toolButton.setText(_translate("MainWindow", "...", None))
        self.outputlocation_toolButton.setText(_translate("MainWindow", "...", None))

