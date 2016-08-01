# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\Documents\GitHub\PYSAT\src\New PYSAT_Gui\mainwindow.ui'
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

class files(object):
    def setupUi(self, MainWindow):
        self.Files = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Files.setFont(font)
        self.Files.setObjectName(_fromUtf8("Files"))
        self.files = QtGui.QVBoxLayout(self.Files)
        self.files.setMargin(11)
        self.files.setSpacing(6)
        self.files.setObjectName(_fromUtf8("files"))
        self.splitter_2 = QtGui.QSplitter(self.Files)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setMargin(11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_6.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setMargin(11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.verticalLayout_5.addWidget(self.lineEdit_6)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.maskFileButton = QtGui.QToolButton(self.layoutWidget)
        self.maskFileButton.setObjectName(_fromUtf8("maskFileButton"))
        self.verticalLayout.addWidget(self.maskFileButton)
        self.unknownDataButton = QtGui.QToolButton(self.layoutWidget)
        self.unknownDataButton.setObjectName(_fromUtf8("unknownDataButton"))
        self.verticalLayout.addWidget(self.unknownDataButton)
        self.fullDataBaseButton = QtGui.QToolButton(self.layoutWidget)
        self.fullDataBaseButton.setObjectName(_fromUtf8("fullDataBaseButton"))
        self.verticalLayout.addWidget(self.fullDataBaseButton)
        self.outPutLocationButton = QtGui.QToolButton(self.layoutWidget)
        self.outPutLocationButton.setObjectName(_fromUtf8("outPutLocationButton"))
        self.verticalLayout.addWidget(self.outPutLocationButton)
        self.pythonButton = QtGui.QToolButton(self.layoutWidget)
        self.pythonButton.setObjectName(_fromUtf8("pythonButton"))
        self.verticalLayout.addWidget(self.pythonButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.files.addWidget(self.splitter_2)
        self.verticalLayout_8.addWidget(self.Files)

        self.Files.setTitle(_translate("MainWindow", "Files", None))
        self.label_3.setText(_translate("MainWindow", "Maskfile", None))
        self.label.setText(_translate("MainWindow", "Unknown Data", None))
        self.label_2.setText(_translate("MainWindow", "Full Database", None))
        self.label_4.setText(_translate("MainWindow", "Output Location", None))
        self.label_5.setText(_translate("MainWindow", "Python exe Location", None))
        self.lineEdit.setText(_translate("MainWindow", "*.csv", None))
        self.lineEdit_2.setText(_translate("MainWindow", "*.csv", None))
        self.lineEdit_3.setText(_translate("MainWindow", "*.csv", None))
        self.lineEdit_4.setText(_translate("MainWindow", "*/*", None))
        self.lineEdit_6.setText(_translate("MainWindow", "*python.exe", None))
        self.maskFileButton.setText(_translate("MainWindow", "...", None))
        self.unknownDataButton.setText(_translate("MainWindow", "...", None))
        self.fullDataBaseButton.setText(_translate("MainWindow", "...", None))
        self.outPutLocationButton.setText(_translate("MainWindow", "...", None))
        self.pythonButton.setText(_translate("MainWindow", "...", None))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)