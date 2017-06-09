from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, change_combo_list_vars
from point_spectra_gui.ui_modules.Error_ import error_print
import inspect
import numpy as np


class removerows_:
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
        self.removerows_ui()  # initiate the UI
        self.set_removerows_parameters()
        self.get_removerows_parameters()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.removerows)

    def get_removerows_parameters(self):
        datakey = self.removerows_choosedata.currentText()
        try:
            colname = self.colname_choices.currentText()
            colname = (self.vars_level0[self.vars_level1.index(colname)], colname)
        except:
            pass
        value = self.rowval_choices.currentText()
        args = [datakey, colname, value]
        kws = {}
        ui_list = 'do_removerows'
        fun_list = 'removerows'
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_removerows_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guirestore(self.restr_list)

    def removerows_ui(self):
        self.removerows = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removerows.setFont(font)
        self.removerows.setObjectName(("removerows"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.removerows)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.removerows_vlayout = QtWidgets.QVBoxLayout()
        self.removerows_vlayout.setContentsMargins(11, 11, 11, 11)
        self.removerows_vlayout.setSpacing(6)
        self.removerows_vlayout.setObjectName(("removerows_vlayout"))
        self.removerows_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.removerows_choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.removerows_choosedata_hlayout.setSpacing(6)
        self.removerows_choosedata_hlayout.setObjectName(("removerows_choosedata_hlayout"))
        self.removerows_choosedata_label = QtWidgets.QLabel(self.removerows)
        self.removerows_choosedata_label.setObjectName(("removerows_choosedata_label"))
        self.removerows_choosedata_hlayout.addWidget(self.removerows_choosedata_label)

        datachoices = self.pysat_fun.datakeys
        
            
            
        self.removerows_choosedata = make_combobox(datachoices)
        self.removerows_choosedata_hlayout.addWidget(self.removerows_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.removerows_choosedata_hlayout.addItem(spacerItem)

        self.removerows_vlayout.addLayout(self.removerows_choosedata_hlayout)
        self.removerows_widget = QtWidgets.QWidget(self.removerows)
        self.removerows_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.removerows_widget.setObjectName(("removerows_widget"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.removerows_widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(("horizontalLayout_2"))
        self.start_of_sentence = QtWidgets.QLabel(self.removerows_widget)
        self.start_of_sentence.setObjectName(("start_of_sentence"))
        self.horizontalLayout_2.addWidget(self.start_of_sentence)

        self.colname_choices = make_combobox(self.get_colname_choices())
        self.horizontalLayout_2.addWidget(self.colname_choices)
        self.end_of_sentence = QtWidgets.QLabel(self.removerows_widget)
        self.end_of_sentence.setObjectName(("end_of_sentence"))
        self.horizontalLayout_2.addWidget(self.end_of_sentence)
        self.rowval_choices = make_combobox(self.get_rowval_choices())
        self.horizontalLayout_2.addWidget(self.rowval_choices)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.removerows_vlayout.addWidget(self.removerows_widget)
        self.verticalLayout.addLayout(self.removerows_vlayout)

        self.module_layout.addWidget(self.removerows)

        self.removerows.setTitle("Remove Rows")
        self.removerows_choosedata_label.setText("Choose data: ")
        self.start_of_sentence.setText("Remove rows where ")

        self.end_of_sentence.setText("is ")
        self.set_removerows_parameters()

    def connectWidgets(self):
        self.colname_choices.currentIndexChanged.connect(lambda: self.get_removerows_parameters())

        self.removerows_choosedata.currentIndexChanged.connect(lambda: self.get_removerows_parameters())
        self.removerows_choosedata.currentIndexChanged.connect(lambda:
                                                               change_combo_list_vars(self.colname_choices,
                                                                                      self.get_colname_choices()))
        self.rowval_choices.currentIndexChanged.connect(lambda: self.get_removerows_parameters())
        self.colname_choices.currentIndexChanged.connect(lambda: change_combo_list_vars(self.rowval_choices,
                                                                                        self.get_rowval_choices()))

    def get_colname_choices(self):
        try:
            self.vars_level0 = self.pysat_fun.data[
                self.removerows_choosedata.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[
                self.removerows_choosedata.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])

            colnamechoices = self.vars_level1

        except:
            colnamechoices = self.pysat_fun.data[self.removerows_choosedata.currentText()].columns.values
        colnamechoices = [i for i in colnamechoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        return colnamechoices

    def get_rowval_choices(self):
        try:
            colname = self.colname_choices.currentText()
            colname = (self.vars_level0[self.vars_level1.index(colname)], colname)
            choices = np.unique(self.pysat_fun.data[self.removerows_choosedata.currentText()].df[colname])
            choices = [str(i) for i in choices]
            choices.append('Null')
        except:
            choices = ['-']
        return choices
