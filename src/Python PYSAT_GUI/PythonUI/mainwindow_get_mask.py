# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_get_mask.ui'
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

class Ui_get_mask(object):
    def setupUi(self, get_mask):
        get_mask.setObjectName(_fromUtf8("get_mask"))
        get_mask.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_mask)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_mask_label = QtGui.QLabel(get_mask)
        self.get_mask_label.setObjectName(_fromUtf8("get_mask_label"))
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtGui.QLineEdit(get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName(_fromUtf8("get_mask_line_edit"))
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtGui.QToolButton(get_mask)
        self.get_mask_button.setObjectName(_fromUtf8("get_mask_button"))
        self.horizontalLayout.addWidget(self.get_mask_button)

        self.retranslateUi(get_mask)
        QtCore.QMetaObject.connectSlotsByName(get_mask)

    def retranslateUi(self, get_mask):
        get_mask.setWindowTitle(_translate("get_mask", "GroupBox", None))
        get_mask.setTitle(_translate("get_mask", "Get Mask File", None))
        self.get_mask_label.setText(_translate("get_mask", "File Name", None))
        self.get_mask_line_edit.setText(_translate("get_mask", "*.csv", None))
        self.get_mask_button.setText(_translate("get_mask", "...", None))

