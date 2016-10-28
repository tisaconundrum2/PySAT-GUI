from PyQt4 import QtCore, QtGui
from pysat_func import pysat_func

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
        self.get_data_u = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_data_u.setFont(font)
        self.get_data_u.setObjectName(_fromUtf8("get_data_u"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.get_data_u)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_u_label = QtGui.QLabel(self.get_data_u)
        self.get_data_u_label.setObjectName(_fromUtf8("get_data_u_label"))
        self.horizontalLayout.addWidget(self.get_data_u_label)
        self.get_data_u_line_edit = QtGui.QLineEdit(self.get_data_u)
        self.get_data_u_line_edit.setReadOnly(True)
        self.get_data_u_line_edit.setObjectName(_fromUtf8("get_data_u_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_u_line_edit)
        self.get_data_u_button = QtGui.QToolButton(self.get_data_u)
        self.get_data_u_button.setObjectName(_fromUtf8("get_data_u_button"))
        self.horizontalLayout.addWidget(self.get_data_u_button)
        self.verticalLayout_8.addWidget(self.get_data_u)

        self.get_data_u.setTitle(_translate("MainWindow", "Load in Unknown data file", None))
        self.get_data_u_label.setText(_translate("MainWindow", "File Name", None))
        self.get_data_u_line_edit.setText(_translate("MainWindow", "*.csv", None))
        self.get_data_u_button.setText(_translate("MainWindow", "...", None))
        try:
            self.get_data_u_button.clicked.connect(
                lambda: get_data_.on_getDataButton_clicked(self, self.get_data_u_line_edit, "Unknown"))

        except:
            pass


    def get_data_k(self, get_data):
        self.get_data_k = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_data_k.setFont(font)
        self.get_data_k.setObjectName(_fromUtf8("get_data_k"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.get_data_k)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_k_label = QtGui.QLabel(self.get_data_k)
        self.get_data_k_label.setObjectName(_fromUtf8("get_data_k_label"))
        self.horizontalLayout.addWidget(self.get_data_k_label)
        self.get_data_k_line_edit = QtGui.QLineEdit(self.get_data_k)
        self.get_data_k_line_edit.setReadOnly(True)
        self.get_data_k_line_edit.setObjectName(_fromUtf8("get_data_k_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_k_line_edit)
        self.get_data_k_button = QtGui.QToolButton(self.get_data_k)
        self.get_data_k_button.setObjectName(_fromUtf8("get_data_k_button"))
        self.horizontalLayout.addWidget(self.get_data_k_button)
        self.verticalLayout_8.addWidget(self.get_data_k)

        self.get_data_k.setTitle(_translate("MainWindow", "Load in Known data file", None))
        self.get_data_k_label.setText(_translate("MainWindow", "File Name", None))
        self.get_data_k_line_edit.setText(_translate("MainWindow", "*.csv", None))
        self.get_data_k_button.setText(_translate("MainWindow", "...", None))
        try:
            self.get_data_k_button.clicked.connect(
                lambda: get_data_.on_getDataButton_clicked(self, self.get_data_k_line_edit, "Known"))
        except:
            pass

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)

