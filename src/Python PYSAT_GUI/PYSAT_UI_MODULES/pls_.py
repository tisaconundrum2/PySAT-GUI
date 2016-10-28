from PyQt4 import QtCore, QtGui
import pysat_func

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
        self.pls = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pls.setFont(font)
        self.pls.setObjectName(_fromUtf8("pls"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.pls)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pls_label = QtGui.QLabel(self.pls)
        self.pls_label.setObjectName(_fromUtf8("pls_label"))
        self.horizontalLayout.addWidget(self.pls_label)
        self.pls_spinbox = QtGui.QSpinBox(self.pls)
        self.pls_spinbox.setObjectName(_fromUtf8("pls_spinbox"))
        self.horizontalLayout.addWidget(self.pls_spinbox)
        self.verticalLayout_8.addWidget(self.pls)

        self.pls.setTitle(_translate("MainWindow", "PLS", None))

