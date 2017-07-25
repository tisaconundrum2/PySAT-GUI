from PyQt5 import QtGui, QtWidgets

from point_spectra_gui.gui_utils import make_combobox
from point_spectra_gui.ui_modules import Qtickle


class get_mask_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.module_layout = module_layout
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.get_mask_ui()
        self.set_mask_params()
        self.get_mask_params()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.get_mask)

    def get_mask_params(self):
        datakey = self.mask_choosedata.currentText()
        maskfile = self.get_mask_line_edit.text()
        ui_list = "do_mask"
        fun_list = "do_mask"
        args = [datakey, maskfile]
        kws = {}
        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def get_mask_ui(self):
        self.get_mask = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_mask.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_mask)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)

        self.choosedata_label = QtWidgets.QLabel(self.get_mask)
        self.choosedata_label.setObjectName("choosedata_label")
        self.horizontalLayout.addWidget(self.choosedata_label)
        datachoices = self.pysat_fun.datakeys

        self.mask_choosedata = make_combobox(datachoices)
        self.mask_choosedata.setObjectName("mask_choosedata")
        self.horizontalLayout.addWidget(self.mask_choosedata)

        self.get_mask_label = QtWidgets.QLabel(self.get_mask)
        self.get_mask_label.setObjectName("get_mask_label")
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtWidgets.QLineEdit(self.get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName("get_mask_line_edit")
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtWidgets.QToolButton(self.get_mask)
        self.get_mask_button.setObjectName("get_mask_button")
        self.horizontalLayout.addWidget(self.get_mask_button)
        self.get_mask.setObjectName("get_mask")
        self.module_layout.addWidget(self.get_mask)

        self.get_mask.setTitle("Mask Data")
        self.choosedata_label.setText("Choose data: ")
        self.get_mask_label.setText("Mask file: ")
        self.get_mask_line_edit.setText("*.csv")
        self.get_mask_button.setText("...")

    def connectWidgets(self):
        self.get_mask_line_edit.textChanged.connect(lambda: self.get_mask_params())
        self.mask_choosedata.currentIndexChanged.connect(lambda: self.get_mask_params())
        self.get_mask_button.clicked.connect(lambda: self.on_getDataButton_clicked(self.get_mask_line_edit))

    def set_mask_params(self):
        if self.arg_list is None:
            self.get_mask_line_edit.setText("*.csv")
        else:
            self.qtickle.guiRestore(self.restr_list)
            self.get_mask_line_edit.setText(self.arg_list[1])
            index = self.mask_choosedata.findText(str(self.arg_list[0]))  # findText 'unknown' or 'known'
            if index is not -1:  # if it's there choose it based on the returned index
                self.mask_choosedata.setCurrentIndex(index)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
