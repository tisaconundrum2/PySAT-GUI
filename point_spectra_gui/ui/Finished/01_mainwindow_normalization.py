


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
        self.normalization = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.normalization.setFont(font)
        self.normalization.setObjectName("normalization")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.normalization)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choosedata_layout = QtWidgets.QHBoxLayout()
        self.choosedata_layout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName("choosedata_layout")
        self.regression_choosedata_label = QtWidgets.QLabel(self.normalization)
        self.regression_choosedata_label.setObjectName("regression_choosedata_label")
        self.choosedata_layout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtWidgets.QComboBox(self.normalization)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata.addItem("")
        self.regression_choosedata.addItem("")
        self.choosedata_layout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)
        self.all_ranges_layout = QtWidgets.QVBoxLayout()
        self.all_ranges_layout.setContentsMargins(11, 11, 11, 11)
        self.all_ranges_layout.setSpacing(6)
        self.all_ranges_layout.setObjectName("all_ranges_layout")
        self.ranges_layout = QtWidgets.QHBoxLayout()
        self.ranges_layout.setContentsMargins(11, 11, 11, 11)
        self.ranges_layout.setSpacing(6)
        self.ranges_layout.setObjectName("ranges_layout")
        self.min_label = QtWidgets.QLabel(self.normalization)
        self.min_label.setObjectName("min_label")
        self.ranges_layout.addWidget(self.min_label)
        self.min_lineEdit = QtWidgets.QLineEdit(self.normalization)
        self.min_lineEdit.setObjectName("min_lineEdit")
        self.ranges_layout.addWidget(self.min_lineEdit)
        self.max_label = QtWidgets.QLabel(self.normalization)
        self.max_label.setObjectName("max_label")
        self.ranges_layout.addWidget(self.max_label)
        self.max_lineEdit = QtWidgets.QLineEdit(self.normalization)
        self.max_lineEdit.setObjectName("max_lineEdit")
        self.ranges_layout.addWidget(self.max_lineEdit)
        self.all_ranges_layout.addLayout(self.ranges_layout)
        self.verticalLayout.addLayout(self.all_ranges_layout)
        self.min_max_horizontalLayout = QtWidgets.QHBoxLayout()
        self.min_max_horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.min_max_horizontalLayout.setSpacing(6)
        self.min_max_horizontalLayout.setObjectName("min_max_horizontalLayout")
        self.add_ranges_button = QtWidgets.QPushButton(self.normalization)
        self.add_ranges_button.setObjectName("add_ranges_button")
        self.min_max_horizontalLayout.addWidget(self.add_ranges_button)
        self.add_ranges_button_2 = QtWidgets.QPushButton(self.normalization)
        self.add_ranges_button_2.setObjectName("add_ranges_button_2")
        self.min_max_horizontalLayout.addWidget(self.add_ranges_button_2)
        self.verticalLayout.addLayout(self.min_max_horizontalLayout)
        self.verticalLayout_8.addWidget(self.normalization)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.normalization.setTitle(_translate("MainWindow", "Normalization"))
        self.regression_choosedata_label.setText(_translate("MainWindow", "Choose data:"))
        self.regression_choosedata.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data"))
        self.min_label.setText(_translate("MainWindow", "Min"))
        self.max_label.setText(_translate("MainWindow", "Max"))
        self.add_ranges_button.setText(_translate("MainWindow", "Add Ranges"))
        self.add_ranges_button_2.setText(_translate("MainWindow", "delete Ranges"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



