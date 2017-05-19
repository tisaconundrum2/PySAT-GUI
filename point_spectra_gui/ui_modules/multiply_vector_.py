from PyQt5 import QtGui, QtCore, QtWidgets
from pysat.utils.gui_utils import make_combobox
from point_spectra_gui.ui_modules import error_print


class multiply_vector_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.module_layout = module_layout
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.multiply_vector_ui()
        self.pysat_fun.set_greyed_modules(self.multiply_vector)

    def multiply_vector_params(self):
        datakey = self.vector_choosedata.currentText()
        vectorfile = self.multiply_vector_line_edit.text()
        ui_list = "do_multiply_vector"
        fun_list = "do_multiply_vector"
        args = [datakey, vectorfile]
        kws = {}
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.ui_id)

    def multiply_vector_ui(self):
        self.multiply_vector = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.multiply_vector.setFont(font)
        self.multiply_vector.setObjectName(("multiply_vector"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.multiply_vector)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(("horizontalLayout"))

        self.choosedata_label = QtWidgets.QLabel(self.multiply_vector)
        self.choosedata_label.setObjectName(("choosedata_label"))
        self.horizontalLayout.addWidget(self.choosedata_label)
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No data has been loaded!')
            datachoices = ['No data has been loaded!']
        self.vector_choosedata = make_combobox(datachoices)
        self.horizontalLayout.addWidget(self.vector_choosedata)

        self.multiply_vector_label = QtWidgets.QLabel(self.multiply_vector)
        self.multiply_vector_label.setObjectName(("multiply_vector_label"))
        self.horizontalLayout.addWidget(self.multiply_vector_label)
        self.multiply_vector_line_edit = QtWidgets.QLineEdit(self.multiply_vector)
        self.multiply_vector_line_edit.setReadOnly(True)
        self.multiply_vector_line_edit.setObjectName(("multiply_vector_line_edit"))
        self.horizontalLayout.addWidget(self.multiply_vector_line_edit)
        self.multiply_vector_button = QtWidgets.QToolButton(self.multiply_vector)
        self.multiply_vector_button.setObjectName(("multiply_vector_button"))
        self.horizontalLayout.addWidget(self.multiply_vector_button)
        self.module_layout.addWidget(self.multiply_vector)

        self.multiply_vector.setTitle("Multiply Data by a Vector")
        self.choosedata_label.setText("Choose data: ")
        self.multiply_vector_label.setText("Vector file: ")
        self.multiply_vector_line_edit.setText("*.csv")
        self.multiply_vector_button.setText("...")
        self.multiply_vector_line_edit.textChanged.connect(lambda: self.multiply_vector_params())
        self.vector_choosedata.currentIndexChanged.connect(lambda: self.multiply_vector_params())
        self.multiply_vector_button.clicked.connect(lambda: self.on_getDataButton_clicked(self.multiply_vector_line_edit))
        self.set_multiply_vector_params()

    def set_multiply_vector_params(self):
        if self.arg_list is None:
            self.multiply_vector_line_edit.setText("*.csv")
        else:
            self.multiply_vector_line_edit.setText(self.arg_list[1])
            index = self.vector_choosedata.findText(str(self.arg_list[0]))  # findText 'unknown' or 'known'
            if index is not -1:  # if it's there choose it based on the returned index
                self.vector_choosedata.setCurrentIndex(index)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Vector Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
