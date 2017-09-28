


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
        self.Interpolation = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.Interpolation.setFont(font)
        self.Interpolation.setObjectName("Interpolation")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Interpolation)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choosedata_layout = QtWidgets.QHBoxLayout()
        self.choosedata_layout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName("choosedata_layout")
        self.regression_choosedata_label = QtWidgets.QLabel(self.Interpolation)
        self.regression_choosedata_label.setObjectName("regression_choosedata_label")
        self.choosedata_layout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtWidgets.QComboBox(self.Interpolation)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata.addItem("")
        self.regression_choosedata.addItem("")
        self.choosedata_layout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)
        self.choosedata_layout_2 = QtWidgets.QHBoxLayout()
        self.choosedata_layout_2.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout_2.setSpacing(6)
        self.choosedata_layout_2.setObjectName("choosedata_layout_2")
        self.regression_choosedata_label_2 = QtWidgets.QLabel(self.Interpolation)
        self.regression_choosedata_label_2.setObjectName("regression_choosedata_label_2")
        self.choosedata_layout_2.addWidget(self.regression_choosedata_label_2)
        self.regression_choosedata_2 = QtWidgets.QComboBox(self.Interpolation)
        self.regression_choosedata_2.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata_2.setObjectName("regression_choosedata_2")
        self.regression_choosedata_2.addItem("")
        self.regression_choosedata_2.addItem("")
        self.choosedata_layout_2.addWidget(self.regression_choosedata_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.choosedata_layout_2)
        self.verticalLayout_8.addWidget(self.Interpolation)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem2)


        self.Interpolation.setTitle(_translate("MainWindow", "Interpolation"))
        self.regression_choosedata_label.setText(_translate("MainWindow", "Choose data:"))
        self.regression_choosedata.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data"))
        self.regression_choosedata_label_2.setText(_translate("MainWindow", "Choose data:"))
        self.regression_choosedata_2.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.regression_choosedata_2.setItemText(1, _translate("MainWindow", "Known Data"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



