from PyQt4 import QtCore, QtGui
from pysat.utils.gui_utils import make_combobox
from PYSAT_UI_MODULES.Error_ import error_print

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


class dim_reduction_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.main()

    def main(self):
        # TODO add function param call here
        
        self.pysat_fun.set_fun_list(self.pysat_fun.do_dim_red)
        self.pysat_fun.set_arg_list([])
        self.pysat_fun.set_kw_list({})
        self.pysat_fun.set_greyed_modules({})
        self.dim_reduction_ui()
        self.pysat_fun.set_greyed_modules(self.dim_reduction, True)
        
        # TODO add try and except here
#        try:
#            # arg_list.append(['known data', 5, 2, ('meta', 'SiO2')])
#            self.create_folds.clicked.connect(
#                lambda: self.pysat_fun.arg_list.append(['known_data', 5, 2, ('meta', 'SiO2')]))
#        except:
#            print('There was a problem with creating stratified folds...')

    def get_dim_red_params(self):
        datakey=self.dim_reduction_choose_data.currentText()
        method=self.dim_red_choosealg.currentText()
        if method=='PCA':
            params={'nc':self.dim_red_widget.pca_nc_spinbox.value()}
        if method=='ICA':
            params = {'nc': self.dim_red_widget.ica_nc_spinbox.value()}
        if method=='ICA-JADE':
            params = {'nc': self.dim_red_widget.ica_jade_nc_spinbox.value()}

        args=[datakey,method,params]
        kws={}
        self.pysat_fun.set_arg_list(args,replacelast=True)
        self.pysat_fun.set_kw_list(kws,replacelast=True)


    def make_dim_red_widget(self,method):
        print(alg)
        try:
            self.dim_red_widget.deleteLater()
        except:
            pass
        self.dim_red_widget = QtGui.QWidget()
        if alg == 'PCA':
            self.dim_red_widget.pca_hlayout = QtGui.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.pca_nc_label = QtGui.QLabel(self.dim_red_widget)
            self.dim_red_widget.pca_nc_label.setText('# of components:')
            self.dim_red_widget.pca_hlayout.addWidget(self.dim_red_widget.pca_nc_label)
            self.dim_red_widget.pca_nc_spinbox = QtGui.QSpinBox(self.dim_red_widget)
            self.dim_red_widget.pca_hlayout.addWidget(self.dim_red_widget.pca_nc_spinbox)
            self.dim_red_widget.pca_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                           QtGui.QSizePolicy.Minimum)
            self.dim_red_widget.pca_hlayout.addItem(self.dim_red_widget.pca_spacer)
            self.dim_red_widget.pca_nc_spinbox.valueChanged.connect(lambda: self.get_dim_red_parameters())
        if alg == 'ICA':
            self.dim_red_widget.ica_hlayout = QtGui.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.ica_nc_label = QtGui.QLabel(self.dim_red_widget)
            self.dim_red_widget.ica_nc_label.setText('# of components:')
            self.dim_red_widget.ica_hlayout.addWidget(self.dim_red_widget.ica_nc_label)
            self.dim_red_widget.ica_nc_spinbox = QtGui.QSpinBox(self.dim_red_widget)
            self.dim_red_widget.ica_hlayout.addWidget(self.dim_red_widget.ica_nc_spinbox)
            self.dim_red_widget.ica_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                           QtGui.QSizePolicy.Minimum)
            self.dim_red_widget.ica_hlayout.addItem(self.dim_red_widget.ica_spacer)
            self.dim_red_widget.ica_nc_spinbox.valueChanged.connect(lambda: self.get_dim_red_parameters())
        if alg == 'ICA-JADE':
            self.dim_red_widget.ica_jade_hlayout = QtGui.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.ica_jade_nc_label = QtGui.QLabel(self.dim_red_widget)
            self.dim_red_widget.ica_jade_nc_label.setText('# of components:')
            self.dim_red_widget.ica_jade_hlayout.addWidget(self.dim_red_widget.ica_jade_nc_label)
            self.dim_red_widget.ica_jade_nc_spinbox = QtGui.QSpinBox(self.dim_red_widget)
            self.dim_red_widget.ica_jade_hlayout.addWidget(self.dim_red_widget.ica_jade_nc_spinbox)
            self.dim_red_widget.ica_jade_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                           QtGui.QSizePolicy.Minimum)
            self.dim_red_widget.ica_jade_hlayout.addItem(self.dim_red_widget.ica_jade_spacer)
            self.dim_red_widget.ica_jade_nc_spinbox.valueChanged.connect(lambda: self.get_dim_red_parameters())

        self.dim_reduction_vlayout.addWidget(self.dim_red_widget)
        self.get_dim_red_params()

    def dim_reduction_ui(self):
        self.dim_reduction = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dim_reduction.setFont(font)
        self.dim_reduction.setObjectName(_fromUtf8("Dimensionality Reduction"))
        self.dim_reduction_vlayout = QtGui.QVBoxLayout(self.dim_reduction)
        self.dim_reduction_vlayout.setObjectName(_fromUtf8("dim_reduction_vlayout"))
        #choose data set to apply dim reduction to
        self.dim_reduction_choose_data_label = QtGui.QLabel(self.dim_reduction)
        self.dim_reduction_choose_data_label.setObjectName(_fromUtf8("dim_reduction_choose_data_label"))
        self.dim_reduction_vlayout.addWidget(self.dim_reduction_choose_data_label)
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No data has been loaded!')
            datachoices = ['No data has been loaded!']
        self.dim_reduction_choose_data = make_combobox(datachoices)
        self.dim_reduction_vlayout.addWidget(self.dim_reduction_choose_data)

        #Choose the algorithm to apply
        self.dim_red_choosealg_label=QtGui.QLabel(self.dim_reduction)
        self.dim_reduction_vlayout.addWidget(self.dim_red_choosealg_label)
        alg_choices=['PCA','ICA','ICA-JADE']
        self.dim_red_choosealg=make_combobox(alg_choices)
        self.dim_reduction_vlayout.addWidget(self.dim_red_choosealg)


        self.verticalLayout_8.addWidget(self.dim_reduction)
        self.dim_reduction.raise_()
        self.dim_reduction.setTitle(_translate("MainWindow", "Dimensionality Reduction", None))
        self.dim_reduction_choose_data_label.setText(_translate("dim_reduction", "Choose data:", None))
        self.dim_red_choosealg_label.setText(_translate("dim_reduction", "Choose method:", None))
        self.dim_reduction_choose_data.currentIndexChanged.connect(lambda: self.get_dim_red_params())
        self.dim_red_choosealg.currentIndexChanged.connect(lambda: self.get_dim_red_params())

