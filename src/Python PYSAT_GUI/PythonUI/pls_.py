from PyQt4 import QtCore, QtGui
from pysat_function import pysat_func

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


class pls_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()

    def pls(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(254, 54)
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 10, 81, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "# of components", None))

