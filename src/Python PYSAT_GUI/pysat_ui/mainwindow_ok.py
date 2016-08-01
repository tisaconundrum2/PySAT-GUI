# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\Documents\GitHub\PYSAT\src\New PYSAT_Gui\mainwindow_ok.ui'
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

class ok(object):
    def setupUi(self, MainWindow):
        self.OK = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.ok = QtGui.QHBoxLayout(self.OK)
        self.ok.setMargin(11)
        self.ok.setSpacing(6)
        self.ok.setObjectName(_fromUtf8("ok"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.ok.addWidget(self.okButton)
        self.verticalLayout_8.addWidget(self.OK)
        self.okButton.setText(_translate("MainWindow", "OK", None))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
