from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars


class regression_train_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.algorithm_list = ['Choose an algorithm',  # 0
                               'PLS',                  # 1
                               'GP',                   # 2
                               'OLS',                  # 3
                               'OMP',                  # 4
                               'Lasso',                # 5
                               'Elastic Net',          # 6
                               'Ridge',                # 7
                               'Bayesian Ridge',       # 8
                               'ARD',                  # 9
                               'LARS',                 # 10
                               'Lasso LARS',           # 11
                               'SVR',                  # 12
                               'KRR',                  # 13
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
        method = self.regression_choosealg.currentText()
        datakey = self.regression_choosedata.currentText()
        xvars = [str(x.text()) for x in self.regression_train_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.regression_train_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        params = {}
        ransacparams = {}
        kws = {}
        try:
            modelkey = method + ' - ' + str(yvars[0][-1]) + ' (' + str(yrange[0]) + '-' + str(yrange[1]) + ') '
        except:
            modelkey = method
        try:
            if method == 'OLS':
                params = {'fit_intercept': self.reg_widget.ols_intercept_checkbox.isChecked()}
                modelkey = modelkey + str(params)
            if method == 'OMP':
                params = {'fit_intercept': self.reg_widget.omp_intercept_checkbox.isChecked(),
                          'n_nonzero_coefs': self.reg_widget.omp_nfeatures.value(),
                          'CV': self.reg_widget.omp_cv_checkbox.isChecked()}
                modelkey = modelkey + str(params)
            if method == 'Lasso':
                params = {'alpha': self.reg_widget.lasso_alpha.value(),
                          'fit_intercept': self.reg_widget.lasso_intercept_checkbox.isChecked(),
                          'max_iter': self.reg_widget.lasso_max.value(), 'tol': self.reg_widget.lasso_tol.value(),
                          'positive': self.reg_widget.lasso_positive_checkbox.isChecked(), 'selection': 'random',
                          'CV': self.reg_widget.lasso_cv_checkbox.isChecked()}
                print(params)
            if method == 'Elastic Net':
                params = {'alpha': self.reg_widget.elnet_alpha.value(),
                          'l1_ratio': self.reg_widget.elnet_l1.value(),
                          'fit_intercept': self.reg_widget.elnet_intercept_checkbox.isChecked(),
                          'max_iter': self.reg_widget.elnet_max.value(),
                          'tol': self.reg_widget.elnet_tol.value(),
                          'positive': self.reg_widget.elnet_positive_checkbox.isChecked(),
                          'selection': 'random',
                          'CV': self.reg_widget.elnet_cv_checkbox.isChecked()}
            if method == 'Ridge':
                params = {'alpha': self.reg_widget.ridge_alpha.value(),
                          'fit_intercept': self.reg_widget.ridge_intercept_checkbox.isChecked(),
                          'max_iter': self.reg_widget.ridge_max.value(),
                          'tol': self.reg_widget.ridge_tol.value(),
                          'CV': self.reg_widget.ridge_cv_checkbox.isChecked()}
            if method == 'Bayesian Ridge':
                pass
            if method == 'ARD':
                pass
            if method == 'LARS':
                pass
            if method == 'Lasso LARS':
                params = {'alpha': self.reg_widget.lasso_alpha.value(),
                          'fit_intercept': self.reg_widget.lasso_intercept_checkbox.isChecked(),
                          'max_iter': self.reg_widget.lasso_max.value(), 'tol': self.reg_widget.lasso_tol.value(),
                          'positive': self.reg_widget.lasso_positive_checkbox.isChecked(), 'selection': 'random',
                          'CV': self.reg_widget.lasso_cv_checkbox.isChecked()}

            if method == 'SVR':
                pass
            if method == 'KRR':
                pass

            if method == 'PLS':
                params = {'n_components': self.reg_widget.pls_nc_spinbox.value(),
                          'scale': False}
                modelkey = modelkey + '(nc=' + str(params['n_components']) + ')'
                kws = {'modelkey': modelkey}
            if method == 'GP':
                params = {'reduce_dim': self.reg_widget.gp_dim_red_combobox.currentText(),
                          'n_components': self.reg_widget.gp_dim_red_nc_spinbox.value(),
                          'random_start': self.reg_widget.gp_rand_starts_spin.value(),
                          'theta0': self.reg_widget.gp_theta0_spin.value(),
                          'thetaL': self.reg_widget.gp_thetaL_spin.value(),
                          'thetaU': self.reg_widget.gp_thetaU_spin.value()}

                modelkey = modelkey + str(params)

        except:
            pass
        kws = {'modelkey': modelkey}
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

        args = [datakey, xvars, yvars, yrange, method, params, ransacparams]
        # TODO Stop the module when there are ill-formed parameters!
        self.r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.r, self.ui_id)

    def set_regression_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guirestore(self.restr_list)
        if self.arg_list is not None:
            try:
                datakey = self.arg_list[0]
                xvars = self.arg_list[1]
                yvars = self.arg_list[2]
                yrange = self.arg_list[3]
                method = self.arg_list[4]
                params = self.arg_list[5]
                ransacparams = self.arg_list[6]

                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                self.regression_choosedata.setCurrentIndex(self.regression_choosedata.findText(str(datakey)))
                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                change_combo_list_vars(self.regression_train_choosex,
                                       self.restr_list['regression_train_choosex_values'])

                try:
                    self.regression_train_choosex.setCurrentItem(
                        self.regression_train_choosex.findItems(xvars[0], QtCore.Qt.MatchExactly)[0])
                    self.regression_train_choosey.setCurrentItem(
                        self.regression_train_choosey.findItems(yvars[0][1], QtCore.Qt.MatchExactly)[0])
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
            self.reg_widget.pls_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.pls_nc_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.pls_nc_label.setText('# of components:')
            self.reg_widget.pls_nc_label.setObjectName("self.pls_nc_label")
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_label)
            self.reg_widget.pls_nc_spinbox = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.pls_nc_spinbox.setObjectName("self.pls_nc_spinbox")
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_spinbox)
            self.reg_widget.pls_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                               QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.pls_hlayout.addItem(self.reg_widget.pls_spacer)
            self.reg_widget.pls_nc_spinbox.valueChanged.connect(lambda: self.get_regression_parameters())
            if params is not None:
                self.reg_widget.pls_nc_spinbox.setValue(params['n_components'])

        if alg == self.algorithm_list[2]:
            self.reg_widget = QtWidgets.QWidget()
            self.reg_widget.gp_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.gp_dim_red_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_dim_red_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_dim_red_label.setText('Choose dimensionality reduction method:')
            self.reg_widget.gp_dim_red_label.setObjectName("self.gp_dim_red_label")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_label)
            self.reg_widget.gp_dim_red_combobox = QtWidgets.QComboBox(self.reg_widget)
            self.reg_widget.gp_dim_red_combobox.addItem(("PCA"))
            self.reg_widget.gp_dim_red_combobox.addItem(("ICA"))
            self.reg_widget.gp_dim_red_combobox.setObjectName("self.gp_dim_red_combobox")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_combobox)
            self.reg_widget.gp_dim_red_nc_label = QtWidgets.QLabel()
            self.reg_widget.gp_dim_red_nc_label.setText('# of components:')
            self.reg_widget.gp_dim_red_nc_label.setObjectName("self.gp_dim_red_nc_label")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_label)
            self.reg_widget.gp_dim_red_nc_spinbox = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.gp_dim_red_nc_spinbox.setObjectName("self.gp_dim_red_nc_spinbox")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_spinbox)

            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_dim_red_hlayout)
            self.reg_widget.gp_rand_starts_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_rand_starts_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_rand_starts_label.setText('# of random starts:')
            self.reg_widget.gp_rand_starts_label.setObjectName("self.gp_rand_starts_label")
            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_label)
            self.reg_widget.gp_rand_starts_spin = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.gp_rand_starts_spin.setValue(1)
            self.reg_widget.gp_rand_starts_spin.setObjectName("self.gp_rand_starts_spin")
            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_spin)
            self.reg_widget.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_rand_starts_hlayout.addItem(self.reg_widget.spacerItem4)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_rand_starts_hlayout)
            self.reg_widget.gp_theta_vlayout = QtWidgets.QVBoxLayout()
            self.reg_widget.gp_theta0_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_theta0_label.setText('Starting Theta:')
            self.reg_widget.gp_theta0_label.setObjectName("self.gp_theta0_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_label)
            self.reg_widget.gp_theta0_spin = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.gp_theta0_spin.setValue(1.0)
            self.reg_widget.gp_theta0_spin.setObjectName("self.gp_theta0_spin")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_spin)
            self.reg_widget.gp_thetaL_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaL_label.setText('Lower bound on Theta:')
            self.reg_widget.gp_thetaL_label.setObjectName("self.gp_thetaL_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_label)
            self.reg_widget.gp_thetaL_spin = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.gp_thetaL_spin.setValue(0.1)
            self.reg_widget.gp_thetaL_spin.setObjectName("self.gp_thetaL_spin")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_spin)
            self.reg_widget.gp_thetaU_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaU_label.setText('Upper bound on Theta:')
            self.reg_widget.gp_thetaU_label.setObjectName("self.gp_thetaU_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_label)
            self.reg_widget.gp_thetaU_spin = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.gp_thetaU_spin.setMaximum(10000)
            self.reg_widget.gp_thetaU_spin.setValue(100.0)

            self.reg_widget.gp_thetaU_spin.setObjectName("self.gp_thetaU_spin")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_spin)
            self.reg_widget.spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_theta_vlayout.addItem(self.reg_widget.spacerItem5)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_theta_vlayout)
            self.reg_widget.gp_dim_red_combobox.currentIndexChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.gp_dim_red_nc_spinbox.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.gp_rand_starts_spin.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.gp_theta0_spin.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.gp_thetaL_spin.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.gp_thetaU_spin.valueChanged.connect(lambda: self.get_regression_parameters())
            if params is not None:
                self.reg_widget.gp_dim_red_combobox.setCurrentIndex(
                    self.reg_widget.gp_dim_red_combobox.findText(params['reduce_dim']))
                self.reg_widget.gp_dim_red_nc_spinbox.setValue(params['n_components'])
                self.reg_widget.gp_rand_starts_spin.setValue(params['random_start'])
                self.reg_widget.gp_theta0_spin.setValue(params['theta0'])
                self.reg_widget.gp_thetaL_spin.setValue(params['thetaL'])
                self.reg_widget.gp_thetaU_spin.setValue(params['thetaU'])

        if alg == self.algorithm_list[3]:
            self.reg_widget.ols_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.ols_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.ols_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.ols_intercept_checkbox.setChecked(True)
            self.reg_widget.ols_intercept_checkbox.setObjectName("self.ols_intercept_checkbox")
            self.reg_widget.ols_hlayout.addWidget(self.reg_widget.ols_intercept_checkbox)
            self.reg_widget.ols_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            if params is not None:
                self.reg_widget.ols_intercept_checkbox.setChecked(params['fit_intercept'])

        if alg == self.algorithm_list[4]:
            self.reg_widget.omp_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.omp_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.omp_label.setText('# of nonzero coefficients:')
            self.reg_widget.omp_label.setObjectName("self.omp_label")
            self.reg_widget.omp_hlayout.addWidget(self.reg_widget.omp_label)
            self.reg_widget.omp_nfeatures = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.omp_nfeatures.setMaximum(9999)
            try:
                xvars = [str(x.text()) for x in self.regression_train_choosex.selectedItems()]
                nfeatures_default = 0.1 * self.pysat_fun.data[self.regression_choosedata.currentText()].df[
                    xvars].columns.levels[1].size
                self.reg_widget.omp_nfeatures.setValue(nfeatures_default)
            except:
                self.reg_widget.omp_nfeatures.setValue(10)
                self.reg_widget.omp_nfeatures.setObjectName("self.omp_nfeatures")
            self.reg_widget.omp_hlayout.addWidget(self.reg_widget.omp_nfeatures)
            self.reg_widget.omp_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.omp_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.omp_intercept_checkbox.setChecked(True)
            self.reg_widget.omp_intercept_checkbox.setObjectName("self.omp_intercept_checkbox")
            self.reg_widget.omp_hlayout.addWidget(self.reg_widget.omp_intercept_checkbox)

            self.reg_widget.omp_cv_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.omp_cv_checkbox.setText('Optimize with Cross Validation? (Ignores # of coeffs)')
            self.reg_widget.omp_cv_checkbox.setChecked(True)
            self.reg_widget.omp_cv_checkbox.setObjectName("self.omp_cv_checkbox")
            self.reg_widget.omp_hlayout.addWidget(self.reg_widget.omp_cv_checkbox)

            self.reg_widget.omp_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.omp_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.omp_nfeatures.valueChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.omp_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.omp_cv_checkbox.setChecked(params['CV'])
                self.reg_widget.omp_nfeatures.setValue(params['n_nonzero_coefs'])

        if alg == self.algorithm_list[5]:
            self.reg_widget.lasso_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.lasso_alpha_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.lasso_iter_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.lasso_checkboxes_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.lasso_alphalabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.lasso_alphalabel.setText('Alpha:')
            self.reg_widget.lasso_alphalabel.setObjectName("self.lasso_alphalabel")
            self.reg_widget.lasso_alpha_hlayout.addWidget(self.reg_widget.lasso_alphalabel)

            self.reg_widget.lasso_alpha = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.lasso_alpha.setMaximum(1000)
            self.reg_widget.lasso_alpha.setMinimum(0.0001)
            self.reg_widget.lasso_alpha.setValue(1.0)
            self.reg_widget.lasso_alpha.setObjectName("self.lasso_alpha")
            self.reg_widget.lasso_alpha_hlayout.addWidget(self.reg_widget.lasso_alpha)

            self.reg_widget.lasso_alpha_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                       QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lasso_alpha_hlayout.addItem(self.reg_widget.lasso_alpha_spacer)
            self.reg_widget.lasso_vlayout.addItem(self.reg_widget.lasso_alpha_hlayout)

            self.reg_widget.lasso_maxlabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.lasso_maxlabel.setText('Max # of iterations:')
            self.reg_widget.lasso_maxlabel.setObjectName("self.lasso_maxlabel")
            self.reg_widget.lasso_iter_hlayout.addWidget(self.reg_widget.lasso_maxlabel)

            self.reg_widget.lasso_max = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.lasso_max.setMaximum(100000)
            self.reg_widget.lasso_max.setMinimum(1)
            self.reg_widget.lasso_max.setValue(1000)
            self.reg_widget.lasso_max.setObjectName("self.lasso_max")
            self.reg_widget.lasso_iter_hlayout.addWidget(self.reg_widget.lasso_max)

            self.reg_widget.lasso_tollabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.lasso_tollabel.setText('Tolerance:')
            self.reg_widget.lasso_tollabel.setObjectName("self.lasso_tollabel")
            self.reg_widget.lasso_iter_hlayout.addWidget(self.reg_widget.lasso_tollabel)

            self.reg_widget.lasso_tol = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.lasso_tol.setMaximum(1000)
            self.reg_widget.lasso_tol.setMinimum(0.0000001)
            self.reg_widget.lasso_tol.setDecimals(5)
            self.reg_widget.lasso_tol.setValue(0.0001)
            self.reg_widget.lasso_tol.setObjectName("self.lasso_tol")
            self.reg_widget.lasso_iter_hlayout.addWidget(self.reg_widget.lasso_tol)

            self.reg_widget.lasso_iter_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                      QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lasso_iter_hlayout.addItem(self.reg_widget.lasso_iter_spacer)
            self.reg_widget.lasso_vlayout.addItem(self.reg_widget.lasso_iter_hlayout)

            self.reg_widget.lasso_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lasso_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.lasso_intercept_checkbox.setChecked(True)
            self.reg_widget.lasso_intercept_checkbox.setObjectName("self.lasso_intercept_checkbox")
            self.reg_widget.lasso_checkboxes_hlayout.addWidget(self.reg_widget.lasso_intercept_checkbox)

            self.reg_widget.lasso_positive_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lasso_positive_checkbox.setText('Force positive coefficients')
            self.reg_widget.lasso_positive_checkbox.setChecked(False)
            self.reg_widget.lasso_positive_checkbox.setObjectName("self.lasso_positive_checkbox")
            self.reg_widget.lasso_checkboxes_hlayout.addWidget(self.reg_widget.lasso_positive_checkbox)

            self.reg_widget.lasso_cv_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lasso_cv_checkbox.setText('Optimize with Cross Validation? (Ignores alpha)')
            self.reg_widget.lasso_cv_checkbox.setChecked(True)
            self.reg_widget.lasso_cv_checkbox.setObjectName("self.lasso_cv_checkbox")
            self.reg_widget.lasso_checkboxes_hlayout.addWidget(self.reg_widget.lasso_cv_checkbox)

            self.reg_widget.lasso_checkbox_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                          QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lasso_checkboxes_hlayout.addItem(self.reg_widget.lasso_checkbox_spacer)
            self.reg_widget.lasso_vlayout.addItem(self.reg_widget.lasso_checkboxes_hlayout)

            self.reg_widget.lasso_alpha.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lasso_max.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lasso_tol.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lasso_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lasso_positive_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lasso_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.lasso_alpha.setValue(params['alpha'])
                self.reg_widget.lasso_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.lasso_tol.setValue(params['tol'])
                self.reg_widget.lasso_max.setValue(params['max_iter'])
                self.reg_widget.lasso_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.lasso_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[6]:
            self.reg_widget.elnet_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.elnet_alpha_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.elnet_l1_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.elnet_iter_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.elnet_checkboxes_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.elnet_alphalabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.elnet_alphalabel.setText('Alpha:')
            self.reg_widget.elnet_alphalabel.setObjectName("self.elnet_alphalabel")
            self.reg_widget.elnet_alpha_hlayout.addWidget(self.reg_widget.elnet_alphalabel)

            self.reg_widget.elnet_alpha = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.elnet_alpha.setMaximum(1000)
            self.reg_widget.elnet_alpha.setMinimum(0.0001)
            self.reg_widget.elnet_alpha.setValue(1.0)
            self.reg_widget.elnet_alpha.setObjectName("self.elnet_alpha")
            self.reg_widget.elnet_alpha_hlayout.addWidget(self.reg_widget.elnet_alpha)

            self.reg_widget.elnet_alpha_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                       QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.elnet_alpha_hlayout.addItem(self.reg_widget.elnet_alpha_spacer)
            self.reg_widget.elnet_vlayout.addItem(self.reg_widget.elnet_alpha_hlayout)

            self.reg_widget.elnet_l1label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.elnet_l1label.setText('L1 ratio:')
            self.reg_widget.elnet_l1label.setObjectName("self.elnet_l1label")
            self.reg_widget.elnet_l1_hlayout.addWidget(self.reg_widget.elnet_l1label)

            self.reg_widget.elnet_l1 = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.elnet_l1.setMaximum(1)
            self.reg_widget.elnet_l1.setMinimum(0)
            self.reg_widget.elnet_l1.setValue(0.5)

            self.reg_widget.elnet_l1.setObjectName("self.elnet_l1")
            self.reg_widget.elnet_l1_hlayout.addWidget(self.reg_widget.elnet_l1)

            self.reg_widget.elnet_l1_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                    QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.elnet_l1_hlayout.addItem(self.reg_widget.elnet_l1_spacer)
            self.reg_widget.elnet_vlayout.addItem(self.reg_widget.elnet_l1_hlayout)

            self.reg_widget.elnet_maxlabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.elnet_maxlabel.setText('Max # of iterations:')
            self.reg_widget.elnet_maxlabel.setObjectName("self.elnet_maxlabel")
            self.reg_widget.elnet_iter_hlayout.addWidget(self.reg_widget.elnet_maxlabel)

            self.reg_widget.elnet_max = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.elnet_max.setMaximum(100000)
            self.reg_widget.elnet_max.setMinimum(1)
            self.reg_widget.elnet_max.setValue(1000)
            self.reg_widget.elnet_max.setObjectName("self.elnet_max")
            self.reg_widget.elnet_iter_hlayout.addWidget(self.reg_widget.elnet_max)

            self.reg_widget.elnet_tollabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.elnet_tollabel.setText('Tolerance:')
            self.reg_widget.elnet_tollabel.setObjectName("self.elnet_tollabel")
            self.reg_widget.elnet_iter_hlayout.addWidget(self.reg_widget.elnet_tollabel)

            self.reg_widget.elnet_tol = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.elnet_tol.setMaximum(1000)
            self.reg_widget.elnet_tol.setMinimum(0.0000001)
            self.reg_widget.elnet_tol.setDecimals(5)
            self.reg_widget.elnet_tol.setValue(0.0001)
            self.reg_widget.elnet_tol.setObjectName("self.elnet_tol")
            self.reg_widget.elnet_iter_hlayout.addWidget(self.reg_widget.elnet_tol)

            self.reg_widget.elnet_iter_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                      QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.elnet_iter_hlayout.addItem(self.reg_widget.elnet_iter_spacer)
            self.reg_widget.elnet_vlayout.addItem(self.reg_widget.elnet_iter_hlayout)

            self.reg_widget.elnet_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.elnet_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.elnet_intercept_checkbox.setChecked(True)
            self.reg_widget.elnet_intercept_checkbox.setObjectName("self.elnet_intercept_checkbox")
            self.reg_widget.elnet_checkboxes_hlayout.addWidget(self.reg_widget.elnet_intercept_checkbox)

            self.reg_widget.elnet_positive_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.elnet_positive_checkbox.setText('Force positive coefficients')
            self.reg_widget.elnet_positive_checkbox.setChecked(False)
            self.reg_widget.elnet_positive_checkbox.setObjectName("self.elnet_positive_checkbox")
            self.reg_widget.elnet_checkboxes_hlayout.addWidget(self.reg_widget.elnet_positive_checkbox)

            self.reg_widget.elnet_cv_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.elnet_cv_checkbox.setText('Optimize with Cross Validation? (Ignores alpha)')
            self.reg_widget.elnet_cv_checkbox.setChecked(True)
            self.reg_widget.elnet_cv_checkbox.setObjectName("self.elnet_cv_checkbox")
            self.reg_widget.elnet_checkboxes_hlayout.addWidget(self.reg_widget.elnet_cv_checkbox)

            self.reg_widget.elnet_checkbox_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                          QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.elnet_checkboxes_hlayout.addItem(self.reg_widget.elnet_checkbox_spacer)
            self.reg_widget.elnet_vlayout.addItem(self.reg_widget.elnet_checkboxes_hlayout)

            self.reg_widget.elnet_alpha.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_l1.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_max.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_tol.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_positive_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.elnet_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.elnet_alpha.setValue(params['alpha'])
                self.reg_widget.elnet_l1.setValue(params['l1_ratio'])
                self.reg_widget.elnet_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.elnet_tol.setValue(params['tol'])
                self.reg_widget.elnet_max.setValue(params['max_iter'])
                self.reg_widget.elnet_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.elnet_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[7]:
            self.reg_widget.ridge_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.ridge_alpha_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.ridge_iter_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.ridge_checkboxes_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.ridge_alphalabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.ridge_alphalabel.setText('Alpha:')
            self.reg_widget.ridge_alphalabel.setObjectName("self.ridge_alphalabel")
            self.reg_widget.ridge_alpha_hlayout.addWidget(self.reg_widget.ridge_alphalabel)

            self.reg_widget.ridge_alpha = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.ridge_alpha.setMaximum(1000)
            self.reg_widget.ridge_alpha.setMinimum(0.0001)
            self.reg_widget.ridge_alpha.setValue(1.0)
            self.reg_widget.ridge_alpha.setObjectName("self.ridge_alpha")
            self.reg_widget.ridge_alpha_hlayout.addWidget(self.reg_widget.ridge_alpha)

            self.reg_widget.ridge_alpha_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                       QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.ridge_alpha_hlayout.addItem(self.reg_widget.ridge_alpha_spacer)
            self.reg_widget.ridge_vlayout.addItem(self.reg_widget.ridge_alpha_hlayout)

            self.reg_widget.ridge_maxlabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.ridge_maxlabel.setText('Max # of iterations:')
            self.reg_widget.ridge_maxlabel.setObjectName("self.ridge_maxlabel")
            self.reg_widget.ridge_iter_hlayout.addWidget(self.reg_widget.ridge_maxlabel)

            self.reg_widget.ridge_max = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.ridge_max.setMaximum(100000)
            self.reg_widget.ridge_max.setMinimum(1)
            self.reg_widget.ridge_max.setValue(1000)
            self.reg_widget.ridge_max.setObjectName("self.ridge_max")
            self.reg_widget.ridge_iter_hlayout.addWidget(self.reg_widget.ridge_max)

            self.reg_widget.ridge_tollabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.ridge_tollabel.setText('Tolerance:')
            self.reg_widget.ridge_tollabel.setObjectName("self.ridge_tollabel")
            self.reg_widget.ridge_iter_hlayout.addWidget(self.reg_widget.ridge_tollabel)

            self.reg_widget.ridge_tol = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.ridge_tol.setMaximum(1000)
            self.reg_widget.ridge_tol.setMinimum(0.0000001)
            self.reg_widget.ridge_tol.setDecimals(5)
            self.reg_widget.ridge_tol.setValue(0.0001)
            self.reg_widget.ridge_tol.setObjectName("self.ridge_tol")
            self.reg_widget.ridge_iter_hlayout.addWidget(self.reg_widget.ridge_tol)

            self.reg_widget.ridge_iter_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                      QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.ridge_iter_hlayout.addItem(self.reg_widget.ridge_iter_spacer)
            self.reg_widget.ridge_vlayout.addItem(self.reg_widget.ridge_iter_hlayout)

            self.reg_widget.ridge_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.ridge_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.ridge_intercept_checkbox.setChecked(True)
            self.reg_widget.ridge_intercept_checkbox.setObjectName("self.ridge_intercept_checkbox")
            self.reg_widget.ridge_checkboxes_hlayout.addWidget(self.reg_widget.ridge_intercept_checkbox)

            self.reg_widget.ridge_cv_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.ridge_cv_checkbox.setText('Optimize with Cross Validation? (Ignores alpha)')
            self.reg_widget.ridge_cv_checkbox.setChecked(True)
            self.reg_widget.ridge_cv_checkbox.setObjectName("self.ridge_cv_checkbox")
            self.reg_widget.ridge_checkboxes_hlayout.addWidget(self.reg_widget.ridge_cv_checkbox)

            self.reg_widget.ridge_checkbox_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                          QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.ridge_checkboxes_hlayout.addItem(self.reg_widget.ridge_checkbox_spacer)
            self.reg_widget.ridge_vlayout.addItem(self.reg_widget.ridge_checkboxes_hlayout)

            self.reg_widget.ridge_alpha.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.ridge_max.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.ridge_tol.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.ridge_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.ridge_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.ridge_alpha.setValue(params['alpha'])
                self.reg_widget.ridge_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.ridge_tol.setValue(params['tol'])
                self.reg_widget.ridge_max.setValue(params['max_iter'])
                self.reg_widget.ridge_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[8]:
            self.line = QtWidgets.QFrame(self.regression_train)
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.min_max_layout = QtWidgets.QHBoxLayout()
            self.min_max_layout.setContentsMargins(11, 11, 11, 11)
            self.min_max_layout.setSpacing(6)
            self.min_max_layout.setObjectName("min_max_layout")
            self.min_max_layout.addWidget(self.line)
            self.groupbox = QtWidgets.QGroupBox(self.regression_train)
            self.groupbox.setObjectName("groupbox")
            self.bayesian_ridge_regression_form = QtWidgets.QFormLayout(self.groupbox)
            self.bayesian_ridge_regression_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
            self.bayesian_ridge_regression_form.setContentsMargins(11, 11, 11, 11)
            self.bayesian_ridge_regression_form.setSpacing(6)
            self.bayesian_ridge_regression_form.setObjectName("bayesian_ridge_regression_form")
            self.n_inter_label = QtWidgets.QLabel(self.groupbox)
            self.n_inter_label.setObjectName("n_inter_label")
            self.bayesian_ridge_regression_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.n_inter_label)
            self.n_inter_spinBox = QtWidgets.QSpinBox(self.groupbox)
            self.n_inter_spinBox.setMaximum(999999)
            self.n_inter_spinBox.setProperty("value", 300)
            self.n_inter_spinBox.setObjectName("n_inter_spinBox")
            self.bayesian_ridge_regression_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.n_inter_spinBox)
            self.tol_label = QtWidgets.QLabel(self.groupbox)
            self.tol_label.setObjectName("tol_label")
            self.bayesian_ridge_regression_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tol_label)
            self.tol_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
            self.tol_doubleSpinBox.setDecimals(5)
            self.tol_doubleSpinBox.setMinimum(-99.0)
            self.tol_doubleSpinBox.setSingleStep(0.001)
            self.tol_doubleSpinBox.setProperty("value", 0.001)
            self.tol_doubleSpinBox.setObjectName("tol_doubleSpinBox")
            self.bayesian_ridge_regression_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tol_doubleSpinBox)
            self.alpha_1_label = QtWidgets.QLabel(self.groupbox)
            self.alpha_1_label.setObjectName("alpha_1_label")
            self.bayesian_ridge_regression_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_1_label)
            self.alpha_1_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
            self.alpha_1_doubleSpinBox.setDecimals(5)
            self.alpha_1_doubleSpinBox.setMinimum(-99.0)
            self.alpha_1_doubleSpinBox.setSingleStep(0.001)
            self.alpha_1_doubleSpinBox.setProperty("value", 0.001)
            self.alpha_1_doubleSpinBox.setObjectName("alpha_1_doubleSpinBox")
            self.bayesian_ridge_regression_form.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                                          self.alpha_1_doubleSpinBox)
            self.alpha_2_label = QtWidgets.QLabel(self.groupbox)
            self.alpha_2_label.setObjectName("alpha_2_label")
            self.bayesian_ridge_regression_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.alpha_2_label)
            self.alpha_2_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
            self.alpha_2_doubleSpinBox.setDecimals(8)
            self.alpha_2_doubleSpinBox.setMinimum(-99.0)
            self.alpha_2_doubleSpinBox.setSingleStep(1e-06)
            self.alpha_2_doubleSpinBox.setProperty("value", 1e-06)
            self.alpha_2_doubleSpinBox.setObjectName("alpha_2_doubleSpinBox")
            self.bayesian_ridge_regression_form.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                                          self.alpha_2_doubleSpinBox)
            self.lambda_2_label = QtWidgets.QLabel(self.groupbox)
            self.lambda_2_label.setObjectName("lambda_2_label")
            self.bayesian_ridge_regression_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lambda_2_label)
            self.lambda_2_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
            self.lambda_2_doubleSpinBox.setDecimals(8)
            self.lambda_2_doubleSpinBox.setMinimum(-99.0)
            self.lambda_2_doubleSpinBox.setSingleStep(1e-06)
            self.lambda_2_doubleSpinBox.setProperty("value", 1e-06)
            self.lambda_2_doubleSpinBox.setObjectName("lambda_2_doubleSpinBox")
            self.bayesian_ridge_regression_form.setWidget(5, QtWidgets.QFormLayout.FieldRole,
                                                          self.lambda_2_doubleSpinBox)
            self.compute_score_label = QtWidgets.QLabel(self.groupbox)
            self.compute_score_label.setObjectName("compute_score_label")
            self.bayesian_ridge_regression_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.compute_score_label)
            self.compute_score_checkBox = QtWidgets.QCheckBox(self.groupbox)
            self.compute_score_checkBox.setCheckable(True)
            self.compute_score_checkBox.setChecked(False)
            self.compute_score_checkBox.setObjectName("compute_score_checkBox")
            self.bayesian_ridge_regression_form.setWidget(6, QtWidgets.QFormLayout.FieldRole,
                                                          self.compute_score_checkBox)
            self.fit_intercept_label = QtWidgets.QLabel(self.groupbox)
            self.fit_intercept_label.setObjectName("fit_intercept_label")
            self.bayesian_ridge_regression_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.fit_intercept_label)
            self.fit_intercept_checkBox = QtWidgets.QCheckBox(self.groupbox)
            self.fit_intercept_checkBox.setCheckable(True)
            self.fit_intercept_checkBox.setChecked(True)
            self.fit_intercept_checkBox.setObjectName("fit_intercept_checkBox")
            self.bayesian_ridge_regression_form.setWidget(7, QtWidgets.QFormLayout.FieldRole,
                                                          self.fit_intercept_checkBox)
            self.normalize_label = QtWidgets.QLabel(self.groupbox)
            self.normalize_label.setObjectName("normalize_label")
            self.bayesian_ridge_regression_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.normalize_label)
            self.normalize_checkBox = QtWidgets.QCheckBox(self.groupbox)
            self.normalize_checkBox.setCheckable(True)
            self.normalize_checkBox.setChecked(False)
            self.normalize_checkBox.setObjectName("normalize_checkBox")
            self.bayesian_ridge_regression_form.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.normalize_checkBox)
            self.copy_X_label = QtWidgets.QLabel(self.groupbox)
            self.copy_X_label.setObjectName("copy_X_label")
            self.bayesian_ridge_regression_form.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.copy_X_label)
            self.copy_X_checkBox = QtWidgets.QCheckBox(self.groupbox)
            self.copy_X_checkBox.setCheckable(True)
            self.copy_X_checkBox.setChecked(True)
            self.copy_X_checkBox.setObjectName("copy_X_checkBox")
            self.bayesian_ridge_regression_form.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.copy_X_checkBox)
            self.verbose_label = QtWidgets.QLabel(self.groupbox)
            self.verbose_label.setObjectName("verbose_label")
            self.bayesian_ridge_regression_form.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.verbose_label)
            self.verbose_checkBox = QtWidgets.QCheckBox(self.groupbox)
            self.verbose_checkBox.setCheckable(True)
            self.verbose_checkBox.setChecked(False)
            self.verbose_checkBox.setObjectName("verbose_checkBox")
            self.bayesian_ridge_regression_form.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.verbose_checkBox)
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.regression_train)
            self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
            self.verticalLayout_2.setSpacing(6)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.verticalLayout_2.addWidget(self.groupbox)

            self.n_inter_label.setText("Number of iterations")
            self.tol_label.setText("Tol")
            self.alpha_1_label.setText("alpha_1")
            self.alpha_2_label.setText("alpha_2")
            self.lambda_2_label.setText("lambda_2")
            self.compute_score_label.setText("compute_score")
            self.compute_score_checkBox.setText("compute the objective function at each step of the model")
            self.fit_intercept_label.setText("fit_intercept")
            self.fit_intercept_checkBox.setText("calculate the intercept for this model")
            self.normalize_label.setText("normalize")
            self.normalize_checkBox.setText("regressors X will be normalized before regression")
            self.copy_X_label.setText("copy_X")
            self.copy_X_checkBox.setText("X will be copied; else, it may be overwritten")
            self.verbose_label.setText("verbose")
            self.verbose_checkBox.setText("Verbose mode when fitting the model")

        if alg == self.algorithm_list[9]:
            self.reg_widget.pl

        if alg == self.algorithm_list[10]:
            pass

        if alg == self.algorithm_list[11]:
            self.reg_widget.lassoLARS_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.lassoLARS_alpha_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.lassoLARS_iter_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.lassoLARS_checkboxes_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)

            self.reg_widget.lassoLARS_alphalabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.lassoLARS_alphalabel.setText('Alpha:')
            self.reg_widget.lassoLARS_alphalabel.setObjectName("self.lassoLARS_alphalabel")
            self.reg_widget.lassoLARS_alpha_hlayout.addWidget(self.reg_widget.lassoLARS_alphalabel)
            self.reg_widget.lassoLARS_alpha = QtWidgets.QDoubleSpinBox(self.reg_widget)
            self.reg_widget.lassoLARS_alpha.setMaximum(1000)
            self.reg_widget.lassoLARS_alpha.setMinimum(0.0001)
            self.reg_widget.lassoLARS_alpha.setValue(1.0)
            self.reg_widget.lassoLARS_alpha.setObjectName("self.lassoLARS_alpha")
            self.reg_widget.lassoLARS_alpha_hlayout.addWidget(self.reg_widget.lassoLARS_alpha)
            self.reg_widget.lassoLARS_alpha_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                           QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lassoLARS_alpha_hlayout.addItem(self.reg_widget.lassoLARS_alpha_spacer)
            self.reg_widget.lassoLARS_vlayout.addItem(self.reg_widget.lassoLARS_alpha_hlayout)

            self.reg_widget.lassoLARS_maxlabel = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.lassoLARS_maxlabel.setText('Max # of iterations:')
            self.reg_widget.lassoLARS_maxlabel.setObjectName("self.lassoLARS_maxlabel")
            self.reg_widget.lassoLARS_iter_hlayout.addWidget(self.reg_widget.lassoLARS_maxlabel)
            self.reg_widget.lassoLARS_max = QtWidgets.QSpinBox(self.reg_widget)
            self.reg_widget.lassoLARS_max.setMaximum(100000)
            self.reg_widget.lassoLARS_max.setMinimum(1)
            self.reg_widget.lassoLARS_max.setValue(1000)
            self.reg_widget.lassoLARS_max.setObjectName("self.lassoLARS_max")
            self.reg_widget.lassoLARS_iter_hlayout.addWidget(self.reg_widget.lassoLARS_max)

            self.reg_widget.lassoLARS_iter_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                          QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lassoLARS_iter_hlayout.addItem(self.reg_widget.lassoLARS_iter_spacer)
            self.reg_widget.lassoLARS_vlayout.addItem(self.reg_widget.lassoLARS_iter_hlayout)

            self.reg_widget.lassoLARS_intercept_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lassoLARS_intercept_checkbox.setText('Fit Intercept')
            self.reg_widget.lassoLARS_intercept_checkbox.setChecked(True)
            self.reg_widget.lassoLARS_intercept_checkbox.setObjectName("self.lassoLARS_intercept_checkbox")
            self.reg_widget.lassoLARS_checkboxes_hlayout.addWidget(self.reg_widget.lassoLARS_intercept_checkbox)

            self.reg_widget.lassoLARS_positive_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lassoLARS_positive_checkbox.setText('Force positive coefficients')
            self.reg_widget.lassoLARS_positive_checkbox.setChecked(False)
            self.reg_widget.lassoLARS_positive_checkbox.setObjectName("self.lassoLARS_positive_checkbox")
            self.reg_widget.lassoLARS_checkboxes_hlayout.addWidget(self.reg_widget.lassoLARS_positive_checkbox)

            self.reg_widget.lassoLARS_cv_checkbox = QtWidgets.QCheckBox(self.reg_widget)
            self.reg_widget.lassoLARS_cv_checkbox.setText('Optimize with Cross Validation? (Ignores alpha)')
            self.reg_widget.lassoLARS_cv_checkbox.setChecked(True)
            self.reg_widget.lassoLARS_cv_checkbox.setObjectName("self.lassoLARS_cv_checkbox")
            self.reg_widget.lassoLARS_checkboxes_hlayout.addWidget(self.reg_widget.lassoLARS_cv_checkbox)

            self.reg_widget.lassoLARS_checkbox_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                              QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.lassoLARS_checkboxes_hlayout.addItem(self.reg_widget.lassoLARS_checkbox_spacer)
            self.reg_widget.lassoLARS_vlayout.addItem(self.reg_widget.lassoLARS_checkboxes_hlayout)

            self.reg_widget.lassoLARS_alpha.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lassoLARS_max.valueChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lassoLARS_intercept_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lassoLARS_positive_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())
            self.reg_widget.lassoLARS_cv_checkbox.stateChanged.connect(lambda: self.get_regression_parameters())

            if params is not None:
                self.reg_widget.lassoLARS_alpha.setValue(params['alpha'])
                self.reg_widget.lassoLARS_intercept_checkbox.setChecked(params['fit_intercept'])
                self.reg_widget.lassoLARS_max.setValue(params['max_iter'])
                self.reg_widget.lassoLARS_positive_checkbox.setChecked(params['positive'])
                self.reg_widget.lassoLARS_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[12]:
            pass

        if alg == self.algorithm_list[13]:
            pass

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
