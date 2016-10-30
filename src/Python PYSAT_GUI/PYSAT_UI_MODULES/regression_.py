from PYSAT_UI_MODULES.Error_ import error_print
from PyQt4 import QtCore, QtGui

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


def regression_train(pysat_fun, verticalLayout_8):
    regression_train = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    regression_train.setFont(font)
    regression_train.setObjectName(_fromUtf8("regression_train"))
    regression_vlayout = QtGui.QVBoxLayout(regression_train)
    regression_vlayout.setObjectName(_fromUtf8("regression_vlayout"))
    # choose data
    regression_choosedata_hlayout = QtGui.QHBoxLayout()
    regression_choosedata_hlayout.setObjectName(_fromUtf8("regression_choosedata_hlayout"))
    regression_train_choosedata_label = QtGui.QLabel(regression_train)
    regression_train_choosedata_label.setObjectName(_fromUtf8("regression_train_choosedata_label"))
    regression_train_choosedata_label.setText(_translate("regression_train", "Choose data:", None))
    regression_choosedata_hlayout.addWidget(regression_train_choosedata_label)
    datachoices = pysat_fun.datakeys
    if datachoices == []:
        error_print('No Data has been loaded')
        datachoices = ['No data has been loaded!']
    regression_choosedata = make_combobox(datachoices)
    regression_choosedata.setIconSize(QtCore.QSize(50, 20))
    regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
    regression_choosedata_hlayout.addWidget(regression_choosedata)
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    regression_choosedata_hlayout.addItem(spacerItem)
    regression_vlayout.addLayout(regression_choosedata_hlayout)
    # choose variables
    regression_choosevars_hlayout = QtGui.QHBoxLayout()
    regression_choosevars_hlayout.setObjectName(_fromUtf8("regression_choosevars_hlayout"))
    regression_train_choosex_label = QtGui.QLabel(regression_train)
    regression_train_choosex_label.setObjectName(_fromUtf8("regression_train_choosex_label"))
    regression_choosevars_hlayout.addWidget(regression_train_choosex_label)

    xvarchoices = pysat_fun.data[regression_choosedata.currentText()].df.columns.levels[0].values
    regression_train_choosex = make_listwidget(xvarchoices)
    regression_train_choosex.setObjectName(_fromUtf8("regression_train_choosex"))
    regression_choosevars_hlayout.addWidget(regression_train_choosex)
    regression_train_choosey_label = QtGui.QLabel(regression_train)
    regression_train_choosey_label.setObjectName(_fromUtf8("regression_train_choosey_label"))
    regression_choosevars_hlayout.addWidget(regression_train_choosey_label)

    yvarchoices = pysat_fun.data[regression_choosedata.currentText()].df['comp'].columns.values
    regression_train_choosey = make_listwidget(yvarchoices)
    regression_choosevars_hlayout.addWidget(regression_train_choosey)
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    regression_choosevars_hlayout.addItem(spacerItem1)
    regression_vlayout.addLayout(regression_choosevars_hlayout)

    # ransac options
    ransac_hlayout = QtGui.QHBoxLayout()
    regression_ransac_checkbox = QtGui.QCheckBox(regression_train)
    regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
    regression_ransac_checkbox.setText('RANSAC')
    ransac_hlayout.addWidget(regression_ransac_checkbox)
    regression_vlayout.addLayout(ransac_hlayout)

    regression_ransac_checkbox.stateChanged.connect(lambda: make_ransac_widget(ransac_hlayout, regression_ransac_checkbox))
    # choose regression algorithm
    regression_choosealg_hlayout = QtGui.QHBoxLayout()
    regression_choosealg_hlayout.setObjectName(_fromUtf8("regression_choosealg_hlayout"))
    regression_choosealg_label = QtGui.QLabel(regression_train)
    regression_choosealg_label.setObjectName(_fromUtf8("regression_choosealg_label"))
    regression_choosealg_hlayout.addWidget(regression_choosealg_label)
    regression_alg_choices = ['Choose an algorithm', 'PLS', 'GP', 'More to come...']
    regression_choosealg = make_combobox(regression_alg_choices)
    regression_choosealg.setIconSize(QtCore.QSize(50, 20))
    regression_choosealg.setObjectName(_fromUtf8("regression_choosealg"))
    regression_choosealg_hlayout.addWidget(regression_choosealg)
    regression_choosealg_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                    QtGui.QSizePolicy.Minimum)
    regression_choosealg_hlayout.addItem(regression_choosealg_spacer)
    regression_vlayout.addLayout(regression_choosealg_hlayout)
    regression_choosealg.activated.connect(lambda: make_regression_widget(regression_choosealg, regression_vlayout))

    verticalLayout_8.addWidget(regression_train)
    regression_train.raise_()
    regression_train.setTitle(_translate("regression_train", "Regression - Train", None))

def make_ransac_widget(ransac_hlayout, regression_ransac_checkbox):
    try:
        ransac_widget.deleteLater()
    except:
        pass
    ransac_widget = QtGui.QWidget()
    if regression_ransac_checkbox.isChecked():
        ransac_widget_hlayout = QtGui.QHBoxLayout(ransac_widget)
        ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
        ransac_lossfunc_label = QtGui.QLabel(ransac_widget)
        ransac_lossfunc_label.setText('Loss function:')
        ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_label)
        ransac_lossfunc_combobox = QtGui.QComboBox(ransac_widget)
        ransac_lossfunc_combobox.addItem(_fromUtf8("Squared Error"))
        ransac_lossfunc_combobox.addItem(_fromUtf8("Absolute Error"))
        ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_combobox)
        ransac_lossfunc_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                   QtGui.QSizePolicy.Minimum)
        ransac_lossfunc_hlayout.addItem(ransac_lossfunc_spacer)
        ransac_widget_hlayout.addLayout(ransac_lossfunc_hlayout)
        ransac_thresh_hlayout = QtGui.QHBoxLayout()
        ransac_thresh_label = QtGui.QLabel(ransac_widget)
        ransac_thresh_label.setText('Threshold:')
        ransac_thresh_hlayout.addWidget(ransac_thresh_label)
        ransac_thresh_spin = QtGui.QDoubleSpinBox(ransac_widget)
        ransac_thresh_hlayout.addWidget(ransac_thresh_spin)
        ransac_thresh_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        ransac_thresh_hlayout.addItem(ransac_thresh_spacer)
        ransac_widget_hlayout.addLayout(ransac_thresh_hlayout)
        ransac_hlayout.addWidget(ransac_widget)

def make_regression_widget(regression_choosealg, regression_vlayout):
    alg = regression_choosealg.currentText()
    print(alg)
    try:
        reg_widget.deleteLater()
    except:
        pass
    reg_widget = QtGui.QWidget()
    if alg == 'Choose an algorithm':
        pass
    if alg == 'PLS':
        pls_hlayout = QtGui.QHBoxLayout(reg_widget)
        pls_nc_label = QtGui.QLabel(reg_widget)
        pls_nc_label.setText('# of components:')
        pls_hlayout.addWidget(pls_nc_label)
        pls_nc_spinbox = QtGui.QSpinBox(reg_widget)
        pls_hlayout.addWidget(pls_nc_spinbox)
        pls_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        pls_hlayout.addItem(pls_spacer)

    if alg == 'GP':
        gp_vlayout = QtGui.QVBoxLayout(reg_widget)
        gp_dim_red_hlayout = QtGui.QHBoxLayout()
        gp_dim_red_label = QtGui.QLabel(reg_widget)
        gp_dim_red_label.setText('Choose dimensionality reduction method:')
        gp_dim_red_hlayout.addWidget(gp_dim_red_label)
        gp_dim_red_combobox = QtGui.QComboBox(reg_widget)
        gp_dim_red_combobox.addItem(_fromUtf8("PCA"))
        gp_dim_red_combobox.addItem(_fromUtf8("ICA"))
        gp_dim_red_hlayout.addWidget(gp_dim_red_combobox)
        gp_vlayout.addLayout(gp_dim_red_hlayout)
        gp_rand_starts_hlayout = QtGui.QHBoxLayout()
        gp_rand_starts_label = QtGui.QLabel(reg_widget)
        gp_rand_starts_label.setText('# of random starts:')
        gp_rand_starts_hlayout.addWidget(gp_rand_starts_label)
        gp_rand_starts_spin = QtGui.QSpinBox(reg_widget)
        gp_rand_starts_spin.setValue(1)
        gp_rand_starts_hlayout.addWidget(gp_rand_starts_spin)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        gp_rand_starts_hlayout.addItem(spacerItem4)
        gp_vlayout.addLayout(gp_rand_starts_hlayout)
        gp_theta_vlayout = QtGui.QVBoxLayout()
        gp_theta0_label = QtGui.QLabel(reg_widget)
        gp_theta0_label.setText('Starting Theta:')
        gp_theta_vlayout.addWidget(gp_theta0_label)
        gp_theta0_spin = QtGui.QDoubleSpinBox(reg_widget)
        gp_theta0_spin.setValue(1.0)
        gp_theta_vlayout.addWidget(gp_theta0_spin)
        gp_thetaL_label = QtGui.QLabel(reg_widget)
        gp_thetaL_label.setText('Lower bound on Theta:')
        gp_theta_vlayout.addWidget(gp_thetaL_label)
        gp_thetaL_spin = QtGui.QDoubleSpinBox(reg_widget)
        gp_thetaL_spin.setValue(0.1)
        gp_theta_vlayout.addWidget(gp_thetaL_spin)
        gp_thetaU_label = QtGui.QLabel(reg_widget)
        gp_thetaU_label.setText('Upper bound on Theta:')
        gp_theta_vlayout.addWidget(gp_thetaU_label)
        gp_thetaU_spin = QtGui.QDoubleSpinBox(reg_widget)
        gp_thetaU_spin.setMaximum(10000)
        gp_thetaU_spin.setValue(100.0)

        gp_theta_vlayout.addWidget(gp_thetaU_spin)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        gp_theta_vlayout.addItem(spacerItem5)
        gp_vlayout.addLayout(gp_theta_vlayout)

    regression_vlayout.addWidget(reg_widget)


class ransac:
    def __init__(self, value):
        self.value = 

def make_combobox(choices):
    combo = QtGui.QComboBox()

    for i, choice in enumerate(choices):
        combo.addItem(_fromUtf8(""))
        combo.setItemText(i, _translate('', choice, None))

    return combo

def make_listwidget(choices):
    listwidget = QtGui.QListWidget()
    listwidget.setItemDelegate
    for item in choices:
        item = QtGui.QListWidgetItem(item)
        listwidget.addItem(item)
    return listwidget

