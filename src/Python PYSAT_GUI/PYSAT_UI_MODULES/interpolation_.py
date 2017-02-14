from PyQt4 import QtCore, QtGui
from PYSAT_UI_MODULES.Error_ import error_print
from pysat.utils.gui_utils import make_combobox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class interpolation_:
    def __init__(self, pysat_fun, verticalLayout_8, arg_list, kw_list):
        self.verticalLayout_8 = verticalLayout_8
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.pysat_fun = pysat_fun
        self.main()

    def main(self):
        self.pysat_fun.set_fun_list(self.pysat_fun.do_interp)
        self.pysat_fun.set_arg_list([])
        self.pysat_fun.set_kw_list({})
        self.pysat_fun.set_greyed_modules({})
        self.interpolation_ui()
        self.pysat_fun.set_greyed_modules(self.Interpolation, True)
        self.interpoliation_choosedata.currentIndexChanged.connect(lambda: self.get_interp_parameters())
        self.interpolation_choosedata_2.currentIndexChanged.connect(lambda: self.get_interp_parameters())

    def get_interp_parameters(self):
        key1 = self.interpoliation_choosedata.currentText()
        key2 = self.interpolation_choosedata_2.currentText()
        # arg_list.append(['unknown data','known data'])
        args = [key1, key2]
        kws = {}
        self.pysat_fun.set_arg_list(args, replacelast=True)
        self.pysat_fun.set_kw_list(kws, replacelast=True)

    def interpolation_ui(self):
        # TODO have the comboboxes called
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
        self.Interpolation = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Interpolation.setFont(font)
        self.Interpolation.setObjectName(_fromUtf8("Interpolation"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Interpolation)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.choosedata_layout = QtGui.QHBoxLayout()
        self.choosedata_layout.setMargin(11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName(_fromUtf8("choosedata_layout"))
        self.interpolation_choosedata_label = QtGui.QLabel(self.Interpolation)
        self.interpolation_choosedata_label.setObjectName(_fromUtf8("interpolation_choosedata_label"))
        self.choosedata_layout.addWidget(self.interpolation_choosedata_label)
        self.interpoliation_choosedata = make_combobox(datachoices)
        self.interpoliation_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.interpoliation_choosedata.setObjectName(_fromUtf8("interpolation_choosedata"))
        self.choosedata_layout.addWidget(self.interpoliation_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)
        self.choosedata_layout_2 = QtGui.QHBoxLayout()
        self.choosedata_layout_2.setMargin(11)
        self.choosedata_layout_2.setSpacing(6)
        self.choosedata_layout_2.setObjectName(_fromUtf8("choosedata_layout_2"))
        self.interpolation_choosedata_label_2 = QtGui.QLabel(self.Interpolation)
        self.interpolation_choosedata_label_2.setObjectName(_fromUtf8("interpolation_choosedata_label_2"))
        self.choosedata_layout_2.addWidget(self.interpolation_choosedata_label_2)
        self.interpolation_choosedata_2 = make_combobox(datachoices)
        self.interpolation_choosedata_2.setIconSize(QtCore.QSize(50, 20))
        self.interpolation_choosedata_2.setObjectName(_fromUtf8("interpolation_choosedata_2"))
        self.choosedata_layout_2.addWidget(self.interpolation_choosedata_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choosedata_layout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.choosedata_layout_2)
        self.verticalLayout_8.addWidget(self.Interpolation)

        self.Interpolation.setTitle(_translate("MainWindow", "Interpolation", None))
        self.interpolation_choosedata_label.setText(_translate("MainWindow", "Choose data: ", None))
        self.interpolation_choosedata_label_2.setText(_translate("MainWindow", "Choose data: ", None))
        self.set_interp_parameters()

    def set_interp_parameters(self):
        if self.arg_list is None:
            pass
        else:
            index = self.interpoliation_choosedata.findText(str(self.arg_list[0]))
            index2 = self.interpolation_choosedata_2.findText(str(self.arg_list[1]))
            if index is not -1 and index2 is not -1:
                self.interpoliation_choosedata.setCurrentIndex(index)
                self.interpolation_choosedata_2.setCurrentIndex(index2)
