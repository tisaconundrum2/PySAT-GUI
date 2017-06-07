from PyQt5 import QtGui, QtCore, QtWidgets
from point_spectra_gui.gui_utils import make_combobox
from point_spectra_gui.ui_modules.Error_ import error_print


class sm_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.submodel_gui_info = []
        self.new_submodel_index = 1
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_id = None
        self.module_layout = module_layout

        self.main()

    def main(self):
        # driver function, calls UI and set's up connections
        # add function list calls here
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.sm_ui()
        self.set_sm_params()
        self.get_sm_params()
        self.pysat_fun.set_greyed_modules(self.submodel_predict)  # set the module grey after use.

    def get_sm_params(self):
        ui_list = "do_submodel_predict"
        fun_list = "do_submodel_predict"
        blendranges = []
        submodel_names = []
        kws = {}

        try:
            datakey = self.choosedata_predict.currentText()
        except:
            datakey = None

        for i in self.submodel_gui_info:
            try:
                min_temp = i[1][0].value()
            except:
                min_temp = i[1][0]

            try:
                max_temp = i[1][1].value()
            except:
                max_temp = i[1][1]

            blendranges.append([min_temp, max_temp])
            submodel_names.append(i[0].currentText())

        try:
            trueval_data = self.choosedata.currentText()
        except:
            trueval_data = None

        args = [datakey, submodel_names, blendranges, trueval_data]
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.ui_id)

    def set_sm_params(self):
        datakey = self.arg_list[0]
        submodel_names = self.arg_list[1]
        blendranges = self.arg_list[2]
        trueval_data = self.arg_list[3]
        self.choosedata_predict.currentIndex(self.choosedata_predict.findText(str(datakey)))

    def sm_ui(self):

        self.submodel_predict = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submodel_predict.setFont(font)
        self.submodel_predict.setObjectName(("submodel_predict"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.submodel_predict)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))

        # choose reference/full model
        self.choosemodel_hlayout = QtWidgets.QHBoxLayout()
        self.choosemodel_hlayout.setContentsMargins(11, 11, 11, 11)
        self.choosemodel_hlayout.setSpacing(6)
        self.choosemodel_hlayout.setObjectName(("choosemodel_hlayout"))
        self.choosemodel_label = QtWidgets.QLabel(self.submodel_predict)
        self.choosemodel_label.setObjectName(("choosemodel_label"))
        self.choosemodel_hlayout.addWidget(self.choosemodel_label)
        modelchoices = self.pysat_fun.modelkeys
        if modelchoices == []:
            error_print('No model has been trained')
            modelchoices = ['No model has been trained!']
        self.choosemodel = make_combobox(modelchoices)

        self.choosemodel_hlayout.addWidget(self.choosemodel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosemodel_hlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosemodel_hlayout)

        # organize submodels vertically
        self.submodels_vlayout = QtWidgets.QVBoxLayout()
        self.submodels_vlayout.setContentsMargins(11, 11, 11, 11)
        self.submodels_vlayout.setSpacing(6)
        self.submodels_vlayout.setObjectName(("submodels_vlayout"))

        # always have a low submodel
        self.low_model_hlayout = QtWidgets.QHBoxLayout()
        self.low_model_hlayout.setContentsMargins(11, 11, 11, 11)
        self.low_model_hlayout.setSpacing(6)
        self.low_model_hlayout.setObjectName(("low_model_hlayout"))
        self.low_model_label = QtWidgets.QLabel(self.submodel_predict)
        self.low_model_label.setText('Low Model:')
        self.low_model_hlayout.addWidget(self.low_model_label)
        self.choose_low_model = make_combobox(modelchoices)
        self.low_model_hlayout.addWidget(self.choose_low_model)
        self.low_model_max_label = QtWidgets.QLabel(self.submodel_predict)
        self.low_model_max_label.setObjectName(("low_model_max_label"))
        self.low_model_hlayout.addWidget(self.low_model_max_label)
        self.low_model_max = QtWidgets.QDoubleSpinBox(self.submodel_predict)
        self.low_model_max.setObjectName(("low_model_max"))
        self.low_model_max.setMaximum(1000)
        self.low_model_max.setMinimum(-1000)
        self.low_model_hlayout.addWidget(self.low_model_max)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.low_model_hlayout.addItem(spacerItem1)
        self.submodels_vlayout.addLayout(self.low_model_hlayout)

        # middle submodels go here
        self.midmodel_vlayout = QtWidgets.QVBoxLayout()
        self.submodels_vlayout.addLayout(self.midmodel_vlayout)

        # always have a high submodel
        self.high_model_hlayout = QtWidgets.QHBoxLayout()
        self.high_model_hlayout.setContentsMargins(11, 11, 11, 11)
        self.high_model_hlayout.setSpacing(6)
        self.high_model_hlayout.setObjectName(("high_model_hlayout"))
        self.high_model_label = QtWidgets.QLabel(self.submodel_predict)
        self.high_model_label.setText('High Model:')
        self.high_model_hlayout.addWidget(self.high_model_label)
        self.choose_high_model = make_combobox(modelchoices)
        self.high_model_hlayout.addWidget(self.choose_high_model)
        self.high_model_min_label = QtWidgets.QLabel(self.submodel_predict)
        self.high_model_min_label.setObjectName(("high_model_min_label"))
        self.high_model_hlayout.addWidget(self.high_model_min_label)
        self.high_model_min = QtWidgets.QDoubleSpinBox(self.submodel_predict)
        self.high_model_min.setObjectName(("high_model_min"))
        self.high_model_min.setMaximum(1000)
        self.high_model_min.setMinimum(-1000)
        self.high_model_hlayout.addWidget(self.high_model_min)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.high_model_hlayout.addItem(spacerItem3)
        self.submodels_vlayout.addLayout(self.high_model_hlayout)
        self.verticalLayout.addLayout(self.submodels_vlayout)

        # set the spinbox ranges based on the models
        self.set_ranges(self.choose_high_model.currentText(), minspin=self.high_model_min)
        self.set_ranges(self.choose_low_model.currentText(), maxspin=self.low_model_max)

        # add or delete submodel buttons
        self.add_delete_hlayout = QtWidgets.QHBoxLayout()
        self.add_delete_hlayout.setContentsMargins(11, 11, 11, 11)
        self.add_delete_hlayout.setSpacing(6)
        self.add_delete_hlayout.setObjectName(("add_delete_hlayout"))
        self.add_submodel_button = QtWidgets.QPushButton(self.submodel_predict)
        self.add_submodel_button.setObjectName(("add_submodel_button"))
        self.add_delete_hlayout.addWidget(self.add_submodel_button)
        self.delete_submodel_button = QtWidgets.QPushButton(self.submodel_predict)
        self.delete_submodel_button.setObjectName(("delete_submodel_button"))
        self.add_delete_hlayout.addWidget(self.delete_submodel_button)
        self.optimize_checkbox = QtWidgets.QCheckBox(self.submodel_predict)
        self.optimize_checkbox.setObjectName(("optimize_checkbox"))
        self.add_delete_hlayout.addWidget(self.optimize_checkbox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_delete_hlayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.add_delete_hlayout)

        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']

        # choose data to optimize blending
        self.choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_hlayout.setSpacing(6)
        self.choosedata_hlayout.setObjectName(("choosedata_hlayout"))
        self.verticalLayout.addLayout(self.choosedata_hlayout)

        # choose data to predict
        self.predictdata_vlayout = QtWidgets.QVBoxLayout()
        self.predictdata_vlayout.setContentsMargins(11, 11, 11, 11)
        self.predictdata_vlayout.setSpacing(6)
        self.predictdata_vlayout.setObjectName(("predictdata_vlayout"))
        self.choosedata_predict_label = QtWidgets.QLabel(self.submodel_predict)
        self.choosedata_predict_label.setObjectName(("choosedata_predict_label"))
        self.predictdata_vlayout.addWidget(self.choosedata_predict_label)
        self.choosedata_predict = make_combobox(datachoices)
        self.predictdata_vlayout.addWidget(self.choosedata_predict)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.predictdata_vlayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.predictdata_vlayout)

        self.module_layout.addWidget(self.submodel_predict)

        # put submodel objects in a list
        self.submodel_gui_info = [[self.choose_low_model, [-9999, self.low_model_max]],
                                  [self.choose_high_model, [self.high_model_min, 9999]],
                                  [self.choosemodel, [-9999, 9999]]]

        self.submodel_predict.setTitle("Submodel - Predict")
        self.choosemodel_label.setText("Choose reference model:")
        self.low_model_max_label.setText("Max:")
        self.high_model_min_label.setText("Min: ")
        self.add_submodel_button.setText("Add Submodel")
        self.delete_submodel_button.setText("Delete Submodel")
        self.optimize_checkbox.setText("Optimize")
        self.choosedata_predict_label.setText("Choose data to predict:")

        # connect the add and delete submodel buttons and opt checkbox
        self.add_submodel_button.clicked.connect(lambda: self.add_submodel())
        self.delete_submodel_button.clicked.connect(lambda: self.del_submodel())
        self.optimize_checkbox.toggled.connect(
            lambda: self.optimize_ranges(self.optimize_checkbox.isChecked(), datachoices))

        # connect the low and high models so spinbox ranges are updated
        self.choose_low_model.currentIndexChanged.connect(
            lambda: self.set_ranges(self.choose_low_model.currentText(), maxspin=self.low_model_max))
        self.choose_high_model.currentIndexChanged.connect(
            lambda: self.set_ranges(self.choose_high_model.currentText(), minspin=self.high_model_min))

        # connect everything so that parameters get updated when changed
        self.choosemodel.currentIndexChanged.connect(lambda: self.get_sm_params())
        self.high_model_min.valueChanged.connect(lambda: self.get_sm_params())
        self.low_model_max.valueChanged.connect(lambda: self.get_sm_params())
        self.choose_low_model.currentIndexChanged.connect(lambda: self.get_sm_params())
        self.choose_high_model.currentIndexChanged.connect(lambda: self.get_sm_params())

        self.get_sm_params()  # get initial parameters

    def add_submodel(self):

        submodel_hlayout = QtWidgets.QHBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(10)

        submodel_hlayout.setContentsMargins(11, 11, 11, 11)
        submodel_hlayout.setSpacing(6)
        submodel_hlayout.setObjectName(("submodel_hlayout"))
        modelchoices = self.pysat_fun.modelkeys
        if modelchoices == []:
            error_print('No model has been trained')
            modelchoices = ['No model has been trained!']
        choose_submodel = make_combobox(modelchoices)
        submodel_hlayout.addWidget(choose_submodel)
        submodel_min_label = QtWidgets.QLabel()
        submodel_min_label.setObjectName(("submodel_min_label"))
        submodel_min_label.setFont(font)
        submodel_hlayout.addWidget(submodel_min_label)
        submodel_min = QtWidgets.QDoubleSpinBox()
        submodel_min.setObjectName(("submodel_min"))
        submodel_min.setFont(font)
        submodel_min.setMaximum(1000)
        submodel_min.setMinimum(-1000)
        submodel_hlayout.addWidget(submodel_min)
        submodel_max_label = QtWidgets.QLabel()
        submodel_max_label.setObjectName(("submodel_max_label"))
        submodel_max_label.setFont(font)
        submodel_hlayout.addWidget(submodel_max_label)
        submodel_max = QtWidgets.QDoubleSpinBox()
        submodel_max.setObjectName(("submodel_max"))
        submodel_max.setFont(font)
        submodel_max.setMaximum(1000)
        submodel_max.setMinimum(-1000)
        submodel_hlayout.addWidget(submodel_max)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        submodel_hlayout.addItem(spacerItem2)

        submodel_min_label.setText("Min: ")
        submodel_max_label.setText("Max: ")
        self.midmodel_vlayout.addLayout(submodel_hlayout)

        # insert the new submodel objects into the list
        self.submodel_gui_info.insert(-1, [choose_submodel, [submodel_min, submodel_max]])

        # connect dropdown so spinbox ranges are updated
        choose_submodel.currentIndexChanged.connect(
            lambda: self.set_ranges(choose_submodel.currentText(), minspin=submodel_min, maxspin=submodel_max))
        # connect so parameters are updated when things are changed
        choose_submodel.currentIndexChanged.connect(lambda: self.get_sm_params())
        submodel_min.valueChanged.connect(lambda: self.get_sm_params())
        submodel_max.valueChanged.connect(lambda: self.get_sm_params())
        # update parameters when submodel is first added
        self.set_ranges(choose_submodel.currentText(), minspin=submodel_min, maxspin=submodel_max)
        self.get_sm_params()

    def del_submodel(self):
        submodel_to_delete = self.midmodel_vlayout.takeAt(self.midmodel_vlayout.count() - 1)
        if submodel_to_delete is not None:
            while submodel_to_delete.count():
                item = submodel_to_delete.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

                else:
                    pass
        del self.submodel_gui_info[-2]

        self.get_sm_params()

    def optimize_ranges(self, ischecked, datachoices):
        if not ischecked:
            self.choosedata_label.deleteLater()
            self.choosedata.deleteLater()

        else:
            font = QtGui.QFont()
            font.setPointSize(10)
            self.choosedata_label = QtWidgets.QLabel(self.submodel_predict)
            self.choosedata_label.setObjectName(("choosedata_label"))
            self.choosedata_label.setText(
                "Choose known data to optimize submodel ranges:")
            self.choosedata_label.setFont(font)
            self.choosedata_hlayout.addWidget(self.choosedata_label)

            self.choosedata = make_combobox(datachoices)
            self.choosedata_hlayout.addWidget(self.choosedata)
            self.choosedata.currentIndexChanged.connect(lambda: self.get_sm_params())

        self.get_sm_params()

    def set_ranges(self, model, minspin=None, maxspin=None):
        try:
            range = self.pysat_fun.models[model].yrange
            if minspin:
                minspin.setValue(range[0])
            if maxspin:
                maxspin.setValue(range[1])
        except:
            pass
