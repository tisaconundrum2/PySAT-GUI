


        self.scrollAreaWidgetContents_2.setStyleSheet("QGroupBox {\n"
"                                    border: 2px solid gray;\n"
"                                    border-radius: 6px;\n"
"                                    margin-top: 0.5em;\n"
"                                    }\n"
"\n"
"                                    QGroupBox::title {\n"
"\n"
"                                    padding-top: -14px;\n"
"                                    padding-left: 8px;\n"
"                                    }\n"
        self.strat_folds = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.strat_folds.setFont(font)
        self.strat_folds.setObjectName("strat_folds")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.strat_folds)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.strat_folds_vlayout = QtWidgets.QVBoxLayout()
        self.strat_folds_vlayout.setContentsMargins(11, 11, 11, 11)
        self.strat_folds_vlayout.setSpacing(6)
        self.strat_folds_vlayout.setObjectName("strat_folds_vlayout")
        self.strat_folds_choose_data = QtWidgets.QComboBox(self.strat_folds)
        self.strat_folds_choose_data.setObjectName("strat_folds_choose_data")
        self.strat_folds_choose_data.addItem("")
        self.strat_folds_choose_data.addItem("")
        self.strat_folds_choose_data.addItem("")
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_element = QtWidgets.QComboBox(self.strat_folds)
        self.strat_folds_choose_element.setObjectName("strat_folds_choose_element")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_choose_element.addItem("")
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_element)
        self.strat_folds_hlayout = QtWidgets.QHBoxLayout()
        self.strat_folds_hlayout.setContentsMargins(11, 11, 11, 11)
        self.strat_folds_hlayout.setSpacing(6)
        self.strat_folds_hlayout.setObjectName("strat_folds_hlayout")
        self.nfolds_label = QtWidgets.QLabel(self.strat_folds)
        self.nfolds_label.setObjectName("nfolds_label")
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtWidgets.QSpinBox(self.strat_folds)
        self.nfolds_spin.setObjectName("nfolds_spin")
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtWidgets.QLabel(self.strat_folds)
        self.test_fold_label.setObjectName("test_fold_label")
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_spin = QtWidgets.QSpinBox(self.strat_folds)
        self.test_fold_spin.setObjectName("test_fold_spin")
        self.strat_folds_hlayout.addWidget(self.test_fold_spin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(spacerItem)
        self.create_folds = QtWidgets.QPushButton(self.strat_folds)
        self.create_folds.setObjectName("create_folds")
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout.addLayout(self.strat_folds_vlayout)
        self.verticalLayout_8.addWidget(self.strat_folds)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.strat_folds.setTitle(_translate("MainWindow", "Stratified Folds"))
        self.strat_folds_choose_data.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.strat_folds_choose_data.setItemText(1, _translate("MainWindow", "Unknown Data"))
        self.strat_folds_choose_data.setItemText(2, _translate("MainWindow", "Known Data"))
        self.strat_folds_choose_element.setItemText(0, _translate("MainWindow", "Choose Element to Stratify On"))
        self.strat_folds_choose_element.setItemText(1, _translate("MainWindow", "SiO2"))
        self.strat_folds_choose_element.setItemText(2, _translate("MainWindow", "TiO2"))
        self.strat_folds_choose_element.setItemText(3, _translate("MainWindow", "Al2O3"))
        self.strat_folds_choose_element.setItemText(4, _translate("MainWindow", "FeOT"))
        self.strat_folds_choose_element.setItemText(5, _translate("MainWindow", "MgO"))
        self.strat_folds_choose_element.setItemText(6, _translate("MainWindow", "CaO"))
        self.strat_folds_choose_element.setItemText(7, _translate("MainWindow", "Na2O"))
        self.strat_folds_choose_element.setItemText(8, _translate("MainWindow", "K2O"))
        self.nfolds_label.setText(_translate("MainWindow", "N folds"))
        self.test_fold_label.setText(_translate("MainWindow", "Test Fold"))
        self.create_folds.setText(_translate("MainWindow", "Create Folds"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



