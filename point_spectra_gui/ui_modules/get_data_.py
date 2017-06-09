import os

from PyQt5 import QtGui, QtCore, QtWidgets
from Qtickle import Qtickle


class get_data_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.restr_list = restr_list
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.get_data_ui()  # initiate the UI
        self.set_data_params()
        self.get_data_params()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.get_data)

    def connectWidgets(self):
        self.get_data_button.clicked.connect(lambda: self.on_getDataButton_clicked())
        self.get_data_line_edit.textChanged.connect(lambda: self.get_data_params())
        self.dataname.textChanged.connect(lambda: self.get_data_params())

    def get_data_params(self):
        filename = self.get_data_line_edit.text()
        dataname = self.dataname.text()
        args = [filename, dataname]
        kws = {}
        ui_list = "do_get_data"
        fun_list = "do_get_data"
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)


    def get_data_ui(self):
        self.get_data = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_data.setFont(font)
        self.get_data.setObjectName("get_data")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.get_data)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_data)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_data_label = QtWidgets.QLabel(self.get_data)
        self.get_data_label.setObjectName("get_data_label")
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtWidgets.QLineEdit(self.get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName("get_data_line_edit")
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtWidgets.QToolButton(self.get_data)
        self.get_data_button.setObjectName("get_data_button")
        self.horizontalLayout.addWidget(self.get_data_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hlayout_dataname = QtWidgets.QHBoxLayout(self.get_data)
        self.dataname_label = QtWidgets.QLabel(self.get_data)
        self.dataname_label.setText('Data set name:')
        self.hlayout_dataname.addWidget(self.dataname_label)
        self.dataname = QtWidgets.QLineEdit(self.get_data)
        self.dataname.setObjectName("dataname")
        self.hlayout_dataname.addWidget(self.dataname)
        self.verticalLayout.addLayout(self.hlayout_dataname)
        self.module_layout.addWidget(self.get_data)
        self.get_data.setTitle("Load Data")
        self.get_data_label.setText("File Name")
        self.get_data_button.setText("...")

    def set_data_params(self):
        if self.restr_list is None:
            self.get_data_line_edit.setText("*.csv")
        else:
            self.qtickle.guirestore(self.restr_list)

    def on_getDataButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", '.', "(*.csv)")
        self.get_data_line_edit.setText(filename)
        if self.get_data_line_edit.text() == "":
            self.get_data_line_edit.setText("*.csv")
        self.get_data_params()
