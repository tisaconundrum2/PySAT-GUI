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


class get_data_u_:
    def __init__(self, pysat_fun, verticalLayout_8, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.arg_list = arg_list
        self.kwlist = kw_list
        self.ui_id = None
        self.main()

    def main(self):
        self.get_data_ui()  # initiate the UI
        self.pysat_fun.set_greyed_modules(self.get_data_u)
        try:
            self.get_data_u_button.clicked.connect(
                lambda: self.on_getDataButton_clicked(self.get_data_u_line_edit, "unknown"))  # when a button is clicked call the on_getDataButton_clicked function
        except:
            pass

    def get_data_ui(self):
        self.get_data_u = QtGui.QGroupBox()
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

        self.get_data_u.setTitle(_translate("MainWindow", "Load Unknown Data", None))
        self.get_data_u_label.setText(_translate("MainWindow", "File Name", None))
        self.get_data_u_button.setText(_translate("MainWindow", "...", None))
        self.set_data_parameters()

    def set_data_parameters(self):
        if self.arg_list is None:
            self.get_data_u_line_edit.setText(_translate("MainWindow", "*.csv", None))
        else:
            self.get_data_u_line_edit.setText(self.arg_list[0])

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        ui_list = "get_unknown_data"
        fun_list = "get_data"
        kw_list = {}
        arg_list = [filename, key]
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, self.ui_id)
        pass


class get_data_k_:
    def __init__(self, pysat_fun, verticalLayout_8, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.arg_list = arg_list
        self.kwlist = kw_list
        self.ui_id = None
        self.main()

    def main(self):
        self.get_data_ui()  # initiate the UI
        self.pysat_fun.set_greyed_modules(self.get_data_u)
        try:
            self.get_data_u_button.clicked.connect(
                lambda: self.on_getDataButton_clicked(self.get_data_u_line_edit,
                                                      "known"))  # when a button is clicked call the on_getDataButton_clicked function
        except:
            pass

    def get_data_ui(self):
        self.get_data_u = QtGui.QGroupBox()
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

        self.get_data_u.setTitle(_translate("MainWindow", "Load Known Data", None))
        self.get_data_u_label.setText(_translate("MainWindow", "File Name", None))
        self.get_data_u_button.setText(_translate("MainWindow", "...", None))
        self.set_data_parameters()

    def set_data_parameters(self):
        if self.arg_list is None:
            self.get_data_u_line_edit.setText(_translate("MainWindow", "*.csv", None))
        else:
            self.get_data_u_line_edit.setText(self.arg_list[0])

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        ui_list = "get_known_data"
        fun_list = "get_data"
        kw_list = {}
        arg_list = [filename, key]
        # when we call this function we will also set the ui_id
        # this way we can always keep track of the specific ui_id that we are messing with.
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, self.ui_id)
        pass
