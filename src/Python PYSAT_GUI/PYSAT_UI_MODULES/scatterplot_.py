from PYSAT_UI_MODULES.Error_ import error_print
from PyQt4 import QtCore, QtGui
import numpy as np
import inspect

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

        xvar = (self.vars_level0[self.vars_level1.index(xvar)], xvar)
        yvar = (self.vars_level0[self.vars_level1.index(yvar)], yvar)
        figname = self.figname_text.text()
        title = self.plot_title_text.text()
        xrange = [self.xmin_spin.value(), self.xmax_spin.value()]
        yrange = [self.ymin_spin.value(), self.ymax_spin.value()]
        xtitle = self.xtitle_text.text()
        ytitle = self.ytitle_text.text()
        lbls = self.legend_label_text.text()
        one_to_one = self.onetoone.isChecked()
        figfile = self.file_text.text()
        colors = [self.color_choices.currentText()]
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

    def scatterplot_ui(self):
        self.scatter = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scatter.setFont(font)
        self.scatter.setObjectName(_fromUtf8("scatter"))
        self.scatter_vlayout = QtGui.QVBoxLayout(self.scatter)
        self.scatter_vlayout.setMargin(11)
        self.scatter_vlayout.setSpacing(6)
        self.scatter_vlayout.setObjectName(_fromUtf8("scatter_vlayout"))

        self.scatter_choosedata_hlayout = QtGui.QHBoxLayout()
        self.scatter_choosedata_hlayout.setMargin(11)
        self.scatter_choosedata_hlayout.setSpacing(6)
        self.scatter_choosedata_hlayout.setObjectName(_fromUtf8("scatter_choosedata_hlayout"))

        self.scatter_choosedata_label = QtGui.QLabel(self.scatter)
        self.scatter_choosedata_label.setObjectName(_fromUtf8("scatter_choosedata_label"))
        self.scatter_choosedata_label.setText('Choose data: ')
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
        self.figname_label.setText('Figure name: ')
        self.scatter_choosedata_hlayout.addWidget(self.figname_label)
        self.figname_text = QtGui.QLineEdit(self.scatter)
        self.figname_text.setObjectName(_fromUtf8("figname_text"))
        self.scatter_choosedata_hlayout.addWidget(self.figname_text)
        self.plot_title_label = QtGui.QLabel(self.scatter)
        self.plot_title_label.setObjectName(_fromUtf8("plot_title_label"))
        self.plot_title_label.setText('Plot title: ')
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
        self.scatter_choosex_label.setText('Choose X variable: ')
        self.scatter_choosex_vlayout.addWidget(self.scatter_choosex_label)
        self.vars_level0 = self.pysat_fun.data[self.scatter_choosedata.currentText()].df.columns.get_level_values(0)
        self.vars_level1 = self.pysat_fun.data[self.scatter_choosedata.currentText()].df.columns.get_level_values(1)
        self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
        self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])
        xvarchoices = self.vars_level1
        self.xvar_choices = make_combobox(xvarchoices)
        self.xvar_choices.SizeAdjustPolicy(0)
        self.scatter_choosex_vlayout.addWidget(self.xvar_choices)
        self.xtitle_hlayout = QtGui.QHBoxLayout()
        self.xtitle_hlayout.setMargin(11)
        self.xtitle_hlayout.setSpacing(6)
        self.xtitle_hlayout.setObjectName(_fromUtf8("xtitle_hlayout"))
        self.xtitle_label = QtGui.QLabel(self.scatter)
        self.xtitle_label.setObjectName(_fromUtf8("xtitle_label"))
        self.xtitle_label.setText('X title: ')
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
        self.xmin_label.setText('X min: ')
        self.xrange_hlayout.addWidget(self.xmin_label)
        self.xmin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmin_spin.setObjectName(_fromUtf8("xmin_spin"))
        self.xmin_spin.setRange(0, 10000000)
        self.xrange_hlayout.addWidget(self.xmin_spin)
        self.xmax_label = QtGui.QLabel(self.scatter)
        self.xmax_label.setObjectName(_fromUtf8("xmax_label"))
        self.xmax_label.setText('X max: ')
        self.xrange_hlayout.addWidget(self.xmax_label)
        self.xmax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmax_spin.setObjectName(_fromUtf8("xmax_spin"))
        self.xmax_spin.setRange(0, 10000000)
        self.xrange_hlayout.addWidget(self.xmax_spin)
        self.scatter_choosex_vlayout.addLayout(self.xrange_hlayout)
        self.scatter_choosevars_hlayout.addLayout(self.scatter_choosex_vlayout)

        self.scatter_choosey_vlayout = QtGui.QVBoxLayout()
        self.scatter_choosey_vlayout.setMargin(11)
        self.scatter_choosey_vlayout.setSpacing(6)
        self.scatter_choosey_vlayout.setObjectName(_fromUtf8("scatter_choosey_vlayout"))
        self.scatter_choosey_label = QtGui.QLabel(self.scatter)
        self.scatter_choosey_label.setObjectName(_fromUtf8("scatter_choosey_label"))
        self.scatter_choosey_label.setText('Choose Y variable: ')
        self.scatter_choosey_vlayout.addWidget(self.scatter_choosey_label)
        yvarchoices = xvarchoices
        self.yvar_choices = make_combobox(yvarchoices)
        self.yvar_choices.SizeAdjustPolicy(0)
        self.scatter_choosey_vlayout.addWidget(self.yvar_choices)
        self.ytitle_hlayout = QtGui.QHBoxLayout()
        self.ytitle_hlayout.setMargin(11)
        self.ytitle_hlayout.setSpacing(6)
        self.ytitle_hlayout.setObjectName(_fromUtf8("ytitle_hlayout"))
        self.ytitle_label = QtGui.QLabel(self.scatter)
        self.ytitle_label.setObjectName(_fromUtf8("ytitle_label"))
        self.ytitle_label.setText('Y title: ')
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
        self.ymin_label.setText('Y min: ')
        self.yrange_hlayout.addWidget(self.ymin_label)
        self.ymin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymin_spin.setObjectName(_fromUtf8("ymin_spin"))
        self.ymin_spin.setRange(0, 10000000)
        self.yrange_hlayout.addWidget(self.ymin_spin)
        self.ymax_label = QtGui.QLabel(self.scatter)
        self.ymax_label.setObjectName(_fromUtf8("ymax_label"))
        self.ymax_label.setText('Y max: ')
        self.yrange_hlayout.addWidget(self.ymax_label)
        self.ymax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymax_spin.setObjectName(_fromUtf8("ymax_spin"))
        self.ymin_spin.setRange(0, 10000000)
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
        self.legend_label.setText('Legend label: ')
        self.legend_hlayout.addWidget(self.legend_label)
        self.legend_label_text = QtGui.QLineEdit(self.scatter)
        self.legend_label_text.setObjectName(_fromUtf8("legend_label_text"))
        self.legend_hlayout.addWidget(self.legend_label_text)
        self.onetoone = QtGui.QCheckBox(self.scatter)
        self.onetoone.setObjectName(_fromUtf8("onetoone"))
        self.onetoone.setText('One to One')
        self.legend_hlayout.addWidget(self.onetoone)
        self.scatter_vlayout.addLayout(self.legend_hlayout)
        self.scatter_color_file_hlayout = QtGui.QHBoxLayout()
        self.scatter_color_file_hlayout.setMargin(11)
        self.scatter_color_file_hlayout.setSpacing(6)
        self.scatter_color_file_hlayout.setObjectName(_fromUtf8("scatter_color_file_hlayout"))
        self.color_label = QtGui.QLabel(self.scatter)
        self.color_label.setObjectName(_fromUtf8("color_label"))
        self.color_label.setText('Color: ')
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
        self.file_label.setText('Plot filename: ')
        self.scatter_color_file_hlayout.addWidget(self.file_label)
        self.file_text = QtGui.QLineEdit(self.scatter)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.scatter_color_file_hlayout.addWidget(self.file_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.scatter_color_file_hlayout.addItem(spacerItem)
        self.scatter_vlayout.addLayout(self.scatter_color_file_hlayout)

        self.verticalLayout_8.addWidget(self.scatter)
        self.scatter.raise_()
        self.scatter.setTitle(_translate("scatter", "Scatterplot", None))

        self.scatter_choosedata.activated[int].connect(lambda: self.scatter_change_vars(self.xvar_choices))
        self.xvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.xmin_spin, self.xmax_spin, self.xvar_choices.currentText()))
        self.scatter_choosedata.activated[int].connect(lambda: self.scatter_change_vars(self.yvar_choices))
        self.yvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))
        self.color_choices.activated.connect(lambda: self.get_scatterplot_parameters())
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, QtGui.QComboBox):
                obj.currentIndexChanged.connect(lambda: self.get_scatterplot_parameters())
            if isinstance(obj, QtGui.QLineEdit):
                obj.textChanged.connect(lambda: self.get_scatterplot_parameters())
            if isinstance(obj, QtGui.QDoubleSpinBox):
                obj.valueChanged.connect(lambda: self.get_scatterplot_parameters())
            if isinstance(obj, QtGui.QCheckBox):
                obj.toggled.connect(lambda: self.get_scatterplot_parameters())
                #
                #        self.scatter_choosedata.currentIndexChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.xvar_choices.currentIndexChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.yvar_choices.currentIndexChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.xmin_spin.valueChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.ymin_spin.valueChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.xmax_spin.valueChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.ymax_spin.valueChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.xtitle_text.textChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.ytitle_text.textChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.legend_label_text.textChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.figname_text.textChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.plot_title_text.textChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.onetoone.toggled.connect(lambda: self.get_scatterplot_parameters())
                #        self.color_choices.currentIndexChanged.connect(lambda: self.get_scatterplot_parameters())
                #        self.file_text.textChanged.connect(lambda: self.get_scatterplot_parameters())

    def scatter_change_vars(self, obj):
        obj.clear()
        choices = self.pysat_fun.data[self.scatter_choosedata.currentText()].df[['meta', 'comp']].columns.values
        for i in choices:        
            obj.addItem(i[1])

    def get_minmax(self, objmin, objmax, var):
        varind = self.vars_level1.index(var)
        vartuple = (self.vars_level0[varind], self.vars_level1[varind])
        vardata = self.pysat_fun.data[self.scatter_choosedata.currentText()].df[vartuple]
        varmin = np.min(vardata)
        varmax = np.max(vardata)
        objmin.setValue(varmin)
        objmax.setValue(varmax)


def make_combobox(choices):
    combo = QtGui.QComboBox()

    for i, choice in enumerate(choices):
        combo.addItem(_fromUtf8(""))
        combo.setItemText(i, str(choice))

    return combo


def make_listwidget(choices):
    listwidget = QtGui.QListWidget()
    listwidget.setItemDelegate
    for item in choices:
        item = QtGui.QListWidgetItem(item)
        listwidget.addItem(item)
    return listwidget
