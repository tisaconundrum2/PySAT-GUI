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


class sm_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.main()

    def get_sm_params(self):
        pass

    def main(self):
        # driver function, calls UI and set's up connections
        # add function list calls here
        self.pysat_fun.set_fun_list(self.pysat_fun.do_submodel_predict)
        self.sm_ui()



    def sm_ui(self):
        self.submodel_opt = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submodel_opt.setFont(font)
        self.submodel_opt.setObjectName(_fromUtf8("submodel_opt"))
        self.verticalLayout = QtGui.QVBoxLayout(self.submodel_opt)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        #choose reference/full model
        self.choosemodel_hlayout = QtGui.QHBoxLayout()
        self.choosemodel_hlayout.setMargin(11)
        self.choosemodel_hlayout.setSpacing(6)
        self.choosemodel_hlayout.setObjectName(_fromUtf8("choosemodel_hlayout"))
        self.choosemodel_label = QtGui.QLabel(self.submodel_opt)
        self.choosemodel_label.setObjectName(_fromUtf8("choosemodel_label"))
        self.choosemodel_hlayout.addWidget(self.choosemodel_label)
        modelchoices = self.pysat_fun.modelkeys
        if modelchoices == []:
            error_print('No model has been trained')
            modelchoices = ['No model has been trained!']
        self.choosemodel = make_combobox(modelchoices)
        self.choosemodel_hlayout.addWidget(self.choosemodel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choosemodel_hlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosemodel_hlayout)

        #organize submodels vertically
        self.submodels_vlayout = QtGui.QVBoxLayout()
        self.submodels_vlayout.setMargin(11)
        self.submodels_vlayout.setSpacing(6)
        self.submodels_vlayout.setObjectName(_fromUtf8("submodels_vlayout"))

        #always have a low submodel
        self.low_model_hlayout = QtGui.QHBoxLayout()
        self.low_model_hlayout.setMargin(11)
        self.low_model_hlayout.setSpacing(6)
        self.low_model_hlayout.setObjectName(_fromUtf8("low_model_hlayout"))
        self.choose_low_model = make_combobox(modelchoices)
        self.low_model_hlayout.addWidget(self.choose_low_model)
        self.low_model_max_label = QtGui.QLabel(self.submodel_opt)
        self.low_model_max_label.setObjectName(_fromUtf8("low_model_max_label"))
        self.low_model_hlayout.addWidget(self.low_model_max_label)
        self.low_model_max = QtGui.QDoubleSpinBox(self.submodel_opt)
        self.low_model_max.setObjectName(_fromUtf8("low_model_max"))
        self.low_model_max.setMaximum(1000)
        self.low_model_max.setMinimum(-1000)

        self.low_model_hlayout.addWidget(self.low_model_max)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.low_model_hlayout.addItem(spacerItem1)
        self.submodels_vlayout.addLayout(self.low_model_hlayout)
        self.set_ranges(self.choose_low_model.currentText(), maxspin=self.low_model_max)

        #middle submodels go here
        self.midmodel_vlayout=QtGui.QVBoxLayout()
        self.submodels_vlayout.addLayout(self.midmodel_vlayout)

        #always have a high submodel
        self.high_model_hlayout = QtGui.QHBoxLayout()
        self.high_model_hlayout.setMargin(11)
        self.high_model_hlayout.setSpacing(6)
        self.high_model_hlayout.setObjectName(_fromUtf8("high_model_hlayout"))
        self.choose_high_model = make_combobox(modelchoices)
        self.high_model_hlayout.addWidget(self.choose_high_model)
        self.high_model_min_label = QtGui.QLabel(self.submodel_opt)
        self.high_model_min_label.setObjectName(_fromUtf8("high_model_min_label"))
        self.high_model_hlayout.addWidget(self.high_model_min_label)
        self.high_model_min = QtGui.QDoubleSpinBox(self.submodel_opt)
        self.high_model_min.setObjectName(_fromUtf8("high_model_min"))
        self.high_model_min.setMaximum(1000)
        self.high_model_min.setMinimum(-1000)
        self.high_model_hlayout.addWidget(self.high_model_min)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.high_model_hlayout.addItem(spacerItem3)
        self.submodels_vlayout.addLayout(self.high_model_hlayout)
        self.verticalLayout.addLayout(self.submodels_vlayout)
        self.set_ranges(self.choose_high_model.currentText(), minspin=self.high_model_min)

        #add or delete submodel buttons
        self.add_delete_hlayout = QtGui.QHBoxLayout()
        self.add_delete_hlayout.setMargin(11)
        self.add_delete_hlayout.setSpacing(6)
        self.add_delete_hlayout.setObjectName(_fromUtf8("add_delete_hlayout"))
        self.add_submodel_button = QtGui.QPushButton(self.submodel_opt)
        self.add_submodel_button.setObjectName(_fromUtf8("add_submodel_button"))
        self.add_delete_hlayout.addWidget(self.add_submodel_button)
        self.delete_submodel_button = QtGui.QPushButton(self.submodel_opt)
        self.delete_submodel_button.setObjectName(_fromUtf8("delete_submodel_button"))
        self.add_delete_hlayout.addWidget(self.delete_submodel_button)
        self.optimize_checkbox = QtGui.QCheckBox(self.submodel_opt)
        self.optimize_checkbox.setObjectName(_fromUtf8("optimize_checkbox"))
        self.add_delete_hlayout.addWidget(self.optimize_checkbox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.add_delete_hlayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.add_delete_hlayout)

        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']

        #choose data to optimize blending
        self.choosedata_hlayout = QtGui.QHBoxLayout()
        self.choosedata_hlayout.setMargin(11)
        self.choosedata_hlayout.setSpacing(6)
        self.choosedata_hlayout.setObjectName(_fromUtf8("choosedata_hlayout"))
        self.verticalLayout.addLayout(self.choosedata_hlayout)

        #choose data to predict
        self.predictdata_vlayout = QtGui.QVBoxLayout()
        self.predictdata_vlayout.setMargin(11)
        self.predictdata_vlayout.setSpacing(6)
        self.predictdata_vlayout.setObjectName(_fromUtf8("predictdata_vlayout"))
        self.choosedata_predict_label = QtGui.QLabel(self.submodel_opt)
        self.choosedata_predict_label.setObjectName(_fromUtf8("choosedata_predict_label"))
        self.predictdata_vlayout.addWidget(self.choosedata_predict_label)


        self.choosedata_predict = make_combobox(datachoices)
        self.predictdata_vlayout.addWidget(self.choosedata_predict)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.predictdata_vlayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.predictdata_vlayout)

        self.verticalLayout_8.addWidget(self.submodel_opt)

        self.submodel_opt.setTitle(_translate("MainWindow", "Submodel - Predict", None))
        self.choosemodel_label.setText(_translate("MainWindow", "Choose reference model:", None))
        self.low_model_max_label.setText(_translate("MainWindow", "Max:", None))

        self.high_model_min_label.setText(_translate("MainWindow", "Min: ", None))
        self.add_submodel_button.setText(_translate("MainWindow", "Add Submodel", None))
        self.delete_submodel_button.setText(_translate("MainWindow", "Delete Submodel", None))
        self.optimize_checkbox.setText(_translate("MainWindow", "Optimize", None))
        self.choosedata_predict_label.setText(_translate("MainWindow", "Choose data to predict:", None))

        self.add_submodel_button.clicked.connect(lambda: self.add_submodel())
        self.delete_submodel_button.clicked.connect(lambda: self.del_submodel())
        self.choose_low_model.currentIndexChanged.connect(
            lambda: self.set_ranges(self.choose_low_model.currentText(),maxspin=self.low_model_max))
        self.choose_low_model.currentIndexChanged.connect(lambda: self.get_sm_params())
        self.choose_high_model.currentIndexChanged.connect(
            lambda: self.set_ranges(self.choose_high_model.currentText(), minspin=self.high_model_min))
        self.choose_high_model.currentIndexChanged.connect(lambda: self.get_sm_params())
        self.optimize_checkbox.toggled.connect(lambda: self.optimize_ranges(self.optimize_checkbox.isChecked(),datachoices))


    def add_submodel(self):
        submodel_hlayout = QtGui.QHBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(10)

        submodel_hlayout.setMargin(11)
        submodel_hlayout.setSpacing(6)
        submodel_hlayout.setObjectName(_fromUtf8("submodel_hlayout"))
        modelchoices = self.pysat_fun.modelkeys
        if modelchoices == []:
            error_print('No model has been trained')
            modelchoices = ['No model has been trained!']
        choose_submodel = make_combobox(modelchoices)
        submodel_hlayout.addWidget(choose_submodel)
        submodel_min_label = QtGui.QLabel()
        submodel_min_label.setObjectName(_fromUtf8("submodel_min_label"))
        submodel_min_label.setFont(font)
        submodel_hlayout.addWidget(submodel_min_label)
        submodel_min = QtGui.QDoubleSpinBox()
        submodel_min.setObjectName(_fromUtf8("submodel_min"))
        submodel_min.setFont(font)
        submodel_min.setMaximum(1000)
        submodel_min.setMinimum(-1000)
        submodel_hlayout.addWidget(submodel_min)
        submodel_max_label = QtGui.QLabel()
        submodel_max_label.setObjectName(_fromUtf8("submodel_max_label"))
        submodel_max_label.setFont(font)
        submodel_hlayout.addWidget(submodel_max_label)
        submodel_max = QtGui.QDoubleSpinBox()
        submodel_max.setObjectName(_fromUtf8("submodel_max"))
        submodel_max.setFont(font)
        submodel_max.setMaximum(1000)
        submodel_max.setMinimum(-1000)
        submodel_hlayout.addWidget(submodel_max)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        submodel_hlayout.addItem(spacerItem2)
        submodel_min_label.setText(_translate("MainWindow", "Min: ", None))
        submodel_max_label.setText(_translate("MainWindow", "Max: ", None))
        self.midmodel_vlayout.addLayout(submodel_hlayout)
        submodel_min.valueChanged.connect(lambda: self.get_sm_params())
        submodel_max.valueChanged.connect(lambda: self.get_sm_params())
        self.set_ranges(choose_submodel.currentText(), minspin=submodel_min, maxspin=submodel_max)
        choose_submodel.currentIndexChanged.connect(lambda: self.set_ranges(choose_submodel.currentText(),minspin=submodel_min,maxspin=submodel_max))
        choose_submodel.currentIndexChanged.connect(lambda: self.get_sm_params())


    def del_submodel(self):
        submodel_to_delete=self.midmodel_vlayout.takeAt(self.midmodel_vlayout.count()-1)
        if submodel_to_delete is not None:
            while submodel_to_delete.count():
                item = submodel_to_delete.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    pass


    def optimize_ranges(self,ischecked,datachoices):
        if not ischecked:
            self.choosedata_label.deleteLater()
            self.choosedata.deleteLater()

        else:
            font = QtGui.QFont()
            font.setPointSize(10)
            self.choosedata_label = QtGui.QLabel(self.submodel_opt)
            self.choosedata_label.setObjectName(_fromUtf8("choosedata_label"))
            self.choosedata_label.setText(
                _translate("MainWindow", "Choose known data to optimize submodel ranges:", None))
            self.choosedata_label.setFont(font)
            self.choosedata_hlayout.addWidget(self.choosedata_label)

            self.choosedata = make_combobox(datachoices)
            self.choosedata_hlayout.addWidget(self.choosedata)
            self.choosedata.currentIndexChanged.connect(lambda: self.get_sm_params())

    def set_ranges(self,model,minspin=None,maxspin=None):
        range=self.pysat_fun.models[model].yrange
        if minspin:
            minspin.setValue(range[0])
        if maxspin:
            maxspin.setValue(range[1])

