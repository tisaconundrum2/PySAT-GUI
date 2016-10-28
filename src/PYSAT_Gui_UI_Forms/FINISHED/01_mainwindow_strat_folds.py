




        self.scrollAreaWidgetContents_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
"  border: 2px solid gray;\n"
"  border-radius: 6px;\n"
"  margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"  padding-top: -14px;\n"
"  padding-left: 8px;\n"
"}\n"
        self.strat_folds = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.strat_folds.setFont(font)
        self.strat_folds.setObjectName(_fromUtf8("strat_folds"))
        self.verticalLayout = QtGui.QVBoxLayout(self.strat_folds)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout()
        self.strat_folds_vlayout.setMargin(11)
        self.strat_folds_vlayout.setSpacing(6)
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data = QtGui.QComboBox(self.strat_folds)
        self.strat_folds_choose_data.setObjectName(_fromUtf8("strat_folds_choose_data"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_element = QtGui.QComboBox(self.strat_folds)
        self.strat_folds_choose_element.setObjectName(_fromUtf8("strat_folds_choose_element"))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_element)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setMargin(11)
        self.strat_folds_hlayout.setSpacing(6)
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(self.strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(self.strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(self.strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_spin = QtGui.QSpinBox(self.strat_folds)
        self.test_fold_spin.setObjectName(_fromUtf8("test_fold_spin"))
        self.strat_folds_hlayout.addWidget(self.test_fold_spin)
        self.strat_folds_hlayout.addItem(spacerItem)
        self.create_folds = QtGui.QPushButton(self.strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout.addLayout(self.strat_folds_vlayout)
        self.verticalLayout_8.addWidget(self.strat_folds)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.strat_folds.setTitle(_translate("MainWindow", "Stratified Folds", None))
        self.strat_folds_choose_data.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.strat_folds_choose_data.setItemText(1, _translate("MainWindow", "Unknown Data", None))
        self.strat_folds_choose_data.setItemText(2, _translate("MainWindow", "Known Data", None))
        self.strat_folds_choose_element.setItemText(0, _translate("MainWindow", "Choose Element to Stratify On", None))
        self.strat_folds_choose_element.setItemText(1, _translate("MainWindow", "SiO2", None))
        self.strat_folds_choose_element.setItemText(2, _translate("MainWindow", "TiO2", None))
        self.strat_folds_choose_element.setItemText(3, _translate("MainWindow", "Al2O3", None))
        self.strat_folds_choose_element.setItemText(4, _translate("MainWindow", "FeOT", None))
        self.strat_folds_choose_element.setItemText(5, _translate("MainWindow", "MgO", None))
        self.strat_folds_choose_element.setItemText(6, _translate("MainWindow", "CaO", None))
        self.strat_folds_choose_element.setItemText(7, _translate("MainWindow", "Na2O", None))
        self.strat_folds_choose_element.setItemText(8, _translate("MainWindow", "K2O", None))
        self.nfolds_label.setText(_translate("MainWindow", "N folds", None))
        self.test_fold_label.setText(_translate("MainWindow", "Test Fold", None))
        self.create_folds.setText(_translate("MainWindow", "Create Folds", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

