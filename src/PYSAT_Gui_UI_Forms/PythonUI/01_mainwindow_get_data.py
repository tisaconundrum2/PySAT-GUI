# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_get_data.ui'
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

class Ui_get_data(object):
    def setupUi(self, get_data):
        get_data.setObjectName(_fromUtf8("get_data"))
        get_data.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_label = QtGui.QLabel(get_data)
        self.get_data_label.setObjectName(_fromUtf8("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtGui.QLineEdit(get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName(_fromUtf8("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtGui.QToolButton(get_data)
        self.get_data_button.setObjectName(_fromUtf8("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button)

        self.retranslateUi(get_data)
        QtCore.QMetaObject.connectSlotsByName(get_data)

    def retranslateUi(self, get_data):
        get_data.setWindowTitle(_translate("get_data", "GroupBox", None))
        get_data.setTitle(_translate("get_data", "<load file>", None))
        self.get_data_label.setText(_translate("get_data", "File Name", None))
        self.get_data_line_edit.setText(_translate("get_data", "*.csv", None))
        self.get_data_button.setText(_translate("get_data", "...", None))

