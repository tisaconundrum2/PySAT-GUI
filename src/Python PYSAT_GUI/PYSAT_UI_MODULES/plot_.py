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


class plot_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.main()

    def main(self):
        self.pysat_fun.set_fun_list(self.pysat_fun.do_plot)
        self.pysat_fun.set_arg_list([])
        self.pysat_fun.set_kw_list({})
        self.pysat_fun.set_greyed_modules({})
        self.plot_ui()
        self.pysat_fun.set_greyed_modules(self.plot, True)

    def get_plot_parameters(self):

        datakey = self.plot_choosedata.currentText()
        xvar = self.xvar_choices.currentText()
        yvar = self.yvar_choices.currentText()
        try:
            xvar = (self.vars_level0[self.vars_level1.index(xvar)], xvar)
            yvar = (self.vars_level0[self.vars_level1.index(yvar)], yvar)
        except:
            print('Problem setting x and/or y variable!')
            pass
        figname = self.figname_text.text()
        title = self.plot_title_text.text()
        xrange = self.xmin_spin.value(), self.xmax_spin.value()
        yrange = self.ymin_spin.value(), self.ymax_spin.value()
        xtitle = self.xtitle_text.text()
        ytitle = self.ytitle_text.text()
        lbl = self.legend_label_text.text()
        one_to_one = self.onetoone.isChecked()
        figfile = self.file_text.text()
        
        color = self.color_choices.currentText()
        alpha=self.alpha_spin.value()    

        if color=='Red':
            color=[1,0,0,alpha]
        if color=='Green':
            color=[0,1,0,alpha]
        if color=='Blue':
            color=[0,0,1,alpha]
        if color=='Cyan':
            color=[0,1,1,alpha]
        if color=='Yellow':
            color=[1,1,0,alpha]
        if color=='Magenta':
            color=[1,0,1,alpha]
        if color=='Black':
            color=[0,0,0,alpha]

        
        marker=self.marker_choices.currentText()        
        if marker=='Circles':
            marker='o'
        if marker=='Squares':
            marker='s'
        if marker=='Diamonds':
            marker='D'
        if marker=='Triangle Up':
            marker='^'
        if marker=='Triangle Down':
            marker='v'
        if marker=='Triangle Right':
            marker='>'
        if marker=='Triangle Left':
            marker='<'
        
        
        line=self.line_choices.currentText()
        if line=='No Line':
            linestyle='None'
        if line=='Line':
            linestyle='-'
        if line=='Dashed Line':
            linestyle='--'
        if line=='Dotted Line':
            linestyle=':'
            
            
        args = [datakey, xvar, yvar]
        kws = {'figname': figname,
               'title': title,
               'xrange': xrange,
               'yrange': yrange,
               'xtitle': xtitle,
               'ytitle': ytitle,
               'lbl': lbl,
               'one_to_one': one_to_one,
               'figfile': figfile,
               'color': color,
               'marker': marker,
               'linestyle':linestyle
               }
        self.pysat_fun.set_arg_list(args, replacelast=True)
        self.pysat_fun.set_kw_list(kws, replacelast=True)

    def plot_ui(self):
        self.scatter = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scatter.setFont(font)
        self.scatter.setObjectName(_fromUtf8("scatter"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scatter)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scatter_choosedata_form = QtGui.QFormLayout()
        self.scatter_choosedata_form.setMargin(11)
        self.scatter_choosedata_form.setSpacing(6)
        self.scatter_choosedata_form.setObjectName(_fromUtf8("scatter_choosedata_form"))
        self.scatter_choosedata_label = QtGui.QLabel(self.scatter)
        self.scatter_choosedata_label.setObjectName(_fromUtf8("scatter_choosedata_label"))
        self.scatter_choosedata_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.scatter_choosedata_label)
        self.scatter_choosedata = QtGui.QComboBox(self.scatter)
        self.scatter_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.scatter_choosedata.setObjectName(_fromUtf8("scatter_choosedata"))
        self.scatter_choosedata_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.scatter_choosedata)
        self.figname_label = QtGui.QLabel(self.scatter)
        self.figname_label.setObjectName(_fromUtf8("figname_label"))
        self.scatter_choosedata_form.setWidget(1, QtGui.QFormLayout.LabelRole, self.figname_label)
        self.figname_text = QtGui.QLineEdit(self.scatter)
        self.figname_text.setObjectName(_fromUtf8("figname_text"))
        self.scatter_choosedata_form.setWidget(1, QtGui.QFormLayout.FieldRole, self.figname_text)
        self.plot_title_label = QtGui.QLabel(self.scatter)
        self.plot_title_label.setObjectName(_fromUtf8("plot_title_label"))
        self.scatter_choosedata_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.plot_title_label)
        self.plot_title_text = QtGui.QLineEdit(self.scatter)
        self.plot_title_text.setEnabled(True)
        self.plot_title_text.setObjectName(_fromUtf8("plot_title_text"))
        self.scatter_choosedata_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.plot_title_text)
        self.verticalLayout.addLayout(self.scatter_choosedata_form)
        self.line = QtGui.QFrame(self.scatter)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.scatter_choosex_form = QtGui.QFormLayout()
        self.scatter_choosex_form.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.scatter_choosex_form.setMargin(11)
        self.scatter_choosex_form.setSpacing(6)
        self.scatter_choosex_form.setObjectName(_fromUtf8("scatter_choosex_form"))
        self.scatter_choosex_label = QtGui.QLabel(self.scatter)
        self.scatter_choosex_label.setObjectName(_fromUtf8("scatter_choosex_label"))
        self.scatter_choosex_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.scatter_choosex_label)
        self.xvar_choices = QtGui.QComboBox(self.scatter)
        self.xvar_choices.setObjectName(_fromUtf8("xvar_choices"))
        self.scatter_choosex_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.xvar_choices)
        self.xtitle_label = QtGui.QLabel(self.scatter)
        self.xtitle_label.setObjectName(_fromUtf8("xtitle_label"))
        self.scatter_choosex_form.setWidget(1, QtGui.QFormLayout.LabelRole, self.xtitle_label)
        self.xtitle_hlayout = QtGui.QHBoxLayout()
        self.xtitle_hlayout.setMargin(11)
        self.xtitle_hlayout.setSpacing(6)
        self.xtitle_hlayout.setObjectName(_fromUtf8("xtitle_hlayout"))
        self.xtitle_text = QtGui.QLineEdit(self.scatter)
        self.xtitle_text.setObjectName(_fromUtf8("xtitle_text"))
        self.xtitle_hlayout.addWidget(self.xtitle_text)
        self.scatter_choosex_form.setLayout(1, QtGui.QFormLayout.FieldRole, self.xtitle_hlayout)
        self.xmin_label = QtGui.QLabel(self.scatter)
        self.xmin_label.setObjectName(_fromUtf8("xmin_label"))
        self.scatter_choosex_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.xmin_label)
        self.xmin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmin_spin.setObjectName(_fromUtf8("xmin_spin"))
        self.scatter_choosex_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.xmin_spin)
        self.xmax_label = QtGui.QLabel(self.scatter)
        self.xmax_label.setObjectName(_fromUtf8("xmax_label"))
        self.scatter_choosex_form.setWidget(3, QtGui.QFormLayout.LabelRole, self.xmax_label)
        self.xmax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.xmax_spin.setObjectName(_fromUtf8("xmax_spin"))
        self.scatter_choosex_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.xmax_spin)
        self.verticalLayout.addLayout(self.scatter_choosex_form)
        self.scatter_choosey_form = QtGui.QFormLayout()
        self.scatter_choosey_form.setMargin(11)
        self.scatter_choosey_form.setSpacing(6)
        self.scatter_choosey_form.setObjectName(_fromUtf8("scatter_choosey_form"))
        self.yvar_choices = QtGui.QComboBox(self.scatter)
        self.yvar_choices.setObjectName(_fromUtf8("yvar_choices"))
        self.scatter_choosey_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.yvar_choices)
        self.ytitle_label = QtGui.QLabel(self.scatter)
        self.ytitle_label.setObjectName(_fromUtf8("ytitle_label"))
        self.scatter_choosey_form.setWidget(1, QtGui.QFormLayout.LabelRole, self.ytitle_label)
        self.ytitle_text = QtGui.QLineEdit(self.scatter)
        self.ytitle_text.setObjectName(_fromUtf8("ytitle_text"))
        self.scatter_choosey_form.setWidget(1, QtGui.QFormLayout.FieldRole, self.ytitle_text)
        self.ymin_label = QtGui.QLabel(self.scatter)
        self.ymin_label.setObjectName(_fromUtf8("ymin_label"))
        self.scatter_choosey_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.ymin_label)
        self.ymin_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymin_spin.setObjectName(_fromUtf8("ymin_spin"))
        self.scatter_choosey_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.ymin_spin)
        self.ymax_label = QtGui.QLabel(self.scatter)
        self.ymax_label.setObjectName(_fromUtf8("ymax_label"))
        self.scatter_choosey_form.setWidget(3, QtGui.QFormLayout.LabelRole, self.ymax_label)
        self.ymax_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.ymax_spin.setObjectName(_fromUtf8("ymax_spin"))
        self.scatter_choosey_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.ymax_spin)
        self.scatter_choosey_label = QtGui.QLabel(self.scatter)
        self.scatter_choosey_label.setObjectName(_fromUtf8("scatter_choosey_label"))
        self.scatter_choosey_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.scatter_choosey_label)
        self.verticalLayout.addLayout(self.scatter_choosey_form)
        self.line_1 = QtGui.QFrame(self.scatter)
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.verticalLayout.addWidget(self.line_1)
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
        self.verticalLayout.addLayout(self.legend_hlayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.color_label = QtGui.QLabel(self.scatter)
        self.color_label.setObjectName(_fromUtf8("color_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.color_label)
        self.color_choices = QtGui.QComboBox(self.scatter)
        self.color_choices.setIconSize(QtCore.QSize(50, 20))
        self.color_choices.setObjectName(_fromUtf8("color_choices"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.color_choices)
        self.line_label = QtGui.QLabel(self.scatter)
        self.line_label.setObjectName(_fromUtf8("line_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_label)
        self.line_choices = QtGui.QComboBox(self.scatter)
        self.line_choices.setIconSize(QtCore.QSize(50, 20))
        self.line_choices.setObjectName(_fromUtf8("line_choices"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_choices)
        self.marker_label = QtGui.QLabel(self.scatter)
        self.marker_label.setObjectName(_fromUtf8("marker_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.marker_label)
        self.marker_choices = QtGui.QComboBox(self.scatter)
        self.marker_choices.setIconSize(QtCore.QSize(50, 20))
        self.marker_choices.setObjectName(_fromUtf8("marker_choices"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.marker_choices)
        self.file_label = QtGui.QLabel(self.scatter)
        self.file_label.setObjectName(_fromUtf8("file_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.file_label)
        self.file_text = QtGui.QLineEdit(self.scatter)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.file_text)
        self.alpha_label = QtGui.QLabel(self.scatter)
        self.alpha_label.setObjectName(_fromUtf8("alpha_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.alpha_label)
        self.alpha_spin = QtGui.QDoubleSpinBox(self.scatter)
        self.alpha_spin.setObjectName(_fromUtf8("alpha_spin"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.alpha_spin)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_8.addWidget(self.scatter)

        self.scatter.setTitle(_translate("MainWindow", "Scatter Plot", None))
        self.scatter_choosedata_label.setText(_translate("MainWindow", "Choose data: ", None))
        self.scatter_choosedata.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.scatter_choosedata.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.figname_label.setText(_translate("MainWindow", "Figure name:", None))
        self.plot_title_label.setText(_translate("MainWindow", "Plot Title: ", None))
        self.scatter_choosex_label.setText(_translate("MainWindow", "Choose X variable: ", None))
        self.xtitle_label.setText(_translate("MainWindow", "X title:", None))
        self.xmin_label.setText(_translate("MainWindow", "X min:", None))
        self.xmax_label.setText(_translate("MainWindow", "X max:", None))
        self.ytitle_label.setText(_translate("MainWindow", "Y title:", None))
        self.ymin_label.setText(_translate("MainWindow", "Y min:", None))
        self.ymax_label.setText(_translate("MainWindow", "Y max:", None))
        self.scatter_choosey_label.setText(_translate("MainWindow", "Choose Y variable: ", None))
        self.legend_label.setText(_translate("MainWindow", "Legend Label: ", None))
        self.onetoone.setText(_translate("MainWindow", "One to One", None))
        self.color_label.setText(_translate("MainWindow", "Color:", None))
        self.color_choices.setItemText(0, _translate("MainWindow", "Red", None))
        self.color_choices.setItemText(1, _translate("MainWindow", "Green", None))
        self.color_choices.setItemText(2, _translate("MainWindow", "Blue", None))
        self.color_choices.setItemText(3, _translate("MainWindow", "Cyan", None))
        self.color_choices.setItemText(4, _translate("MainWindow", "Magenta", None))
        self.color_choices.setItemText(5, _translate("MainWindow", "Yellow", None))
        self.color_choices.setItemText(6, _translate("MainWindow", "Black", None))
        self.line_label.setText(_translate("MainWindow", "Line:", None))
        self.line_choices.setItemText(0, _translate("MainWindow", "No Line", None))
        self.line_choices.setItemText(1, _translate("MainWindow", "Line", None))
        self.line_choices.setItemText(2, _translate("MainWindow", "Dashed Line", None))
        self.line_choices.setItemText(3, _translate("MainWindow", "Dotted Line", None))
        self.marker_label.setText(_translate("MainWindow", "Marker:", None))
        self.marker_choices.setItemText(0, _translate("MainWindow", "Circles", None))
        self.marker_choices.setItemText(1, _translate("MainWindow", "Squares", None))
        self.marker_choices.setItemText(2, _translate("MainWindow", "Diamonds", None))
        self.marker_choices.setItemText(3, _translate("MainWindow", "Triangle Up", None))
        self.marker_choices.setItemText(4, _translate("MainWindow", "Triangle Down", None))
        self.marker_choices.setItemText(5, _translate("MainWindow", "Triangle Left", None))
        self.marker_choices.setItemText(6, _translate("MainWindow", "Triangle Right", None))
        self.marker_choices.setItemText(7, _translate("MainWindow", "None", None))
        self.file_label.setText(_translate("MainWindow", "Plot Filename:", None))
        self.alpha_label.setText(_translate("MainWindow", "Alpha:", None))

        self.alpha_spin = QtGui.QDoubleSpinBox(self.plot)
        self.alpha_spin.setObjectName(_fromUtf8("alpha_spin"))
        self.alpha_spin.setRange(0, 1)
        self.alpha_spin.setValue(0.5)
        self.alpha_spin.setSingleStep(0.1)
        self.plot_appearance_options.addWidget(self.alpha_spin)


        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.plot_appearance_options.addItem(spacerItem)
        self.plot_vlayout.addLayout(self.plot_appearance_options)

        self.file_hlayout = QtGui.QHBoxLayout()

        self.file_label = QtGui.QLabel(self.plot)
        self.file_label.setObjectName(_fromUtf8("file_label"))
        self.file_label.setText('Plot filename: ')
        self.file_hlayout.addWidget(self.file_label)
        self.file_text = QtGui.QLineEdit(self.plot)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.file_hlayout.addWidget(self.file_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.file_hlayout.addItem(spacerItem)

        self.plot_vlayout.addLayout(self.file_hlayout)

        self.verticalLayout_8.addWidget(self.plot)
        self.plot.raise_()
        self.plot.setTitle(_translate("plot", "Plot", None))

        self.plot_choosedata.activated[int].connect(lambda: self.plot_change_vars(self.xvar_choices))

        self.plot_choosedata.activated[int].connect(
            lambda: self.get_minmax(self.xmin_spin, self.xmax_spin, self.xvar_choices.currentText()))
        self.plot_choosedata.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))

        self.xvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.xmin_spin, self.xmax_spin, self.xvar_choices.currentText()))
        self.plot_choosedata.activated[int].connect(lambda: self.plot_change_vars(self.yvar_choices))
        self.yvar_choices.activated[int].connect(
            lambda: self.get_minmax(self.ymin_spin, self.ymax_spin, self.yvar_choices.currentText()))
        self.color_choices.activated.connect(lambda: self.get_plot_parameters())

        for name, obj in inspect.getmembers(self):
            if isinstance(obj, QtGui.QComboBox):
                obj.currentIndexChanged.connect(lambda: self.get_plot_parameters())
            if isinstance(obj, QtGui.QLineEdit):
                obj.textChanged.connect(lambda: self.get_plot_parameters())
            if isinstance(obj, QtGui.QDoubleSpinBox):
                obj.valueChanged.connect(lambda: self.get_plot_parameters())
            if isinstance(obj, QtGui.QCheckBox):
                obj.toggled.connect(lambda: self.get_plot_parameters())

                       self.plot_choosedata.currentIndexChanged.connect(lambda: self.get_plot_parameters())
                       self.xvar_choices.currentIndexChanged.connect(lambda: self.get_plot_parameters())
                       self.yvar_choices.currentIndexChanged.connect(lambda: self.get_plot_parameters())
                       self.xmin_spin.valueChanged.connect(lambda: self.get_plot_parameters())
                       self.ymin_spin.valueChanged.connect(lambda: self.get_plot_parameters())
                       self.xmax_spin.valueChanged.connect(lambda: self.get_plot_parameters())
                       self.ymax_spin.valueChanged.connect(lambda: self.get_plot_parameters())
                       self.xtitle_text.textChanged.connect(lambda: self.get_plot_parameters())
                       self.ytitle_text.textChanged.connect(lambda: self.get_plot_parameters())
                       self.legend_label_text.textChanged.connect(lambda: self.get_plot_parameters())
                       self.figname_text.textChanged.connect(lambda: self.get_plot_parameters())
                       self.plot_title_text.textChanged.connect(lambda: self.get_plot_parameters())
                       self.onetoone.toggled.connect(lambda: self.get_plot_parameters())
                       self.color_choices.currentIndexChanged.connect(lambda: self.get_plot_parameters())
                       self.file_text.textChanged.connect(lambda: self.get_plot_parameters())

    def plot_change_vars(self, obj):
        obj.clear()
        try:
            self.vars_level0 = self.pysat_fun.data[self.plot_choosedata.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.pysat_fun.data[self.plot_choosedata.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])

            choices = self.vars_level1

            for i in choices:
                obj.addItem(i)
        except:
            try:
                choices=self.pysat_fun.data[self.plot_choosedata.currentText()].columns.values
                for i in choices:
                    obj.addItem(i)
            except:
                choices=['No valid choices']

    def get_minmax(self, objmin, objmax, var):
        try:
            varind = self.vars_level1.index(var)
            vartuple = (self.vars_level0[varind], self.vars_level1[varind])
            vardata = self.pysat_fun.data[self.plot_choosedata.currentText()].df[vartuple]

        except:
            try:
                vardata=self.pysat_fun.data[self.plot_choosedata.currentText()][var]
            except:
                vardata=[0,0]
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
