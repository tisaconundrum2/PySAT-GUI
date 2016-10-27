





    def on_maskFile_clicked(self, lineEdit):
        filename = QFileDialog.getOpenFileName(None, "Open Mask File", '.', "(*.csv)")
        lineEdit.setText(filename)
        self.pysat_fun.set_file_maskfile(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.set_mask()

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QFileDialog.getOpenFileName(None, "Open Uknown Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)

    def on_outPutLocationButton_clicked(self, lineEdit):
        filename = QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        lineEdit.setText(filename)
        self.pysat_fun.file_outpath(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*/*")

    #### Ok Button Clicked
    def on_okButton_clicked(self):
        self.pysat_fun.set_sm()
        self.pysat_fun.get_sm_fit()
        self.pysat_fun.get_plots()

    def strat_fold_change_vars(self):
        self.strat_folds_choose_var.clear()
        choices = self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        print(choices)
        self.strat_folds_choose_var.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.choose_test_fold.clear()
        choices = list(map(str, list(range(1, self.nfolds_spin.value() + 1))))
        print(choices)
        self.choose_test_fold.addItems(choices)

    def make_ransac_widget(self):
        try:
            self.ransac_widget.deleteLater()
        except:
            pass
        self.ransac_widget = QtGui.QWidget()
        if self.regression_ransac_checkbox.isChecked():
            ransac_widget_hlayout = QtGui.QHBoxLayout(self.ransac_widget)
            ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
            ransac_lossfunc_label = QtGui.QLabel(self.ransac_widget)
            ransac_lossfunc_label.setText('Loss function:')
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_label)
            ransac_lossfunc_combobox = QtGui.QComboBox(self.ransac_widget)
            ransac_lossfunc_combobox.addItem(_fromUtf8("Squared Error"))
            ransac_lossfunc_combobox.addItem(_fromUtf8("Absolute Error"))
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_combobox)
            ransac_lossfunc_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            ransac_lossfunc_hlayout.addItem(ransac_lossfunc_spacer)
            ransac_widget_hlayout.addLayout(ransac_lossfunc_hlayout)
            ransac_thresh_hlayout = QtGui.QHBoxLayout()
            ransac_thresh_label = QtGui.QLabel(self.ransac_widget)
            ransac_thresh_label.setText('Threshold:')
            ransac_thresh_hlayout.addWidget(ransac_thresh_label)
            ransac_thresh_spin = QtGui.QDoubleSpinBox(self.ransac_widget)
            ransac_thresh_hlayout.addWidget(ransac_thresh_spin)
            ransac_thresh_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            ransac_thresh_hlayout.addItem(ransac_thresh_spacer)
            ransac_widget_hlayout.addLayout(ransac_thresh_hlayout)
            self.ransac_hlayout.addWidget(self.ransac_widget)

    def make_regression_widget(self):
        alg = self.regression_choosealg.currentText()
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtGui.QWidget()
        if alg == 'Choose an algorithm':
            pass
        if alg == 'PLS':
            pls_hlayout = QtGui.QHBoxLayout(self.reg_widget)
            pls_nc_label = QtGui.QLabel(self.reg_widget)
            pls_nc_label.setText('# of components:')
            pls_hlayout.addWidget(pls_nc_label)
            pls_nc_spinbox = QtGui.QSpinBox(self.reg_widget)
            pls_hlayout.addWidget(pls_nc_spinbox)
            pls_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            pls_hlayout.addItem(pls_spacer)

        if alg == 'GP':
            gp_vlayout = QtGui.QVBoxLayout(self.reg_widget)
            gp_dim_red_hlayout = QtGui.QHBoxLayout()
            gp_dim_red_label = QtGui.QLabel(self.reg_widget)
            gp_dim_red_label.setText('Choose dimensionality reduction method:')
            gp_dim_red_hlayout.addWidget(gp_dim_red_label)
            gp_dim_red_combobox = QtGui.QComboBox(self.reg_widget)
            gp_dim_red_combobox.addItem(_fromUtf8("PCA"))
            gp_dim_red_combobox.addItem(_fromUtf8("ICA"))
            gp_dim_red_hlayout.addWidget(gp_dim_red_combobox)
            gp_vlayout.addLayout(gp_dim_red_hlayout)
            gp_rand_starts_hlayout = QtGui.QHBoxLayout()
            gp_rand_starts_label = QtGui.QLabel(self.reg_widget)
            gp_rand_starts_label.setText('# of random starts:')
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_label)
            gp_rand_starts_spin = QtGui.QSpinBox(self.reg_widget)
            gp_rand_starts_spin.setValue(1)
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_spin)
            spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_rand_starts_hlayout.addItem(spacerItem4)
            gp_vlayout.addLayout(gp_rand_starts_hlayout)
            gp_theta_vlayout = QtGui.QVBoxLayout()
            gp_theta0_label = QtGui.QLabel(self.reg_widget)
            gp_theta0_label.setText('Starting Theta:')
            gp_theta_vlayout.addWidget(gp_theta0_label)
            gp_theta0_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_theta0_spin.setValue(1.0)
            gp_theta_vlayout.addWidget(gp_theta0_spin)
            gp_thetaL_label = QtGui.QLabel(self.reg_widget)
            gp_thetaL_label.setText('Lower bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaL_label)
            gp_thetaL_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaL_spin.setValue(0.1)
            gp_theta_vlayout.addWidget(gp_thetaL_spin)
            gp_thetaU_label = QtGui.QLabel(self.reg_widget)
            gp_thetaU_label.setText('Upper bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaU_label)
            gp_thetaU_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaU_spin.setMaximum(10000)
            gp_thetaU_spin.setValue(100.0)

            gp_theta_vlayout.addWidget(gp_thetaU_spin)
            spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_theta_vlayout.addItem(spacerItem5)
            gp_vlayout.addLayout(gp_theta_vlayout)

        self.regression_vlayout.addWidget(self.reg_widget)





<< << << < HEAD
return listwidget
== == == =
return listwidget
>> >> >> > 18
fa50f900de0cff5a4d52115c9310b4d63de617



    def stratified_folds(self, MainWindow):
        self.strat_folds = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.strat_folds.setFont(font)
        self.strat_folds.setObjectName(_fromUtf8("Stratified Folds"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout(self.strat_folds)
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_data_label.setObjectName(_fromUtf8("strat_folds_choose_data_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data_label)
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            datachoices = ['No data has been loaded!']
        self.strat_folds_choose_data = make_combobox(datachoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_var_label = QtGui.QLabel(self.strat_folds)
        self.strat_folds_choose_var_label.setObjectName(_fromUtf8("strat_folds_choose_var_label"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var_label)

        varchoices = self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        self.strat_folds_choose_var = make_combobox(varchoices)
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_var)
        self.strat_folds_choose_data.activated[int].connect(self.strat_fold_change_vars)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(self.strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(self.strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.nfolds_spin.setMinimum(1)
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(self.strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        foldchoices = ['1']
        self.choose_test_fold = make_combobox(foldchoices)
        self.choose_test_fold.setObjectName(_fromUtf8("choose_test_fold"))
        self.nfolds_spin.valueChanged.connect(self.strat_fold_change_testfolds)
        self.strat_folds_hlayout.addWidget(self.choose_test_fold)
        self.spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(self.spacerItem)
        self.create_folds = QtGui.QPushButton(self.strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout_8.addWidget(self.strat_folds)
        self.strat_folds.raise_()
        self.strat_folds.setTitle(_translate("MainWindow", "Stratified Folds", None))
        self.nfolds_label.setText(_translate("strat_folds", "N folds", None))
        self.test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))
        self.strat_folds_choose_data_label.setText(_translate("strat_folds", "Choose data to stratify:", None))
        self.strat_folds_choose_var_label.setText(
            _translate("strat_folds", "Choose variable on which to sort:", None))
        try:
            self.create_folds.clicked.connect(
                lambda: self.pysat_fun.do_strat_folds(datakey=str(self.strat_folds_choose_data.currentText()),
                                                      nfolds=int(self.nfolds_spin.text()),
                                                      testfold=int(self.choose_test_fold.currentText()),
                                                      colname=('comp', self.strat_folds_choose_var.currentText())))
        except:
            print('There was a problem with creating stratified folds...')


            ####These functions below are private and add functionality to the UI

    def submodel(self, MainWindow):
        pass

    def masked(self, MainWindow):
        self.masked = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.masked.setFont(font)
        self.masked.setObjectName(_fromUtf8("masked"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.masked)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setMargin(11)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setMargin(11)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.label_9 = QtGui.QLabel(self.masked)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_17.addWidget(self.label_9)
        self.horizontalLayout_13.addLayout(self.verticalLayout_17)
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setMargin(11)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.lineEdit_10 = QtGui.QLineEdit(self.masked)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.verticalLayout_22.addWidget(self.lineEdit_10)
        self.horizontalLayout_13.addLayout(self.verticalLayout_22)
        self.verticalLayout_24 = QtGui.QVBoxLayout()
        self.verticalLayout_24.setMargin(11)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.fullDataBaseButton_4 = QtGui.QToolButton(self.masked)
        self.fullDataBaseButton_4.setObjectName(_fromUtf8("fullDataBaseButton_4"))
        self.verticalLayout_24.addWidget(self.fullDataBaseButton_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_24)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.label_16 = QtGui.QLabel(self.masked)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout.addWidget(self.label_16)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_8.addWidget(self.masked)
        self.masked.setTitle(_translate("MainWindow", "Mask", None))
        self.label_9.setText(_translate("MainWindow", "Maskfile", None))
        self.lineEdit_10.setText(_translate("MainWindow", "*.csv", None))
        self.fullDataBaseButton_4.setText(_translate("MainWindow", "...", None))
        self.label_16.setText(_translate("MainWindow", "Mask was applied to unknown and known data", None))
        try:
            self.fullDataBaseButton_4.clicked.connect(lambda: pysat_ui.on_maskFile_clicked(self, self.lineEdit_10))
        except:
            pass

    """ =============================================
    Please do not delete the files below this line!
    These files are the working files that allow the UI
    to operate and do things!
    ============================================== """

    def set_module_button(self, QVBoxLayout, PushButtonName):
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        PushButtonName.setObjectName(_fromUtf8("run_module_files"))
        self.horizontalLayout.addWidget(PushButtonName)
        QVBoxLayout.addLayout(self.horizontalLayout)
        PushButtonName.setText(_translate("MainWindow", "Run Module", None))

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")

    def menu_item_functions(self, MainWindow):
        self.actionSet_output_location.triggered.connect(lambda: pysat_ui.file_outpath(self, MainWindow))
        self.actionLoad_Unknown_Data.triggered.connect(lambda: pysat_ui.unknown_data(self, MainWindow))
        self.actionLoad_reference_Data.triggered.connect(lambda: pysat_ui.reference_data(self, MainWindow))
        self.actionNormalization.triggered.connect(lambda: pysat_ui.normalization(self, MainWindow))
        self.actionInterpolate.triggered.connect(lambda: pysat_ui.interpolated(self, MainWindow))
        self.actionApply_Mask.triggered.connect(lambda: pysat_ui.masked(self, MainWindow))
        self.actionStratified_Folds.triggered.connect(lambda: pysat_ui.stratified_folds(self, MainWindow))
        self.actionTrain.triggered.connect(lambda: pysat_ui.regression_train(self, MainWindow))

    def saveworkflow(self):
        # TODO save the current window's data into a save file
        pass

    def openworkflow(self):
        # TODO open file dialog
        self.filename = QFileDialog.getOpenFileName(self, "Open a Workflow File", '.', "(*.wrf)")

    def on_maskFile_clicked(self, lineEdit):
        filename = QFileDialog.getOpenFileName(None, "Open Mask File", '.', "(*.csv)")
        lineEdit.setText(filename)
        self.pysat_fun.set_file_maskfile(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.set_mask()

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QFileDialog.getOpenFileName(None, "Open Uknown Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)

    def on_okButton_clicked(self):
        self.pysat_fun.set_sm()
        self.pysat_fun.get_sm_fit()
        self.pysat_fun.get_plots()


