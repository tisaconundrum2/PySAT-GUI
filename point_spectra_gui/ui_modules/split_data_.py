from PyQt5 import QtGui, QtCore, QtWidgets
from point_spectra_gui.gui_utils import make_combobox,change_combo_list_vars
from point_spectra_gui.ui_modules.Error_ import error_print
import inspect


class split_data_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_id = None
        self.module_layout = module_layout
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.split_data_ui()  # initiate the UI
        self.pysat_fun.set_greyed_modules(self.split_data)

    def get_split_data_parameters(self):

        datakey = self.split_data_choosedata.currentText()
        try:
            colname = self.colname_choices.currentText()
            colname = (self.vars_level0[self.vars_level1.index(colname)], colname)
        except:
            pass
        args = [datakey, colname]
        kws = {}
        ui_list = 'do_split_data'
        fun_list = 'do_split_data'
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.ui_id)

    def set_split_data_parameters(self):
        if self.arg_list is not None:
            datakey = self.arg_list[0]
            colname = self.arg_list[1]
            self.split_data_choosedata.setCurrentIndex(self.split_data_choosedata.findText(datakey))
            change_combo_list_vars(self.colname_choices,self.get_choices())
            self.colname_choices.setCurrentIndex(self.colname_choices.findText(colname[1]))

        self.get_split_data_parameters()
    def split_data_ui(self):
        self.split_data = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.split_data.setFont(font)
        self.split_data.setObjectName(("split_data"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.split_data)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.split_data_vlayout = QtWidgets.QVBoxLayout()
        self.split_data_vlayout.setContentsMargins(11, 11, 11, 11)
        self.split_data_vlayout.setSpacing(6)
        self.split_data_vlayout.setObjectName(("split_data_vlayout"))
        self.split_data_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.split_data_choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.split_data_choosedata_hlayout.setSpacing(6)
        self.split_data_choosedata_hlayout.setObjectName(("split_data_choosedata_hlayout"))
        self.split_data_choosedata_label = QtWidgets.QLabel(self.split_data)
        self.split_data_choosedata_label.setObjectName(("split_data_choosedata_label"))
        self.split_data_choosedata_hlayout.addWidget(self.split_data_choosedata_label)

        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No data has been loaded!')
            datachoices = ['No data has been loaded!']
        self.split_data_choosedata = make_combobox(datachoices)
        self.split_data_choosedata_hlayout.addWidget(self.split_data_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.split_data_choosedata_hlayout.addItem(spacerItem)

        self.split_data_vlayout.addLayout(self.split_data_choosedata_hlayout)
        self.split_data_widget = QtWidgets.QWidget(self.split_data)
        self.split_data_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.split_data_widget.setObjectName(("split_data_widget"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.split_data_widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(("horizontalLayout_2"))
        self.start_of_sentence = QtWidgets.QLabel(self.split_data_widget)
        self.start_of_sentence.setObjectName(("start_of_sentence"))
        self.horizontalLayout_2.addWidget(self.start_of_sentence)


        self.colname_choices = make_combobox(self.get_choices())
        self.horizontalLayout_2.addWidget(self.colname_choices)
        self.end_of_sentence = QtWidgets.QLabel(self.split_data_widget)
        self.end_of_sentence.setObjectName(("end_of_sentence"))
        self.horizontalLayout_2.addWidget(self.end_of_sentence)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.split_data_vlayout.addWidget(self.split_data_widget)
        self.verticalLayout.addLayout(self.split_data_vlayout)

        self.module_layout.addWidget(self.split_data)

        self.split_data.setTitle("Split Dataset")
        self.split_data_choosedata_label.setText("Choose data: ")
        self.start_of_sentence.setText("Split on unique values of ")

        self.end_of_sentence.setText("")
        self.set_split_data_parameters()

        self.colname_choices.currentIndexChanged.connect(lambda: self.get_split_data_parameters())
        self.split_data_choosedata.currentIndexChanged.connect(lambda: self.get_split_data_parameters())
        self.split_data_choosedata.currentIndexChanged.connect(lambda:
                                                               change_combo_list_vars(self.colname_choices,
                                                                self.get_choices()))

    def get_choices(self):
        try:
            self.vars_level0 = self.pysat_fun.data[
                self.split_data_choosedata.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[
                self.split_data_choosedata.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])

            colnamechoices = self.vars_level1

        except:
            colnamechoices = self.pysat_fun.data[self.split_data_choosedata.currentText()].columns.values
        colnamechoices = [i for i in colnamechoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        return colnamechoices