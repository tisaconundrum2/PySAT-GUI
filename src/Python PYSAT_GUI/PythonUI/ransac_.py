
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


class regression_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()

    def regression(self, ransac):
        ransac.setObjectName(_fromUtf8("ransac"))
        ransac.resize(676, 100)
        ransac.setMinimumSize(QtCore.QSize(600, 100))
        ransac.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ransac)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ransac_vlayout = QtGui.QVBoxLayout()
        self.ransac_vlayout.setObjectName(_fromUtf8("ransac_vlayout"))
        self.ransac_loss_func_hlayout = QtGui.QHBoxLayout()
        self.ransac_loss_func_hlayout.setObjectName(_fromUtf8("ransac_loss_func_hlayout"))
        self.ransac_loss_func = QtGui.QComboBox(ransac)
        self.ransac_loss_func.setObjectName(_fromUtf8("ransac_loss_func"))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_loss_func)
        self.ransac_threshold_label = QtGui.QLabel(ransac)
        self.ransac_threshold_label.setObjectName(_fromUtf8("ransac_threshold_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold_label)
        self.ransac_threshold = QtGui.QDoubleSpinBox(ransac)
        self.ransac_threshold.setObjectName(_fromUtf8("ransac_threshold"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold)
        self.ransac_min_label = QtGui.QLabel(ransac)
        self.ransac_min_label.setObjectName(_fromUtf8("ransac_min_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min_label)
        self.ransac_min = QtGui.QDoubleSpinBox(ransac)
        self.ransac_min.setObjectName(_fromUtf8("ransac_min"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_loss_func_hlayout.addItem(spacerItem)
        self.ransac_vlayout.addLayout(self.ransac_loss_func_hlayout)
        self.verticalLayout_2.addLayout(self.ransac_vlayout)
        ransac.setWindowTitle(_translate("ransac", "RANSAC", None))
        ransac.setTitle(_translate("ransac", "RANSAC", None))
        self.ransac_loss_func.setItemText(0, _translate("ransac", "Loss Function", None))
        self.ransac_loss_func.setItemText(1, _translate("ransac", "Absolute Error", None))
        self.ransac_loss_func.setItemText(2, _translate("ransac", "Squared Error", None))
        self.ransac_threshold_label.setText(_translate("ransac", "Threshold", None))
        self.ransac_min_label.setText(_translate("ransac", "Minimum samples ", None))

