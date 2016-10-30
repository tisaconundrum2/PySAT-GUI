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


def get_data_u(pysat_fun, verticalLayout_8):
    get_data_u = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    get_data_u.setFont(font)
    get_data_u.setObjectName(_fromUtf8("get_data_u"))
    horizontalLayout = QtGui.QHBoxLayout(get_data_u)
    horizontalLayout.setMargin(11)
    horizontalLayout.setSpacing(6)
    horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    get_data_u_label = QtGui.QLabel(get_data_u)
    get_data_u_label.setObjectName(_fromUtf8("get_data_u_label"))
    horizontalLayout.addWidget(get_data_u_label)
    get_data_u_line_edit = QtGui.QLineEdit(get_data_u)
    get_data_u_line_edit.setReadOnly(True)
    get_data_u_line_edit.setObjectName(_fromUtf8("get_data_u_line_edit"))
    horizontalLayout.addWidget(get_data_u_line_edit)
    get_data_u_button = QtGui.QToolButton(get_data_u)
    get_data_u_button.setObjectName(_fromUtf8("get_data_u_button"))
    horizontalLayout.addWidget(get_data_u_button)
    verticalLayout_8.addWidget(get_data_u)

    get_data_u.setTitle(_translate("MainWindow", "Load in Unknown data file", None))
    get_data_u_label.setText(_translate("MainWindow", "File Name", None))
    get_data_u_line_edit.setText(_translate("MainWindow", "*.csv", None))
    get_data_u_button.setText(_translate("MainWindow", "...", None))
    try:
        get_data_u_button.clicked.connect(
            lambda: on_getDataButton_clicked(pysat_fun, get_data_u_line_edit, "Unknown"))

    except:
        pass


def get_data_k(pysat_fun, verticalLayout_8):
    get_data_k = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    get_data_k.setFont(font)
    get_data_k.setObjectName(_fromUtf8("get_data_k"))
    horizontalLayout = QtGui.QHBoxLayout(get_data_k)
    horizontalLayout.setMargin(11)
    horizontalLayout.setSpacing(6)
    horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    get_data_k_label = QtGui.QLabel(get_data_k)
    get_data_k_label.setObjectName(_fromUtf8("get_data_k_label"))
    horizontalLayout.addWidget(get_data_k_label)
    get_data_k_line_edit = QtGui.QLineEdit(get_data_k)
    get_data_k_line_edit.setReadOnly(True)
    get_data_k_line_edit.setObjectName(_fromUtf8("get_data_k_line_edit"))
    horizontalLayout.addWidget(get_data_k_line_edit)
    get_data_k_button = QtGui.QToolButton(get_data_k)
    get_data_k_button.setObjectName(_fromUtf8("get_data_k_button"))
    horizontalLayout.addWidget(get_data_k_button)
    verticalLayout_8.addWidget(get_data_k)

    get_data_k.setTitle(_translate("MainWindow", "Load in Known data file", None))
    get_data_k_label.setText(_translate("MainWindow", "File Name", None))
    get_data_k_line_edit.setText(_translate("MainWindow", "*.csv", None))
    get_data_k_button.setText(_translate("MainWindow", "...", None))
    try:
        get_data_k_button.clicked.connect(
            lambda: on_getDataButton_clicked(pysat_fun, get_data_k_line_edit, "Known"))
    except:
        pass

def on_getDataButton_clicked(pysat_fun, lineEdit, key):
    filename = QtGui.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
    lineEdit.setText(filename)
    if lineEdit.text() == "":
        lineEdit.setText("*.csv")
    pysat_fun.get_data(filename, key)

