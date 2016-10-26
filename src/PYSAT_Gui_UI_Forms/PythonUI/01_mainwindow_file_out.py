# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_file_out.ui'
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

class Ui_file_out_path(object):
    def setupUi(self, file_out_path):
        file_out_path.setObjectName(_fromUtf8("file_out_path"))
        file_out_path.resize(600, 150)
        file_out_path.setMinimumSize(QtCore.QSize(600, 150))
        file_out_path.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalLayout = QtGui.QHBoxLayout(file_out_path)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_out_path_label = QtGui.QLabel(file_out_path)
        self.file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtGui.QLineEdit(file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtGui.QToolButton(file_out_path)
        self.file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
        self.horizontalLayout.addWidget(self.file_out_path_button)

        self.retranslateUi(file_out_path)
        QtCore.QMetaObject.connectSlotsByName(file_out_path)

    def retranslateUi(self, file_out_path):
        file_out_path.setWindowTitle(_translate("file_out_path", "PCA", None))
        file_out_path.setTitle(_translate("file_out_path", "Output Folder", None))
        self.file_out_path_label.setText(_translate("file_out_path", "Folder Name", None))
        self.file_out_path_line_edit.setText(_translate("file_out_path", "*/", None))
        self.file_out_path_button.setText(_translate("file_out_path", "...", None))

