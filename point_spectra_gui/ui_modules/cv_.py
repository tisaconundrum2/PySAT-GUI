from point_spectra_gui.ui_modules.Error_ import error_print
from PyQt5 import QtGui, QtCore, QtWidgets


class cv_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list):
        self.pysat_fun = pysat_fun
        self.ui_id = None
        self.module_layout = module_layout
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.cv_ui()
        self.cv_choosealg.currentIndexChanged.connect(lambda: self.make_reg_widget(self.cv_choosealg.currentText()))

    def get_cv_parameters(self):

        method = self.cv_choosealg.currentText()
        datakey = self.cv_choosedata.currentText()
        xvars = [str(x.text()) for x in self.cv_train_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.cv_train_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        params = {}
        kws = {}
        try:
            if method == 'PLS':
                nc = self.reg_widget.pls_nc_lineedit.text().split(',')
                nc = [int(i) for i in nc]
                params = {'n_components': nc,
                          'scale': [False]}
                # modelkey=[method+' (nc='+str(i)+')' for i in self.reg_widget.pls_nc_lineedit.text().split(',')]

            if method == 'GP':
                nc = [int(i) for i in self.reg_widget.gp_dim_red_nc_lineedit.text().split(',')]
                random_start = [int(i) for i in self.reg_widget.gp_rand_starts_lineedit.text().split(',')]
                theta0 = [float(i) for i in self.reg_widget.gp_theta0_lineedit.text().split(',')]
                thetaL = [float(i) for i in self.reg_widget.gp_thetaL_lineedit.text().split(',')]
                thetaU = [float(i) for i in self.reg_widget.gp_thetaU_lineedit.text().split(',')]

                params = {'reduce_dim': self.reg_widget.gp_dim_red_lineedit.text().split(','),
                          'n_components': nc,
                          'random_start': random_start,
                          'theta0': theta0,
                          'thetaL': thetaL,
                          'thetaU': thetaU}

        except:
            pass

        args = [datakey, xvars, yvars, yrange, method, params]

        ui_list = 'do_cv'
        fun_list = 'do_cv'
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.ui_id)

    def make_reg_widget(self, alg):
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtWidgets.QWidget()
        if alg == 'PLS':
            self.reg_widget.pls_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.pls_nc_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.pls_nc_label.setText('# of components:')
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_label)
            self.reg_widget.pls_nc_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_lineedit)
            self.reg_widget.pls_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                               QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.pls_hlayout.addItem(self.reg_widget.pls_spacer)
            self.reg_widget.pls_nc_lineedit.textChanged.connect(lambda: self.get_cv_parameters())

        elif alg == 'GP':
            self.reg_widget = QtWidgets.QWidget()
            self.reg_widget.gp_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.gp_dim_red_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_dim_red_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_dim_red_label.setText('Choose dimensionality reduction method:')
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_label)
            self.reg_widget.gp_dim_red_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_dim_red_lineedit.setText('PCA')
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_lineedit)
            self.reg_widget.gp_dim_red_nc_label = QtWidgets.QLabel()
            self.reg_widget.gp_dim_red_nc_label.setText('# of components:')
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_label)
            self.reg_widget.gp_dim_red_nc_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_dim_red_nc_lineedit.setText('10')
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_lineedit)

            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_dim_red_hlayout)
            self.reg_widget.gp_rand_starts_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_rand_starts_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_rand_starts_label.setText('# of random starts:')
            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_label)
            self.reg_widget.gp_rand_starts_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_rand_starts_lineedit.setText('1')

            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_lineedit)
            self.reg_widget.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_rand_starts_hlayout.addItem(self.reg_widget.spacerItem4)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_rand_starts_hlayout)
            self.reg_widget.gp_theta_vlayout = QtWidgets.QVBoxLayout()
            self.reg_widget.gp_theta0_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_theta0_label.setText('Starting Theta:')
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_label)
            self.reg_widget.gp_theta0_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_theta0_lineedit.setText('1.0')
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_lineedit)
            self.reg_widget.gp_thetaL_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaL_label.setText('Lower bound on Theta:')
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_label)
            self.reg_widget.gp_thetaL_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_thetaL_lineedit.setText('0.1')
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_lineedit)
            self.reg_widget.gp_thetaU_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaU_label.setText('Upper bound on Theta:')
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_label)
            self.reg_widget.gp_thetaU_lineedit = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_thetaU_lineedit.setText('100.0')

            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_lineedit)
            self.reg_widget.spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_theta_vlayout.addItem(self.reg_widget.spacerItem5)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_theta_vlayout)

            self.reg_widget.gp_dim_red_lineedit.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_dim_red_nc_lineedit.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_rand_starts_lineedit.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_theta0_lineedit.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_thetaL_lineedit.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_thetaU_lineedit.textChanged.connect(lambda: self.get_cv_parameters())

        self.cv_vlayout.addWidget(self.reg_widget)

    def cv_ui(self):
        self.cv_train = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cv_train.setFont(font)
        self.cv_train.setObjectName(("cv_train"))
        self.cv_vlayout = QtWidgets.QVBoxLayout(self.cv_train)
        self.cv_vlayout.setObjectName(("cv_vlayout"))
        # choose data
        self.cv_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.cv_choosedata_hlayout.setObjectName(("cv_choosedata_hlayout"))
        self.cv_train_choosedata_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosedata_label.setObjectName(("cv_train_choosedata_label"))
        self.cv_train_choosedata_label.setText(("cv_train", "Choose data:"))
        self.cv_choosedata_hlayout.addWidget(self.cv_train_choosedata_label)
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
        self.cv_choosedata = make_combobox(datachoices)
        self.cv_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.cv_choosedata.setObjectName(("cv_choosedata"))
        self.cv_choosedata_hlayout.addWidget(self.cv_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cv_choosedata_hlayout.addItem(spacerItem)
        self.cv_vlayout.addLayout(self.cv_choosedata_hlayout)
        # choose variables
        self.cv_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.cv_choosevars_hlayout.setObjectName(("cv_choosevars_hlayout"))
        self.cv_choosexvars_vlayout = QtWidgets.QVBoxLayout()
        self.cv_chooseyvars_vlayout = QtWidgets.QVBoxLayout()
        self.cv_choosevars_hlayout.addLayout(self.cv_choosexvars_vlayout)
        self.cv_choosevars_hlayout.addLayout(self.cv_chooseyvars_vlayout)

        # choose x variables
        self.cv_train_choosex_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosex_label.setObjectName(("cv_train_choosex_label"))
        self.cv_train_choosex_label.setText('X variable:')
        self.cv_choosexvars_vlayout.addWidget(self.cv_train_choosex_label)
        xvarchoices = self.pysat_fun.data[self.cv_choosedata.currentText()].df.columns.levels[0].values
        xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        self.cv_train_choosex = make_listwidget(xvarchoices)
        self.cv_train_choosex.setObjectName(("cv_train_choosex"))
        self.cv_choosexvars_vlayout.addWidget(self.cv_train_choosex)

        # choose y variables
        self.cv_train_choosey_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosey_label.setObjectName(("cv_train_choosey_label"))
        self.cv_train_choosey_label.setText('Y variable:')
        self.cv_chooseyvars_vlayout.addWidget(self.cv_train_choosey_label)
        yvarchoices = self.pysat_fun.data[self.cv_choosedata.currentText()].df['comp'].columns.values
        yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        self.cv_train_choosey = make_listwidget(yvarchoices)
        self.cv_chooseyvars_vlayout.addWidget(self.cv_train_choosey)

        # set limits
        self.cv_yvarlimits_hlayout = QtWidgets.QHBoxLayout()
        self.yvarmin_label = QtWidgets.QLabel(self.cv_train)
        self.yvarmin_label.setText('Min:')
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmin_spin.setMaximum(99999)
        self.yvarmin_spin.setMinimum(0)
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_spin)

        self.yvarmax_label = QtWidgets.QLabel(self.cv_train)
        self.yvarmax_label.setText('Max:')
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmax_spin.setMaximum(99999)
        self.yvarmax_spin.setMinimum(0)
        self.yvarmax_spin.setValue(100)
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_spin)
        self.cv_chooseyvars_vlayout.addLayout(self.cv_yvarlimits_hlayout)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cv_choosevars_hlayout.addItem(spacerItem1)
        self.cv_vlayout.addLayout(self.cv_choosevars_hlayout)

        # ransac options
        self.ransac_hlayout = QtWidgets.QHBoxLayout()
        self.cv_ransac_checkbox = QtWidgets.QCheckBox(self.cv_train)
        self.cv_ransac_checkbox.setObjectName(("cv_ransac_checkbox"))
        self.cv_ransac_checkbox.setText('RANSAC')
        self.ransac_hlayout.addWidget(self.cv_ransac_checkbox)
        self.cv_vlayout.addLayout(self.ransac_hlayout)

        # choose cv algorithm
        self.cv_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.cv_choosealg_hlayout.setObjectName(("cv_choosealg_hlayout"))
        self.cv_choosealg_label = QtWidgets.QLabel(self.cv_train)
        self.cv_choosealg_label.setObjectName(("cv_choosealg_label"))
        self.cv_choosealg_hlayout.addWidget(self.cv_choosealg_label)
        self.cv_alg_choices = ['Choose an algorithm', 'PLS', 'GP', 'More to come...']
        self.cv_choosealg = make_combobox(self.cv_alg_choices)
        self.cv_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.cv_choosealg.setObjectName(("cv_choosealg"))
        self.cv_choosealg_hlayout.addWidget(self.cv_choosealg)
        # TODO add logic that knows when args and kwargs are added.
        cv_choosealg_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
        self.cv_choosealg_hlayout.addItem(cv_choosealg_spacer)
        self.cv_vlayout.addLayout(self.cv_choosealg_hlayout)

        self.module_layout.addWidget(self.cv_train)
        self.cv_train.raise_()
        self.cv_train.setTitle(("cv_train", "Cross Validation / Training"))

        self.cv_choosedata.currentIndexChanged.connect(lambda: self.get_cv_parameters())
        self.cv_choosealg.currentIndexChanged.connect(lambda: self.get_cv_parameters())
        self.cv_train_choosex.currentItemChanged.connect(lambda: self.get_cv_parameters())
        self.cv_train_choosey.currentItemChanged.connect(lambda: self.get_cv_parameters())
        self.cv_choosedata.activated[int].connect(lambda: self.cv_change_vars(self.cv_train_choosey))

    def cv_change_vars(self, obj):
        obj.clear()
        try:
            choices = self.pysat_fun.data[self.cv_choosedata.currentText()].df[['comp']].columns.values
        except:
            choices = ['No valid options']
        for i in choices:
            obj.addItem(i[1])


def make_combobox(choices):
    combo = QtWidgets.QComboBox()

    for i, choice in enumerate(choices):
        combo.addItem((""))
        combo.setItemText(i, ('', choice))

    return combo


def make_listwidget(choices):
    listwidget = QtWidgets.QListWidget()
    listwidget.setItemDelegate
    for item in choices:
        item = QtWidgets.QListWidgetItem(item)
        listwidget.addItem(item)
    return listwidget
