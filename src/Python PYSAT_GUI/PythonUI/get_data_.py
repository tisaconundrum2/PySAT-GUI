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


class get_data_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()

    def get_data_u(self, get_data):
        get_data.setObjectName(_fromUtf8("get_data"))
        get_data.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_label = QtGui.QLabel(get_data)
        self.get_data_label.setObjectName(_fromUtf8("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit_U = QtGui.QLineEdit(get_data)
        self.get_data_line_edit_U.setReadOnly(True)
        self.get_data_line_edit_U.setObjectName(_fromUtf8("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit_U)
        self.get_data_button_U = QtGui.QToolButton(get_data)
        self.get_data_button_U.setObjectName(_fromUtf8("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button_U)
        get_data.setWindowTitle(_translate("get_data", "GroupBox", None))
        get_data.setTitle(_translate("get_data", "Load Unknown Data", None))
        self.get_data_label.setText(_translate("get_data", "File Name", None))
        self.get_data_line_edit_U.setText(_translate("get_data", "*.csv", None))
        self.get_data_button_U.setText(_translate("get_data", "...", None))
        try:
            self.get_data_button_U.clicked.connect(
                lambda: get_data_.on_getDataButton_clicked(self, self.get_data_line_edit_U, "Unknown"))

        except:
            pass


    def get_data_k(self, get_data):
        get_data.setObjectName(_fromUtf8("get_data"))
        get_data.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_label = QtGui.QLabel(get_data)
        self.get_data_label.setObjectName(_fromUtf8("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit_K = QtGui.QLineEdit(get_data)
        self.get_data_line_edit_K.setReadOnly(True)
        self.get_data_line_edit_K.setObjectName(_fromUtf8("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit_K)
        self.get_data_button_K = QtGui.QToolButton(get_data)
        self.get_data_button_K.setObjectName(_fromUtf8("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button_K)
        get_data.setWindowTitle(_translate("get_data", "GroupBox", None))
        get_data.setTitle(_translate("get_data", "Load Unknown Data", None))
        self.get_data_label.setText(_translate("get_data", "File Name", None))
        self.get_data_line_edit_K.setText(_translate("get_data", "*.csv", None))
        self.get_data_button_K.setText(_translate("get_data", "...", None))
        try:
            self.get_data_button_K.clicked.connect(
                lambda: get_data_.on_getDataButton_clicked(self, self.get_data_line_edit_K, "Known"))
        except:
            pass

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open Uknown Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)

