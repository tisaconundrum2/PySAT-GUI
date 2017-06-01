from PyQt5 import QtGui, QtCore, QtWidgets
from point_spectra_gui.ui_modules.Error_ import error_print
from point_spectra_gui.gui_utils import make_combobox


class interpolation_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_id = None
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.interpolation_ui()
        self.set_parameters()
        self.get_parameters()
        self.pysat_fun.set_greyed_modules(self.Interpolation)
        self.interpoliation_choosedata.currentIndexChanged.connect(lambda: self.get_parameters())
        self.interpolation_choosedata_2.currentIndexChanged.connect(lambda: self.get_parameters())

    def interpolation_ui(self):
        # TODO have the comboboxes called
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
        self.Interpolation = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Interpolation.setFont(font)
        self.Interpolation.setObjectName("Interpolation")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Interpolation)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choosedata_layout = QtWidgets.QHBoxLayout()
        self.choosedata_layout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName("choosedata_layout")
        self.interpolation_choosedata_label = QtWidgets.QLabel(self.Interpolation)
        self.interpolation_choosedata_label.setObjectName("interpolation_choosedata_label")
        self.choosedata_layout.addWidget(self.interpolation_choosedata_label)
        self.interpoliation_choosedata = make_combobox(datachoices)
        self.interpoliation_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.interpoliation_choosedata.setObjectName("interpolation_choosedata")
        self.choosedata_layout.addWidget(self.interpoliation_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)
        self.choosedata_layout_2 = QtWidgets.QHBoxLayout()
        self.choosedata_layout_2.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout_2.setSpacing(6)
        self.choosedata_layout_2.setObjectName("choosedata_layout_2")
        self.interpolation_choosedata_label_2 = QtWidgets.QLabel(self.Interpolation)
        self.interpolation_choosedata_label_2.setObjectName("interpolation_choosedata_label_2")
        self.choosedata_layout_2.addWidget(self.interpolation_choosedata_label_2)
        self.interpolation_choosedata_2 = make_combobox(datachoices)
        self.interpolation_choosedata_2.setIconSize(QtCore.QSize(50, 20))
        self.interpolation_choosedata_2.setObjectName("interpolation_choosedata_2")
        self.choosedata_layout_2.addWidget(self.interpolation_choosedata_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.choosedata_layout_2)
        self.module_layout.addWidget(self.Interpolation)

        self.Interpolation.setTitle("Interpolation")
        self.interpolation_choosedata_label.setText("Choose data to interpolate: ")
        self.interpolation_choosedata_label_2.setText("Choose data to use as reference: ")

    def set_parameters(self):
        if self.arg_list is not None:
            index = self.interpoliation_choosedata.findText(str(self.arg_list[0]))
            index2 = self.interpolation_choosedata_2.findText(str(self.arg_list[1]))
            if index is not -1 and index2 is not -1:
                self.interpoliation_choosedata.setCurrentIndex(index)
                self.interpolation_choosedata_2.setCurrentIndex(index2)

    def get_parameters(self):
        ui_list = "do_interp"
        fun_list = "do_interp"
        key1 = self.interpoliation_choosedata.currentText()
        key2 = self.interpolation_choosedata_2.currentText()
        # arg_list.append(['unknown data','known data'])
        arg_list = [key1, key2]
        kw_list = {}
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, self.ui_id)
