from PyQt5 import QtGui, QtCore, QtWidgets
from point_spectra_gui.gui_utils import make_combobox
from point_spectra_gui.ui_modules import error_print, Qtickle


class peak_area_:
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
        self.peak_area_ui()
        self.set_peak_area_params()
        self.peak_area_params()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.peak_area)

    def peak_area_params(self):
        datakey = self.peak_area_choosedata.currentText()
        peaks_mins_file = self.peak_area_line_edit.text()
        if peaks_mins_file=="None (calculate from average spectrum)":
            peaks_mins_file=None
        ui_list = "do_peak_area"
        fun_list = "do_peak_area"
        args = [datakey, peaks_mins_file]
        kws = {}
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def peak_area_ui(self):
        self.peak_area = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.peak_area.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.peak_area)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)

        self.choosedata_label = QtWidgets.QLabel(self.peak_area)
        self.choosedata_label.setObjectName("choosedata_label")
        self.horizontalLayout.addWidget(self.choosedata_label)
        datachoices = self.pysat_fun.datakeys
        
            
            
        self.peak_area_choosedata = make_combobox(datachoices)
        self.peak_area_choosedata.setObjectName("peak_area_choosedata")
        self.horizontalLayout.addWidget(self.peak_area_choosedata)

        self.peak_area_label = QtWidgets.QLabel(self.peak_area)
        self.peak_area_label.setObjectName("peak_area_label")
        self.horizontalLayout.addWidget(self.peak_area_label)
        self.peak_area_line_edit = QtWidgets.QLineEdit(self.peak_area)
        self.peak_area_line_edit.setReadOnly(True)
        self.peak_area_line_edit.setObjectName("peak_area_line_edit")
        self.horizontalLayout.addWidget(self.peak_area_line_edit)
        self.peak_area_button = QtWidgets.QToolButton(self.peak_area)
        self.peak_area_button.setObjectName("peak_area_button")
        self.horizontalLayout.addWidget(self.peak_area_button)
        self.peak_area.setObjectName("peak_area")
        self.module_layout.addWidget(self.peak_area)

        self.peak_area.setTitle("Peak Areas")
        self.choosedata_label.setText("Choose data: ")
        self.peak_area_label.setText("Peaks and minima file: ")
        self.peak_area_line_edit.setText("None (calculate from average spectrum)")
        self.peak_area_button.setText("...")

    def connectWidgets(self):
        self.peak_area_line_edit.textChanged.connect(lambda: self.peak_area_params())
        self.peak_area_choosedata.currentIndexChanged.connect(lambda: self.peak_area_params())
        self.peak_area_button.clicked.connect(lambda: self.on_getDataButton_clicked(self.peak_area_line_edit))

    def set_peak_area_params(self):
        if self.arg_list is None:
            self.peak_area_line_edit.setText("None (calculate from average spectrum)")
        else:
            self.qtickle.guirestore(self.restr_list)
            peaks_mins_file=self.arg_list[1]
            if peaks_mins_file == None:
                peaks_mins_file = "None (calculate from average spectrum)"

            self.peak_area_line_edit.setText(peaks_mins_file)
            index = self.peak_area_choosedata.findText(str(self.arg_list[0]))  # findText 'unknown' or 'known'
            if index is not -1:  # if it's there choose it based on the returned index
                self.peak_area_choosedata.setCurrentIndex(index)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open peaks and minima File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("None (calculate from average spectrum)")
