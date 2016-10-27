# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\TODO\01_mainwindow_unknown_data.ui'
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

class Ui_unknown_data(object):
    def setupUi(self, unknown_data):
        unknown_data.setObjectName(_fromUtf8("unknown_data"))
        unknown_data.resize(362, 164)
        self.horizontalLayout = QtGui.QHBoxLayout(unknown_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unknown_data_label = QtGui.QLabel(unknown_data)
        self.unknown_data_label.setObjectName(_fromUtf8("unknown_data_label"))
        self.horizontalLayout.addWidget(self.unknown_data_label)
        self.unknown_data_line_edit = QtGui.QLineEdit(unknown_data)
        self.unknown_data_line_edit.setReadOnly(True)
        self.unknown_data_line_edit.setObjectName(_fromUtf8("unknown_data_line_edit"))
        self.horizontalLayout.addWidget(self.unknown_data_line_edit)
        self.unknown_data_button = QtGui.QToolButton(unknown_data)
        self.unknown_data_button.setObjectName(_fromUtf8("unknown_data_button"))
        self.horizontalLayout.addWidget(self.unknown_data_button)

        self.retranslateUi(unknown_data)
        QtCore.QMetaObject.connectSlotsByName(unknown_data)

    def retranslateUi(self, unknown_data):
        unknown_data.setWindowTitle(_translate("unknown_data", "GroupBox", None))
        unknown_data.setTitle(_translate("unknown_data", "Unknown Data", None))
        self.unknown_data_label.setText(_translate("unknown_data", "File Name", None))
        self.unknown_data_line_edit.setText(_translate("unknown_data", "*.csv", None))
        self.unknown_data_button.setText(_translate("unknown_data", "...", None))

