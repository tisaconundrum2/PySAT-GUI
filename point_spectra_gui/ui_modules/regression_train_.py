from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars
from point_spectra_gui.ui_modules.regressionMethods import *


class regression_train_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.algorithm_list = ['Choose an algorithm',  # 0
                               'PLS',  # 1
                               'GP',  # 2
                               'OLS',  # 3
                               'OMP',  # 4
                               'Lasso',  # 5
                               'Elastic Net',  # 6
                               'Ridge',  # 7
                               'Bayesian Ridge',  # 8
                               'ARD',  # 9
                               'LARS',  # 10
                               'Lasso LARS',  # 11
                               'SVR',  # 12
                               'KRR',  # 13
                               'More to come...']
        self.isRestore = False
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
        if self.arg_list is not None:
            self.isRestore = True
        self.regression_ui()  # start the regression UI. create our submodule
        self.set_regression_parameters()  # Do it the first time to get data
        # self.regression_ransac_checkbox.toggled.connect(  #
        #     lambda: self.make_ransac_widget(self.regression_ransac_checkbox.isChecked()))  #
        self.regression_choosealg.currentIndexChanged.connect(  #
            lambda: self.make_regression_widget(self.regression_choosealg.currentText()))  #
        self.get_regression_parameters()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.regression_train)

    def get_regression_parameters(self):
        self.method = self.regression_choosealg.currentText()
        self.datakey = self.regression_choosedata.currentText()
        self.xvars = [str(x.text()) for x in self.regression_train_choosex.selectedItems()]
        self.yvars = [('comp', str(y.text())) for y in self.regression_train_choosey.selectedItems()]
        self.yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        self.params = {}
        self.ransacparams = {}
        self.kws = {}
        try:
            self.modelkey = self.method + ' - ' + str(self.yvars[0][-1]) + ' (' + str(self.yrange[0]) + '-' + str(
                self.yrange[1]) + ') '
        except:
            self.modelkey = self.method
        try:

        except:
            pass
        self.kws = {'self.modelkey': self.modelkey}
        # if self.regression_ransac_checkbox.isChecked():
        #     lossval = self.ransac_widget.ransac_lossfunc_combobox.currentText()
        #     if lossval == 'Squared Error':
        #         loss = 'squared_loss'
        #     if lossval == 'Absolute Error':
        #         loss = 'absolute_loss'
        #     ransacparams = {'residual_threshold': self.ransac_widget.ransac_thresh_spin.value(),
        #                     'loss': loss}
        ui_list = "do_regression_train"
        fun_list = "do_regression_train"

        args = [self.datakey, self.xvars, self.yvars, self.yrange, self.method, self.params, self.ransacparams]
        # TODO Stop the module when there are ill-formed parameters!
        self.r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, self.kws, self.r, self.ui_id)

    def set_regression_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)
        if self.arg_list is not None:
            try:
                self.datakey = self.arg_list[0]
                self.xvars = self.arg_list[1]
                self.yvars = self.arg_list[2]
                yrange = self.arg_list[3]
                method = self.arg_list[4]
                params = self.arg_list[5]
                ransacparams = self.arg_list[6]

                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                self.regression_choosedata.setCurrentIndex(self.regression_choosedata.findText(str(self.datakey)))
                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                change_combo_list_vars(self.regression_train_choosex,
                                       self.restr_list['regression_train_choosex_values'])

                try:
                    self.regression_train_choosex.setCurrentItem(
                        self.regression_train_choosex.findItems(self.xvars[0], QtCore.Qt.MatchExactly)[0])
                    self.regression_train_choosey.setCurrentItem(
                        self.regression_train_choosey.findItems(self.yvars[0][1], QtCore.Qt.MatchExactly)[0])
                except:
                    pass
                self.yvarmin_spin.setValue(yrange[0])
                self.yvarmax_spin.setValue(yrange[1])
                self.regression_choosealg.setCurrentIndex(self.regression_choosealg.findText(str(method)))
                self.make_regression_widget(self.regression_choosealg.currentText(), params=params)
            except:
                pass

    def make_ransac_widget(self, isChecked):
        if not isChecked:
            self.ransac_widget.deleteLater()
        else:
            self.ransac_widget = QtWidgets.QWidget()
            self.ransac_widget.ransac_widget_hlayout = QtWidgets.QHBoxLayout(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_hlayout = QtWidgets.QHBoxLayout()
            self.ransac_widget.ransac_lossfunc_label = QtWidgets.QLabel(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_label.setText('Loss function:')
            self.ransac_widget.ransac_lossfunc_label.setObjectName("self.ransac_lossfunc_label")
            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_label)
            self.ransac_widget.ransac_lossfunc_combobox = QtWidgets.QComboBox(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_combobox.addItem(("Squared Error"))
            self.ransac_widget.ransac_lossfunc_combobox.addItem(("Absolute Error"))
            self.ransac_widget.ransac_lossfunc_combobox.setObjectName("self.ransac_lossfunc_combobox")
            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_combobox)
            self.ransac_widget.ransac_lossfunc_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                              QtWidgets.QSizePolicy.Minimum)
            self.ransac_widget.ransac_lossfunc_hlayout.addItem(self.ransac_widget.ransac_lossfunc_spacer)
            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_lossfunc_hlayout)
            self.ransac_widget.ransac_thresh_hlayout = QtWidgets.QHBoxLayout()
            self.ransac_widget.ransac_thresh_label = QtWidgets.QLabel(self.ransac_widget)
            self.ransac_widget.ransac_thresh_label.setText('Threshold:')
            self.ransac_widget.ransac_thresh_label.setObjectName("self.ransac_thresh_label")
            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_label)
            self.ransac_widget.ransac_thresh_spin = QtWidgets.QDoubleSpinBox(self.ransac_widget)
            self.ransac_widget.ransac_thresh_spin.setObjectName("self.ransac_thresh_spin")
            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_spin)
            self.ransac_widget.ransac_thresh_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                            QtWidgets.QSizePolicy.Minimum)
            self.ransac_widget.ransac_thresh_hlayout.addItem(self.ransac_widget.ransac_thresh_spacer)
            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_thresh_hlayout)
            self.ransac_widget.setObjectName("ransac_widget")
            self.ransac_hlayout.addWidget(self.ransac_widget)

            self.ransac_widget.ransac_lossfunc_combobox.currentIndexChanged.connect(
                lambda: self.get_regression_parameters())
            self.ransac_widget.ransac_thresh_spin.valueChanged.connect(lambda: self.get_regression_parameters())

    def make_regression_widget(self, alg, params=None):
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtWidgets.QWidget()

        if alg == self.algorithm_list[1]:
            self.pls = PLS.Ui_Form()
            self.pls.setupUi(self.reg_widget)
            # detect a change in the UI

        if alg == self.algorithm_list[2]:
            self.gp = GP.Ui_Form()
            self.gp.setupUi(self.reg_widget)

        if alg == self.algorithm_list[3]:
            self.ols = OLS.Ui_Form()
            self.ols.setupUi(self.reg_widget)

            self.ols.fitInterceptCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            if params is not None:
                self.reg_widget.ols_intercept_checkbox.setChecked(params['fit_intercept'])

        if alg == self.algorithm_list[4]:
            self.omp = OMP.Ui_Form()
            self.omp.setupUi(self.reg_widget)

            self.omp.fitInterceptCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.omp.optimizeWCrossValidationCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.omp.numOfNonZeroCoeffsSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.omp.fitInterceptCheckBox.setChecked(params['fit_intercept'])
                self.omp.optimizeWCrossValidationCheckBox.setChecked(params['CV'])
                self.omp.numOfNonZeroCoeffsSpinBox.setValue(params['n_nonzero_coefs'])

        if alg == self.algorithm_list[5]:
            self.lasso = Lasso.Ui_Form()
            self.lasso.setupUi(self.reg_widget)

            self.lasso.alphaDoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.lasso.maxNumOfIterationsSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.lasso.toleranceDoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.lasso.fitInterceptCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.lasso.forcePositiveCoefficientsCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.lasso.optimizeWCrossValidaitonCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.lasso_alpha.setValue(params['alpha'])
                self.reg_widget.lasso_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.lasso_tol.setValue(params['tol'])
                self.reg_widget.lasso_max.setValue(params['max_iter'])
                self.reg_widget.lasso_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.lasso_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[6]:
            self.elastic_net = ElasticNet.Ui_Form()
            self.elastic_net.setupUi(self.reg_widget)

            self.elastic_net.alphaDoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.elastic_net.l1RatioDoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.elastic_net.maxNumOfIterationsSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.elastic_net.toleranceDoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.elastic_net.fitInterceptCheckBox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.elastic_net.forcePositiveCoefficientsCheckBox.stateChanged.connect(
                lambda: self.get_regression_parameters())
            self.elastic_net.optimizeWCrossValidationCheckBox.stateChanged.connect(
                lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.elnet_alpha.setValue(params['alpha'])
                self.reg_widget.elnet_l1.setValue(params['l1_ratio'])
                self.reg_widget.elnet_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.elnet_tol.setValue(params['tol'])
                self.reg_widget.elnet_max.setValue(params['max_iter'])
                self.reg_widget.elnet_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.elnet_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[7]:
            self.ridge = Ridge.Ui_Form()
            self.ridge.setupUi(self.reg_widget)

        if alg == self.algorithm_list[8]:
            self.br = bayesian_ridge.Ui_Form()
            self.br.setupUi(self.reg_widget)

            self.br.alpha1DoubleSpinBox.valueChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.ridge_alpha.setValue(params['alpha'])
                self.reg_widget.ridge_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.ridge_tol.setValue(params['tol'])
                self.reg_widget.ridge_max.setValue(params['max_iter'])
                self.reg_widget.ridge_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[9]:
            self.ard = ARD.Ui_Form()
            self.ard.setupUi(self.reg_widget)
            Qtickle.isGuiChanged(self.ard, self.get_regression_parameters())

        if alg == self.algorithm_list[10]:
            self.lars = LARS.Ui_Form()
            self.lars.setupUi(self.reg_widget)

        if alg == self.algorithm_list[11]:
            self.lassoLARS = LassoLARS.Ui_Form()
            self.lassoLARS.setupUi(self.reg_widget)

            # self.reg_widget.lassoLARS_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.lassoLARS_alpha.setValue(params['alpha'])
                self.reg_widget.lassoLARS_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.lassoLARS_max.setValue(params['max_iter'])
                self.reg_widget.lassoLARS_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.lassoLARS_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[12]:
            self.svr = SVR.Ui_Form()
            self.svr.setupUi(self.reg_widget)

        if alg == self.algorithm_list[13]:
            self.krr = KRR.Ui_Form()
            self.krr.setupUi(self.reg_widget)

        self.reg_widget.setObjectName("reg_widget")
        self.regression_vlayout.addWidget(self.reg_widget)
        self.get_regression_parameters()

    def regression_ui(self):
        self.regression_train = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression_train.setFont(font)
        self.regression_vlayout = QtWidgets.QVBoxLayout(self.regression_train)
        # choose data
        self.regression_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_train_choosedata_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosedata_label.setText("Choose data:")
        self.regression_train_choosedata_label.setObjectName("regression_train_choosedata_label")
        self.regression_choosedata_hlayout.addWidget(self.regression_train_choosedata_label)
        datachoices = self.pysat_fun.datakeys
        datachoices = [i for i in datachoices if i != 'CV Results']  # prevent CV results from showing up as an option

        self.regression_choosedata = make_combobox(datachoices)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        # choose variables
        self.regression_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosexvars_vlayout = QtWidgets.QVBoxLayout()
        self.regression_chooseyvars_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosevars_hlayout.addLayout(self.regression_choosexvars_vlayout)
        self.regression_choosevars_hlayout.addLayout(self.regression_chooseyvars_vlayout)
        # choose x variables
        self.regression_train_choosex_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosex_label.setText('X variable:')
        self.regression_train_choosex_label.setObjectName("regression_train_choosex_label")
        self.regression_choosexvars_vlayout.addWidget(self.regression_train_choosex_label)
        self.regression_train_choosex = make_listwidget(self.xvar_choices())
        self.regression_train_choosex.setObjectName("regression_train_choosex")
        self.regression_choosexvars_vlayout.addWidget(self.regression_train_choosex)

        # choose y variables
        self.regression_train_choosey_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosey_label.setText('Y variable:')
        self.regression_train_choosey_label.setObjectName("regression_train_choosey_label")
        self.regression_chooseyvars_vlayout.addWidget(self.regression_train_choosey_label)
        if self.isRestore == True:
            self.regression_train_choosey = make_listwidget([])
        else:
            self.regression_train_choosey = make_listwidget(self.yvar_choices())
        # TODO add ability to select multiple items
        # self.regression_train_choosey.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.regression_train_choosey.setObjectName("regression_train_choosey")
        self.regression_chooseyvars_vlayout.addWidget(self.regression_train_choosey)
        self.regression_yvarlimits_hlayout = QtWidgets.QHBoxLayout()
        self.yvarmin_label = QtWidgets.QLabel(self.regression_train)
        self.yvarmin_label.setText('Min:')
        self.yvarmin_label.setObjectName("yvarmin_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox()
        # TODO: eventually we may want the ability to handle values outside 0-100 for regressions not dealing with wt.%
        self.yvarmin_spin.setMaximum(99999)
        self.yvarmin_spin.setMinimum(0)
        self.yvarmin_label.setObjectName("yvarmin_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin.setObjectName("yvarmin_spin")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_spin)

        self.yvarmax_label = QtWidgets.QLabel(self.regression_train)
        self.yvarmax_label.setText('Max:')
        self.yvarmax_label.setObjectName("yvarmax_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmax_spin.setMaximum(99999)
        self.yvarmax_spin.setMinimum(0)
        self.yvarmax_spin.setValue(100)
        self.yvarmax_label.setObjectName("yvarmax_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin.setObjectName("yvarmax_spin")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_spin)
        self.regression_chooseyvars_vlayout.addLayout(self.regression_yvarlimits_hlayout)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosevars_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosevars_hlayout)

        # ransac options
        # self.ransac_hlayout = QtWidgets.QHBoxLayout()
        # self.regression_ransac_checkbox = QtWidgets.QCheckBox(self.regression_train)
        # self.regression_ransac_checkbox.setText('RANSAC')
        # self.ransac_hlayout.addWidget(self.regression_ransac_checkbox)
        # self.regression_vlayout.addLayout(self.ransac_hlayout)

        # choose regression algorithm
        self.regression_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosealg_label = QtWidgets.QLabel(self.regression_train)
        self.regression_choosealg_label.setObjectName("regression_choosealg_label")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_alg_choices = self.algorithm_list
        self.regression_choosealg = make_combobox(self.regression_alg_choices)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName("regression_choosealg")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        regression_choosealg_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(regression_choosealg_spacer)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.regression_train.setObjectName("regression_train")
        self.module_layout.addWidget(self.regression_train)
        self.regression_train.raise_()
        self.regression_train.setTitle(("Regression - Train"))

    def connectWidgets(self):
        self.regression_choosedata.currentIndexChanged.connect(lambda: self.get_regression_parameters())
        self.regression_choosealg.currentIndexChanged.connect(lambda: self.get_regression_parameters())
        self.regression_train_choosex.currentItemChanged.connect(lambda: self.get_regression_parameters())
        self.regression_train_choosey.currentItemChanged.connect(lambda: self.get_regression_parameters())
        self.yvarmin_spin.valueChanged.connect(lambda: self.get_regression_parameters())
        self.yvarmax_spin.valueChanged.connect(lambda: self.get_regression_parameters())
        self.regression_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.regression_train_choosey, self.yvar_choices()))
        self.regression_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.regression_train_choosex, self.xvar_choices()))

    def yvar_choices(self):
        try:
            yvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices
