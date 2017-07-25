from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars
from point_spectra_gui.ui_modules.Error_ import error_print


class write_data_:
    """

    """
    def __init__(self, pysat_fun, module_layout, arg_list,kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.pysat_fun = pysat_fun
        self.ui_id = None
        self.module_layout = module_layout
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.write_data_ui()
        self.set_write_params()
        self.get_write_params()
        self.pysat_fun.set_greyed_modules(self.write_data)

    def set_write_params(self): #TODO this function should be rewritten to accomodate for restoration
        if self.restr_list is not None:
             self.qtickle.guirestore(self.restr_list)

    def get_write_params(self):
        datakey = self.write_data_choose_data.currentText()
        filename = self.write_data_file.text()
        selected_cols=self.write_data_choosecols.selectedItems()
        cols=[]
        for selection in selected_cols:
            cols.append(selection.text())
        args = [filename, datakey,cols]
        kws = {}
        ui_list = 'do_write_data'
        fun_list = 'do_write_data'
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def write_data_ui(self):
        self.write_data = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.write_data.setFont(font)
        self.write_data_vlayout = QtWidgets.QVBoxLayout(self.write_data)

        self.write_data_choose_data_label = QtWidgets.QLabel(self.write_data)
        self.write_data_choose_data_label.setText("Choose data set to write to .csv:")
        self.write_data_choose_data_label.setObjectName("write_data_choose_data_label")
        self.write_data_vlayout.addWidget(self.write_data_choose_data_label)

        datachoices = self.pysat_fun.datakeys
        self.write_data_choose_data = make_combobox(datachoices)
        self.write_data_choose_data.setObjectName("write_data_choose_data")
        self.write_data_vlayout.addWidget(self.write_data_choose_data)

        self.write_data_choosecols_label = QtWidgets.QLabel(self.write_data)
        self.write_data_choosecols_label.setText('Variables to write:')
        self.write_data_choosecols_label.setObjectName("write_data_choosecols_label")
        self.write_data_vlayout.addWidget(self.write_data_choosecols_label)
        self.write_data_choosecols = make_listwidget(self.xvar_choices())
        self.write_data_choosecols.setObjectName("write_data_choosecols")
        self.write_data_choosecols.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.write_data_vlayout.addWidget(self.write_data_choosecols)


        self.write_data_linedit_label = QtWidgets.QLabel(self.write_data)
        self.write_data_linedit_label.setText('Specify a filename:')
        self.write_data_linedit_label.setObjectName("write_data_linedit_label")
        self.write_data_vlayout.addWidget(self.write_data_linedit_label)

        self.write_data_file = QtWidgets.QLineEdit(self.write_data)
        self.write_data_file.setText('output.csv')
        self.write_data_file.setObjectName("write_data_file")
        self.write_data_vlayout.addWidget(self.write_data_file)

        self.write_data.setObjectName("write_data")
        self.module_layout.addWidget(self.write_data)
        self.write_data.raise_()
        self.write_data.setTitle("Write to CSV")

        self.write_data_choose_data.activated[int].connect(
            lambda: change_combo_list_vars(self.write_data_choosecols, self.xvar_choices()))
        self.write_data_choose_data.currentIndexChanged.connect(lambda: self.get_write_params())
        self.write_data_file.textChanged.connect(lambda: self.get_write_params())
        self.write_data_choosecols.itemSelectionChanged.connect(lambda: self.get_write_params())

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.pysat_fun.data[self.write_data_choose_data.currentText()].df.columns.levels[0].values
            except:
                xvarchoices = self.pysat_fun.data[self.write_data_choose_data.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices