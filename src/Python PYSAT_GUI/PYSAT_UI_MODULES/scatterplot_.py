from PYSAT_UI_MODULES.Error_ import error_print
from PyQt4 import QtCore, QtGui
import numpy as np

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


class scatterplot_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.main()

    def main(self):
        self.pysat_fun.set_fun_list(self.pysat_fun.do_scatterplot)
        self.pysat_fun.set_arg_list([])
        self.pysat_fun.set_kw_list({})
        self.scatterplot_ui()

    def get_scatterplot_parameters(self):
        datakey = self.scatter_choosedata.currentText()
        xvar = self.xvar_choices.currentText()
        yvar = self.yvar_choices.currentText()

        figname = self.figname_text.text()
        title = self.plot_title_text.text()
        xrange = [self.xmin_spin.value(), self.xmax_spin.value()]
        yrange = [self.ymin_spin.value(), self.ymax_spin.value()]
        xtitle = self.xtitle_text.text()
        ytitle = self.ytitle_text.text()
        lbls = self.legend_label_text.text()
        one_to_one = self.onetoone.isChecked()
        figfile = self.file_text.text()
        colors = self.color_choices.currentText()
        args = [datakey, xvar, yvar]
        kws = {'figname': figname,
               'title': title,
               'xrange': xrange,
               'yrange': yrange,
               'xtitle': xtitle,
               'ytitle': ytitle,
               'lbls': lbls,
               'one_to_one': one_to_one,
               'figfile': figfile,
               'colors': colors,
               }
        self.pysat_fun.set_arg_list(args, replacelast=True)
        self.pysat_fun.set_kw_list(kws, replacelast=True)

    #
    #        method=self.regression_choosealg.currentText()
    #        datakey=self.regression_choosedata.currentText()
    #        xvars=[str(x.text()) for x in self.regression_train_choosex.selectedItems()]
    #        yvars=[('comp',str(y.text())) for y in self.regression_train_choosey.selectedItems()]
    #        params={}
    #        ransacparams={}
    #        kws={}
    #        try:
    #            if method=='PLS':
    #                params={'n_components':self.reg_widget.pls_nc_spinbox.value(),
    #                        'scale':False}
    #                modelkey=method+' (nc='+str(self.reg_widget.pls_nc_spinbox.value())+')'
    #                kws={'modelkey':modelkey}
    #            if method=='GP':
    #                params={'reduce_dim':self.reg_widget.gp_dim_red_combobox.currentText(),
    #                        'n_components':self.reg_widget.gp_dim_red_nc_spinbox.value(),
    #                        'random_start':self.reg_widget.gp_rand_starts_spin.value(),
    #                        'theta0':self.reg_widget.gp_theta0_spin.value(),
    #                        'thetaL':self.reg_widget.gp_thetaL_spin.value(),
    #                        'thetaU':self.reg_widget.gp_thetaU_spin.value()}
    #                modelkey=method  #TODO: make this somehow concisely summarize the GP parameters in a string label for the model
    #                kws={'modelkey':modelkey}
    #        except:
    #            pass
    #        if self.regression_ransac_checkbox.isChecked():
    #            lossval=self.ransac_widget.ransac_lossfunc_combobox.currentText()
    #            if lossval=='Squared Error':
    #                loss='squared_loss'
    #            if lossval=='Absolute Error':
    #                loss='absolute_loss'
    #            ransacparams={'residual_threshold':self.ransac_widget.ransac_thresh_spin.value(),
    #                          'loss':loss}
    #
    #        args=[datakey,xvars,yvars,method,params,ransacparams]
    #        self.pysat_fun.set_arg_list(args,replacelast=True)
    #        self.pysat_fun.set_kw_list(kws,replacelast=True)
    #
    #
    #    def make_ransac_widget(self, isChecked):
    #        if not isChecked:
    #            self.ransac_widget.deleteLater()
    #        else:
    #            self.ransac_widget = QtGui.QWidget()
    #            self.ransac_widget.ransac_widget_hlayout = QtGui.QHBoxLayout(self.ransac_widget)
    #            self.ransac_widget.ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
    #            self.ransac_widget.ransac_lossfunc_label = QtGui.QLabel(self.ransac_widget)
    #            self.ransac_widget.ransac_lossfunc_label.setText('Loss function:')
    #            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_label)
    #            self.ransac_widget.ransac_lossfunc_combobox = QtGui.QComboBox(self.ransac_widget)
    #            self.ransac_widget.ransac_lossfunc_combobox.addItem(_fromUtf8("Squared Error"))
    #            self.ransac_widget.ransac_lossfunc_combobox.addItem(_fromUtf8("Absolute Error"))
    #            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_combobox)
    #            self.ransac_widget.ransac_lossfunc_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
    #                                                       QtGui.QSizePolicy.Minimum)
    #            self.ransac_widget.ransac_lossfunc_hlayout.addItem(self.ransac_widget.ransac_lossfunc_spacer)
    #            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_lossfunc_hlayout)
    #            self.ransac_widget.ransac_thresh_hlayout = QtGui.QHBoxLayout()
    #            self.ransac_widget.ransac_thresh_label = QtGui.QLabel(self.ransac_widget)
    #            self.ransac_widget.ransac_thresh_label.setText('Threshold:')
    #            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_label)
    #            self.ransac_widget.ransac_thresh_spin = QtGui.QDoubleSpinBox(self.ransac_widget)
    #            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_spin)
    #            self.ransac_widget.ransac_thresh_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    #            self.ransac_widget.ransac_thresh_hlayout.addItem(self.ransac_widget.ransac_thresh_spacer)
    #            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_thresh_hlayout)
    #            self.ransac_hlayout.addWidget(self.ransac_widget)
    #
    #            self.ransac_widget.ransac_lossfunc_combobox.currentIndexChanged.connect(lambda: self.get_regression_parameters())
    #            self.ransac_widget.ransac_thresh_spin.valueChanged.connect(lambda: self.get_regression_parameters())
    #
    #    def make_regression_widget(self, alg):
    #        print(alg)
    #        try:
    #            self.reg_widget.deleteLater()
    #        except:
    #            pass
    #        self.reg_widget = QtGui.QWidget()
    #        if alg == 'PLS':
    #            self.reg_widget.pls_hlayout = QtGui.QHBoxLayout(self.reg_widget)
    #            self.reg_widget.pls_nc_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.pls_nc_label.setText('# of components:')
    #            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_label)
    #            self.reg_widget.pls_nc_spinbox = QtGui.QSpinBox(self.reg_widget)
    #            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_spinbox)
    #            self.reg_widget.pls_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    #            self.reg_widget.pls_hlayout.addItem(self.reg_widget.pls_spacer)
    #            self.reg_widget.pls_nc_spinbox.valueChanged.connect(lambda: self.get_regression_parameters())
    #
    #        elif alg == 'GP':
    #            self.reg_widget = QtGui.QWidget()
    #            self.reg_widget.gp_vlayout = QtGui.QVBoxLayout(self.reg_widget)
    #            self.reg_widget.gp_dim_red_hlayout = QtGui.QHBoxLayout()
    #            self.reg_widget.gp_dim_red_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.gp_dim_red_label.setText('Choose dimensionality reduction method:')
    #            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_label)
    #            self.reg_widget.gp_dim_red_combobox = QtGui.QComboBox(self.reg_widget)
    #            self.reg_widget.gp_dim_red_combobox.addItem(_fromUtf8("PCA"))
    #            self.reg_widget.gp_dim_red_combobox.addItem(_fromUtf8("ICA"))
    #            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_combobox)
    #            self.reg_widget.gp_dim_red_nc_label = QtGui.QLabel()
    #            self.reg_widget.gp_dim_red_nc_label.setText('# of components:')
    #            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_label)
    #            self.reg_widget.gp_dim_red_nc_spinbox = QtGui.QSpinBox(self.reg_widget)
    #            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_spinbox)
    #
    #            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_dim_red_hlayout)
    #            self.reg_widget.gp_rand_starts_hlayout = QtGui.QHBoxLayout()
    #            self.reg_widget.gp_rand_starts_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.gp_rand_starts_label.setText('# of random starts:')
    #            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_label)
    #            self.reg_widget.gp_rand_starts_spin = QtGui.QSpinBox(self.reg_widget)
    #            self.reg_widget.gp_rand_starts_spin.setValue(1)
    #            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_spin)
    #            self.reg_widget.spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    #            self.reg_widget.gp_rand_starts_hlayout.addItem(self.reg_widget.spacerItem4)
    #            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_rand_starts_hlayout)
    #            self.reg_widget.gp_theta_vlayout = QtGui.QVBoxLayout()
    #            self.reg_widget.gp_theta0_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.gp_theta0_label.setText('Starting Theta:')
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_label)
    #            self.reg_widget.gp_theta0_spin = QtGui.QDoubleSpinBox(self.reg_widget)
    #            self.reg_widget.gp_theta0_spin.setValue(1.0)
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_spin)
    #            self.reg_widget.gp_thetaL_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.gp_thetaL_label.setText('Lower bound on Theta:')
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_label)
    #            self.reg_widget.gp_thetaL_spin = QtGui.QDoubleSpinBox(self.reg_widget)
    #            self.reg_widget.gp_thetaL_spin.setValue(0.1)
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_spin)
    #            self.reg_widget.gp_thetaU_label = QtGui.QLabel(self.reg_widget)
    #            self.reg_widget.gp_thetaU_label.setText('Upper bound on Theta:')
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_label)
    #            self.reg_widget.gp_thetaU_spin = QtGui.QDoubleSpinBox(self.reg_widget)
    #            self.reg_widget.gp_thetaU_spin.setMaximum(10000)
    #            self.reg_widget.gp_thetaU_spin.setValue(100.0)
    #
    #            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_spin)
    #            self.reg_widget.spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    #            self.reg_widget.gp_theta_vlayout.addItem(self.reg_widget.spacerItem5)
    #            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_theta_vlayout)
    #
    #            self.reg_widget.gp_dim_red_combobox.currentIndexChanged.connect(lambda: self.get_regression_parameters())
    #            self.reg_widget.gp_dim_red_nc_spinbox.valueChanged.connect(lambda: self.get_regression_parameters())
    #            self.reg_widget.gp_rand_starts_spin.valueChanged.connect(lambda: self.get_regression_parameters())
    #            self.reg_widget.gp_theta0_spin.valueChanged.connect(lambda: self.get_regression_parameters())
    #            self.reg_widget.gp_thetaL_spin.valueChanged.connect(lambda: self.get_regression_parameters())
    #            self.reg_widget.gp_thetaU_spin.valueChanged.connect(lambda: self.get_regression_parameters())
    #
    #        self.regression_vlayout.addWidget(self.reg_widget)

    def scatterplot_ui(self):
        self.scatter = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scatter.setFont(font)
        self.scatter.setObjectName(_fromUtf8("scatter"))
        self.scatter_vlayout = QtGui.QVBoxLayout()
        self.scatter_vlayout.setMargin(11)
        self.scatter_vlayout.setSpacing(6)
        self.scatter_vlayout.setObjectName(_fromUtf8("scatter_vlayout"))

        self.scatter_choosedata_hlayout = QtGui.QHBoxLayout()
        self.scatter_choosedata_hlayout.setMargin(11)
        self.scatter_choosedata_hlayout.setSpacing(6)
        self.scatter_choosedata_hlayout.setObjectName(_fromUtf8("scatter_choosedata_hlayout"))

        self.scatter_choosedata_label = QtGui.QLabel(self.scatter)
        self.scatter_choosedata_label.setObjectName(_fromUtf8("scatter_choosedata_label"))
        self.scatter_choosedata_hlayout.addWidget(self.scatter_choosedata_label)

        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
        self.scatter_choosedata = make_combobox(datachoices)
        self.scatter_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.scatter_choosedata.setObjectName(_fromUtf8("scatter_choosedata"))
        self.scatter_choosedata_hlayout.addWidget(self.scatter_choosedata)

        self.figname_label = QtGui.QLabel(self.scatter)
        self.figname_label.setObjectName(_fromUtf8("figname_label"))
        self.scatter_choosedata_hlayout.addWidget(self.figname_label)
        self.figname_text = QtGui.QLineEdit(self.scatter)
        self.figname_text.setObjectName(_fromUtf8("figname_text"))
        self.scatter_choosedata_hlayout.addWidget(self.figname_text)
        self.plot_title_label = QtGui.QLabel(self.scatter)
        self.plot_title_label.setObjectName(_fromUtf8("plot_title_label"))
        self.scatter_choosedata_hlayout.addWidget(self.plot_title_label)
        self.plot_title_text = QtGui.QLineEdit(self.scatter)
        self.plot_title_text.setObjectName(_fromUtf8("plot_title_text"))
        self.scatter_choosedata_hlayout.addWidget(self.plot_title_text)
        self.scatter_vlayout.addLayout(self.scatter_choosedata_hlayout)
        self.scatter_choosevars_hlayout = QtGui.QHBoxLayout()
        self.scatter_choosevars_hlayout.setMargin(11)
        self.scatter_choosevars_hlayout.setSpacing(6)
        self.scatter_choosevars_hlayout.setObjectName(_fromUtf8("scatter_choosevars_hlayout"))
        self.scatter_choosex_vlayout = QtGui.QVBoxLayout()
        self.scatter_choosex_vlayout.setMargin(11)
        self.scatter_choosex_vlayout.setSpacing(6)
        self.scatter_choosex_vlayout.setObjectName(_fromUtf8("scatter_choosex_vlayout"))
        self.scatter_choosex_label = QtGui.QLabel(self.scatter)
        self.scatter_choosex_label.setObjectName(_fromUtf8("scatter_choosex_label"))
        self.scatter_choosex_vlayout.addWidget(self.scatter_choosex_label)

        xvarchoices_comp = self.pysat_fun.data[self.scatter_choosedata.currentText()].df['comp'].columns.values
        for i in xvarchoices_comp:
            i = ('comp', i)
        xvarchoices_meta = self.pysat_fun.data[self.scatter_choosedata.currentText()].df['meta'].columns.values
        for i in xvarchoices_meta:
            i = ('meta', i)
        xvarchoices = xvarchoices_comp.append(xvarchoices_meta)
        self.xvar_choices = make_combobox(xvarchoices)
        self.scatter_choosex_vlayout.addWidget(self.xvar_choices)

        self.xtitle_hlayout = QtGui.QHBoxLayout()
        self.xtitle_hlayout.setMargin(11)
        self.xtitle_hlayout.setSpacing(6)
        self.xtitle_hlayout.setObjectName(_fromUtf8("xtitle_hlayout"))
        self.xtitle_label = QtGui.QLabel(self.scatter)
        self.xtitle_label.setObjectName(_fromUtf8("xtitle_label"))
        self.xtitle_hlayout.addWidget(self.xtitle_label)
        self.xtitle_text = QtGui.QLineEdit(self.scatter)
        self.xtitle_text.setObjectName(_fromUtf8("xtitle_text"))
        self.xtitle_hlayout.addWidget(self.xtitle_text)
        self.scatter_choosex_vlayout.addLayout(self.xtitle_hlayout)
        self.xrange_hlayout = QtGui.QHBoxLayout()
        self.xrange_hlayout.setMargin(11)
        self.xrange_hlayout.setSpacing(6)
        self.xrange_hlayout.setObjectName(_fromUtf8("xrange_hlayout"))
        self.xmin_label = QtGui.QLabel(self.scatter)
        self.xmin_label.setObjectName(_fromUtf8("xmin_label"))
        self.xrange_hlayout.addWidget(self.xmin_label)
        self.xmin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmin_spin.setObjectName(_fromUtf8("xmin_spin"))
        self.xrange_hlayout.addWidget(self.xmin_spin)
        self.xmax_label = QtGui.QLabel(self.scatter)
        self.xmax_label.setObjectName(_fromUtf8("xmax_label"))
        self.xrange_hlayout.addWidget(self.xmax_label)
        self.xmax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmax_spin.setObjectName(_fromUtf8("xmax_spin"))
        self.xrange_hlayout.addWidget(self.xmax_spin)
        self.scatter_choosex_vlayout.addLayout(self.xrange_hlayout)
        self.scatter_choosevars_hlayout.addLayout(self.scatter_choosex_vlayout)
        self.scatter_choosey_vlayout = QtGui.QVBoxLayout()
        self.scatter_choosey_vlayout.setMargin(11)
        self.scatter_choosey_vlayout.setSpacing(6)
        self.scatter_choosey_vlayout.setObjectName(_fromUtf8("scatter_choosey_vlayout"))
        self.scatter_choosey_label = QtGui.QLabel(self.scatter)
        self.scatter_choosey_label.setObjectName(_fromUtf8("scatter_choosey_label"))
        self.scatter_choosey_vlayout.addWidget(self.scatter_choosey_label)

        yvarchoices = self.pysat_fun.data[self.scatter_choosedata.currentText()].df['meta', 'comp'].columns.values
        self.yvar_choices = make_combobox(yvarchoices)
        self.scatter_choosey_vlayout.addWidget(self.yvar_choices)

        self.ytitle_hlayout = QtGui.QHBoxLayout()
        self.ytitle_hlayout.setMargin(11)
        self.ytitle_hlayout.setSpacing(6)
        self.ytitle_hlayout.setObjectName(_fromUtf8("ytitle_hlayout"))
        self.ytitle_label = QtGui.QLabel(self.scatter)
        self.ytitle_label.setObjectName(_fromUtf8("ytitle_label"))
        self.ytitle_hlayout.addWidget(self.ytitle_label)
        self.ytitle_text = QtGui.QLineEdit(self.scatter)
        self.ytitle_text.setObjectName(_fromUtf8("ytitle_text"))
        self.ytitle_hlayout.addWidget(self.ytitle_text)
        self.scatter_choosey_vlayout.addLayout(self.ytitle_hlayout)

        self.yrange_hlayout = QtGui.QHBoxLayout()
        self.yrange_hlayout.setMargin(11)
        self.yrange_hlayout.setSpacing(6)
        self.yrange_hlayout.setObjectName(_fromUtf8("yrange_hlayout"))
        self.ymin_label = QtGui.QLabel(self.scatter)
        self.ymin_label.setObjectName(_fromUtf8("ymin_label"))
        self.yrange_hlayout.addWidget(self.ymin_label)
        self.ymin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymin_spin.setObjectName(_fromUtf8("ymin_spin"))
        self.yrange_hlayout.addWidget(self.ymin_spin)
        self.ymax_label = QtGui.QLabel(self.scatter)
        self.ymax_label.setObjectName(_fromUtf8("ymax_label"))
        self.yrange_hlayout.addWidget(self.ymax_label)
        self.ymax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymax_spin.setObjectName(_fromUtf8("ymax_spin"))
        self.yrange_hlayout.addWidget(self.ymax_spin)

        self.scatter_choosey_vlayout.addLayout(self.yrange_hlayout)
        self.scatter_choosevars_hlayout.addLayout(self.scatter_choosey_vlayout)
        self.scatter_vlayout.addLayout(self.scatter_choosevars_hlayout)
        self.legend_hlayout = QtGui.QHBoxLayout()
        self.legend_hlayout.setMargin(11)
        self.legend_hlayout.setSpacing(6)
        self.legend_hlayout.setObjectName(_fromUtf8("legend_hlayout"))
        self.legend_label = QtGui.QLabel(self.scatter)
        self.legend_label.setObjectName(_fromUtf8("legend_label"))
        self.legend_hlayout.addWidget(self.legend_label)
        self.legend_label_text = QtGui.QLineEdit(self.scatter)
        self.legend_label_text.setObjectName(_fromUtf8("legend_label_text"))
        self.legend_hlayout.addWidget(self.legend_label_text)
        self.onetoone = QtGui.QCheckBox(self.scatter)
        self.onetoone.setObjectName(_fromUtf8("onetoone"))
        self.legend_hlayout.addWidget(self.onetoone)
        self.scatter_vlayout.addLayout(self.legend_hlayout)
        self.scatter_color_file_hlayout = QtGui.QHBoxLayout()
        self.scatter_color_file_hlayout.setMargin(11)
        self.scatter_color_file_hlayout.setSpacing(6)
        self.scatter_color_file_hlayout.setObjectName(_fromUtf8("scatter_color_file_hlayout"))
        self.color_label = QtGui.QLabel(self.scatter)
        self.color_label.setObjectName(_fromUtf8("color_label"))
        self.scatter_color_file_hlayout.addWidget(self.color_label)
        self.color_choices = QtGui.QComboBox(self.scatter)
        self.color_choices.setIconSize(QtCore.QSize(50, 20))
        self.color_choices.setObjectName(_fromUtf8("color_choices"))
        self.color_choices.addItem(_fromUtf8("Red"))
        self.color_choices.addItem(_fromUtf8("Green"))
        self.color_choices.addItem(_fromUtf8("Blue"))
        self.color_choices.addItem(_fromUtf8("Cyan"))
        self.color_choices.addItem(_fromUtf8("Yellow"))
        self.color_choices.addItem(_fromUtf8("Magenta"))
        self.color_choices.addItem(_fromUtf8("Black"))
        self.scatter_color_file_hlayout.addWidget(self.color_choices)
        self.file_label = QtGui.QLabel(self.scatter)
        self.file_label.setObjectName(_fromUtf8("file_label"))
        self.scatter_color_file_hlayout.addWidget(self.file_label)
        self.file_text = QtGui.QLineEdit(self.scatter)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.scatter_color_file_hlayout.addWidget(self.file_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.scatter_color_file_hlayout.addItem(spacerItem)
        self.scatter_vlayout.addLayout(self.scatter_color_file_hlayout)
        self.verticalLayout.addLayout(self.scatter_vlayout)
        self.verticalLayout_8.addWidget(self.scatter)
        self.scatter.raise_()

        self.scatter_choosedata.activated[int].connect(lambda: self.scatter_change_vars(self.xvar_choices))
        self.yvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))
        self.yvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))
        self.scatter_choosedata.activated[int].connect(lambda: self.scatter_change_vars(self.yvar_choices))
        self.yvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))

    def scatter_change_vars(self, obj):
        obj.clear()
        choices = self.pysat_fun.data[self.scatter_choosedata.currentText()].df['meta', 'comp'].columns.values
        print(choices)
        obj.addItems(choices)

    def get_minmax(self, objmin, objmax, var):
        vardata = self.pysat_fun.data[self.scatter_choosedata.currentText()].df[var]
        varmin = np.min(vardata)
        varmax = np.max(vardata)
        objmin.setValue(varmin)
        objmax.setValue(varmax)


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
