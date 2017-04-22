from PyQt5 import QtGui, QtCore, QtWidgets


class get_data_u_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.get_data_ui()  # initiate the UI
        self.pysat_fun.set_greyed_modules(self.get_data)
        try:
            self.get_data_button.clicked.connect(lambda: self.on_getDataButton_clicked(self.get_data_line_edit,
                                                                                       "unknown"))  # when a button is clicked call the on_getDataButton_clicked function
        except:
            pass

    def get_data_ui(self):
        self.get_data = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_data.setFont(font)
        self.get_data.setObjectName(("get_data"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_data)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.get_data_label = QtWidgets.QLabel(self.get_data)
        self.get_data_label.setObjectName(("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtWidgets.QLineEdit(self.get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName(("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtWidgets.QToolButton(self.get_data)
        self.get_data_button.setObjectName(("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button)
        self.module_layout.addWidget(self.get_data)

        self.horizontalWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        # self.line.setStyleSheet("background-color: grey")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.module_layout.addWidget(self.horizontalWidget)

        self.get_data.setTitle("Load Known Data")
        self.get_data_label.setText("File Name")
        self.get_data_button.setText("...")
        self.set_data_parameters()

        self.get_data.setTitle("Load Unknown Data")
        self.get_data_label.setText("File Name")
        self.get_data_button.setText("...")
        self.set_data_parameters()

    def set_data_parameters(self):
        if self.arg_list is None:
            self.get_data_line_edit.setText("*.csv")
        else:
            # the 0'th element has the name of the file that we want to work with.
            self.get_data_line_edit.setText(self.arg_list[0])
            self.push_parameters(self.arg_list, self.kw_list)

    def push_parameters(self, arg_list, kw_list):
        ui_list = "get_known_data"
        fun_list = "get_data"
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, self.ui_id)

    def on_getDataButton_clicked(self, lineEdit, key):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.push_parameters([filename, key], {})


class get_data_k_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.get_data_ui()  # initiate the UI
        self.pysat_fun.set_greyed_modules(self.get_data)
        try:
            self.get_data_button.clicked.connect(lambda: self.on_getDataButton_clicked(self.get_data_line_edit,
                                                                                       "known"))  # when a button is clicked call the on_getDataButton_clicked function
        except:
            pass

    def get_data_ui(self):
        self.get_data = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_data.setFont(font)
        self.get_data.setObjectName(("get_data"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_data)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.get_data_label = QtWidgets.QLabel(self.get_data)
        self.get_data_label.setObjectName(("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtWidgets.QLineEdit(self.get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName(("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtWidgets.QToolButton(self.get_data)
        self.get_data_button.setObjectName(("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button)
        self.module_layout.addWidget(self.get_data)

        self.horizontalWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        # self.line.setStyleSheet("background-color: grey")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.module_layout.addWidget(self.horizontalWidget)

        self.get_data.setTitle("Load Known Data")
        self.get_data_label.setText("File Name")
        self.get_data_button.setText("...")
        self.set_data_parameters()

    def radio_button_clicked(self):
        # TODO set the counting distance
        pass

    def set_data_parameters(self):
        if self.arg_list is None:
            self.get_data_line_edit.setText("*.csv")
        else:
            # the 0'th element has the name of the file that we want to work with.
            self.get_data_line_edit.setText(self.arg_list[0])
            self.push_parameters(self.arg_list, self.kw_list)

    def push_parameters(self, arg_list, kw_list):
        ui_list = "get_known_data"
        fun_list = "get_data"
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, self.ui_id)

    def on_getDataButton_clicked(self, lineEdit, key):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.push_parameters([filename, key], {})
