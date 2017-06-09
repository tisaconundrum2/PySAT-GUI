from PyQt5 import QtGui, QtCore, QtWidgets
from pysat.utils.gui_utils import make_combobox

from Qtickle import Qtickle
from point_spectra_gui.ui_modules.Error_ import error_print
import inspect


class removenull_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.ui_id = None
        self.module_layout = module_layout
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.removenull_ui()  # initiate the UI
        self.set_removenull_parameters()
        self.get_removenull_parameters()
        self.pysat_fun.set_greyed_modules(self.removenull)

    def get_removenull_parameters(self):

        datakey = self.removenull_choosedata.currentText()
        colname = self.colname_choices.currentText()
        colname = (self.vars_level0[self.vars_level1.index(colname)], colname)

        ui_list = "do_removenull"
        fun_list = "do_removenull"
        args = [datakey, colname]
        kws = {}
        ui_list = 'do_removenull'
        fun_list = 'removenull'
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_removenull_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guirestore(self.restr_list)

    def removenull_ui(self):
        self.removenull = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removenull.setFont(font)
        self.removenull.setObjectName(("removenull"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.removenull)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.removenull_vlayout = QtWidgets.QVBoxLayout()
        self.removenull_vlayout.setContentsMargins(11, 11, 11, 11)
        self.removenull_vlayout.setSpacing(6)
        self.removenull_vlayout.setObjectName(("removenull_vlayout"))
        self.removenull_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.removenull_choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.removenull_choosedata_hlayout.setSpacing(6)
        self.removenull_choosedata_hlayout.setObjectName(("removenull_choosedata_hlayout"))
        self.removenull_choosedata_label = QtWidgets.QLabel(self.removenull)
        self.removenull_choosedata_label.setObjectName(("removenull_choosedata_label"))
        self.removenull_choosedata_hlayout.addWidget(self.removenull_choosedata_label)

        datachoices = self.pysat_fun.datakeys
        
            
            
        self.removenull_choosedata = make_combobox(datachoices)
        self.removenull_choosedata_hlayout.addWidget(self.removenull_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.removenull_choosedata_hlayout.addItem(spacerItem)

        self.removenull_vlayout.addLayout(self.removenull_choosedata_hlayout)
        self.removenull_widget = QtWidgets.QWidget(self.removenull)
        self.removenull_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.removenull_widget.setObjectName(("removenull_widget"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.removenull_widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(("horizontalLayout_2"))
        self.start_of_sentence = QtWidgets.QLabel(self.removenull_widget)
        self.start_of_sentence.setObjectName(("start_of_sentence"))
        self.horizontalLayout_2.addWidget(self.start_of_sentence)

        try:
            self.vars_level0 = self.pysat_fun.data[
                self.removenull_choosedata.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[
                self.removenull_choosedata.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])

            colnamechoices = self.vars_level1

        except:
            colnamechoices = self.pysat_fun.data[self.removenull_choosedata.currentText()].columns.values
        colnamechoices = [i for i in colnamechoices if not 'Unnamed' in i]  # remove unnamed columns from choices

        self.colname_choices = make_combobox(colnamechoices)
        self.horizontalLayout_2.addWidget(self.colname_choices)
        self.end_of_sentence = QtWidgets.QLabel(self.removenull_widget)
        self.end_of_sentence.setObjectName(("end_of_sentence"))
        self.horizontalLayout_2.addWidget(self.end_of_sentence)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.removenull_vlayout.addWidget(self.removenull_widget)
        self.verticalLayout.addLayout(self.removenull_vlayout)

        self.module_layout.addWidget(self.removenull)

        self.removenull.setTitle("Remove Null")
        self.removenull_choosedata_label.setText("Choose data: ")
        self.start_of_sentence.setText("Remove rows where ")

        self.end_of_sentence.setText("is null.")
        self.set_removenull_parameters()

        self.colname_choices.currentIndexChanged.connect(lambda: self.get_removenull_parameters())
        self.removenull_choosedata.currentIndexChanged.connect(lambda: self.get_removenull_parameters())
