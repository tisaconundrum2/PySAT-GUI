from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars
import numpy as np

class cal_tran_:
    """

    """

    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
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
        self.cal_tran_ui()
        self.set_cal_tran_params()
        self.get_cal_tran_params()
        self.pysat_fun.set_greyed_modules(self.cal_tran)

    def set_cal_tran_params(self):  # TODO this function should be rewritten to accomodate for restoration
        pass
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)


    def get_cal_tran_params(self):
        data_transform = self.CalTran_dataSetTransform.currentText()
        data_ref = self.CalTran_dataSetRef.currentText()
        method = self.methodComboBox.currentText()
        colmatch_ref = self.col_choices_ref.currentText()
        colmatch_transform = self.col_choices_transform.currentText()

        args = [data_transform, data_ref, colmatch_ref, colmatch_transform,method]
        kws = {}
        ui_list = 'do_cal_tran'
        fun_list = 'do_cal_tran'
        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)
    def make_cal_tran_widget(self,method,params=None):
        print(method)
        try:
            self.cal_tran_widget.deleteLater()
        except:
            pass
        self.cal_tran_widget = QtWidgets.QWidget()

        if alg == 'LRA - Low Rank Alignment':
            self.pls = PLS.Ui_Form()
            self.pls.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.pls, self.get_regression_parameters)


    def cal_tran_ui(self):
        self.cal_tran = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cal_tran.setFont(font)

        self.CalTran_vLayout = QtWidgets.QVBoxLayout(self.cal_tran)
        self.CalTran_vLayout.setObjectName("vlayout")
        #self.CalTran_vLayout.setContentsMargins(11, 11, 11, 11)
        #self.CalTran_vLayout.setSpacing(6)

        self.cal_tran_layout = QtWidgets.QFormLayout(self.cal_tran)
        datachoices = self.pysat_fun.datakeys

        self.CalTran_dataSetRefLabel = QtWidgets.QLabel(self.cal_tran)
        self.CalTran_dataSetRefLabel.setObjectName("CalTran_dataSetRefLabel")
        self.CalTran_dataSetRefLabel.setText('Reference Data Set:')
        self.cal_tran_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetRefLabel)
        self.CalTran_dataSetRef = make_combobox(datachoices)
        self.cal_tran_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetRef)

        self.CalTran_columnToMatchRef_Label = QtWidgets.QLabel(self.cal_tran)
        self.CalTran_columnToMatchRef_Label.setObjectName("CalTran_columnToMatchRef_Label")
        self.CalTran_columnToMatchRef_Label.setText('Column to match:')
        self.cal_tran_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CalTran_columnToMatchRef_Label)
        self.col_choices_ref = make_combobox([''])
        self.col_choices_ref.setObjectName("col_choices_ref")
        change_combo_list_vars(self.col_choices_ref,
                               self.get_choices(self.CalTran_dataSetRef.currentText()))
        self.cal_tran_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.col_choices_ref)

        self.CalTran_dataSetTransformLabel = QtWidgets.QLabel(self.cal_tran)
        self.CalTran_dataSetTransformLabel.setObjectName("CalTran_dataSetTransformLabel")
        self.CalTran_dataSetTransformLabel.setText('Data set to transform:')
        self.cal_tran_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CalTran_dataSetTransformLabel)
        self.CalTran_dataSetTransform = make_combobox(datachoices)
        self.cal_tran_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CalTran_dataSetTransform)
        self.CalTran_columnToMatchTransform_Label = QtWidgets.QLabel(self.cal_tran)
        self.CalTran_columnToMatchTransform_Label.setObjectName("CalTran_columnToMatchTransform_Label")
        self.CalTran_columnToMatchTransform_Label.setText('Column to match:')
        self.cal_tran_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.CalTran_columnToMatchTransform_Label)

        self.col_choices_transform = make_combobox([''])
        self.col_choices_transform.setObjectName("col_choices_transform")

        change_combo_list_vars(self.col_choices_transform, self.get_choices(self.CalTran_dataSetTransform.currentText()))
        self.cal_tran_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.col_choices_transform)
        self.methodLabel = QtWidgets.QLabel(self.cal_tran)
        self.methodLabel.setObjectName("methodLabel")
        self.methodLabel.setText('Method:')
        self.cal_tran_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.methodLabel)
        self.methodComboBox = QtWidgets.QComboBox(self.cal_tran)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("LRA - Low Rank Alignment")
        self.methodComboBox.addItem("PDS - Piecewise Direct Standardization")
        self.cal_tran_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.methodComboBox)
        self.CalTran_vLayout.addLayout(self.cal_tran_layout)
        self.module_layout.addWidget(self.cal_tran)
        self.cal_tran.raise_()
        self.cal_tran.setTitle(("Calibration Transfer"))

        self.CalTran_dataSetTransform.activated[int].connect(
            lambda: change_combo_list_vars(self.col_choices_transform, self.get_choices(self.CalTran_dataSetTransform.currentText())))
        self.CalTran_dataSetRef.activated[int].connect(
            lambda: change_combo_list_vars(self.col_choices_ref,
                                           self.get_choices(self.CalTran_dataSetRef.currentText())))
        self.CalTran_dataSetTransform.currentIndexChanged.connect(lambda: self.get_cal_tran_params())
        self.CalTran_dataSetRef.currentIndexChanged.connect(lambda: self.get_cal_tran_params())
        self.col_choices_ref.currentIndexChanged.connect(lambda: self.get_cal_tran_params())
        self.col_choices_transform.currentIndexChanged.connect(lambda: self.get_cal_tran_params())
        self.methodComboBox.currentIndexChanged.connect(lambda: self.get_cal_tran_params())

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.pysat_fun.data[self.CalTran_dataSetTransform.currentText()].df.columns.levels[0].values
            except:
                xvarchoices = self.pysat_fun.data[self.CalTran_dataSetTransform.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices


    def get_choices(self,dataset):
        try:
            self.vars_level0 = self.pysat_fun.data[dataset].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[dataset].df.columns.get_level_values(1)
            self.vars_level1 = self.vars_level1[self.vars_level0 != 'wvl']
            self.vars_level0 = self.vars_level0[self.vars_level0 != 'wvl']
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'masked'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'masked'])
            try:
                self.vars_level0 = [i for i in self.vars_level0 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            try:
                self.vars_level1 = [i for i in self.vars_level1 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            choices = self.vars_level1

        except:
            try:
                choices = self.pysat_fun.data[dataset].columns.values
            except:
                choices = ['No valid choices']
        return choices