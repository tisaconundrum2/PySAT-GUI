# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\pca.ui'
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

class Ui_pca(object):
    def setupUi(self, pca):
        pca.setObjectName(_fromUtf8("pca"))
        pca.resize(614, 150)
        pca.setMinimumSize(QtCore.QSize(600, 150))
        pca.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(pca)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pca_vlayout = QtGui.QVBoxLayout()
        self.pca_vlayout.setObjectName(_fromUtf8("pca_vlayout"))
        self.pca_choose_data = QtGui.QComboBox(pca)
        self.pca_choose_data.setObjectName(_fromUtf8("pca_choose_data"))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtGui.QHBoxLayout()
        self.pca_hlayout.setObjectName(_fromUtf8("pca_hlayout"))
        self.pca_nc_label = QtGui.QLabel(pca)
        self.pca_nc_label.setObjectName(_fromUtf8("pca_nc_label"))
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtGui.QSpinBox(pca)
        self.pca_nc.setObjectName(_fromUtf8("pca_nc"))
        self.pca_hlayout.addWidget(self.pca_nc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtGui.QPushButton(pca)
        self.pca_button.setObjectName(_fromUtf8("pca_button"))
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout_2.addLayout(self.pca_vlayout)

        self.retranslateUi(pca)
        QtCore.QMetaObject.connectSlotsByName(pca)

    def retranslateUi(self, pca):
        pca.setWindowTitle(_translate("pca", "PCA", None))
        pca.setTitle(_translate("pca", "PCA", None))
        self.pca_choose_data.setItemText(0, _translate("pca", "Choose Data", None))
        self.pca_choose_data.setItemText(1, _translate("pca", "Known Data", None))
        self.pca_nc_label.setText(_translate("pca", "# of components", None))
        self.pca_button.setText(_translate("pca", "Do PCA", None))

