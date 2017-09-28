


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
        self.removenull = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.removenull.setFont(font)
        self.removenull.setObjectName("removenull")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.removenull)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.removenull_vlayout = QtWidgets.QVBoxLayout()
        self.removenull_vlayout.setContentsMargins(11, 11, 11, 11)
        self.removenull_vlayout.setSpacing(6)
        self.removenull_vlayout.setObjectName("removenull_vlayout")
        self.removenull_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.removenull_choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.removenull_choosedata_hlayout.setSpacing(6)
        self.removenull_choosedata_hlayout.setObjectName("removenull_choosedata_hlayout")
        self.removenull_choosedata_label = QtWidgets.QLabel(self.removenull)
        self.removenull_choosedata_label.setObjectName("removenull_choosedata_label")
        self.removenull_choosedata_hlayout.addWidget(self.removenull_choosedata_label)
        self.removenull_choosedata = QtWidgets.QComboBox(self.removenull)
        self.removenull_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.removenull_choosedata.setObjectName("removenull_choosedata")
        self.removenull_choosedata.addItem("")
        self.removenull_choosedata.addItem("")
        self.removenull_choosedata_hlayout.addWidget(self.removenull_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.removenull_choosedata_hlayout.addItem(spacerItem)
        self.removenull_vlayout.addLayout(self.removenull_choosedata_hlayout)
        self.removenull_widget = QtWidgets.QWidget(self.removenull)
        self.removenull_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.removenull_widget.setObjectName("removenull_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.removenull_widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_of_sentence = QtWidgets.QLabel(self.removenull_widget)
        self.start_of_sentence.setObjectName("start_of_sentence")
        self.horizontalLayout_2.addWidget(self.start_of_sentence)
        self.rowcol_comboBox = QtWidgets.QComboBox(self.removenull_widget)
        self.rowcol_comboBox.setObjectName("rowcol_comboBox")
        self.rowcol_comboBox.addItem("")
        self.rowcol_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.rowcol_comboBox)
        self.middle_of_sentence = QtWidgets.QLabel(self.removenull_widget)
        self.middle_of_sentence.setObjectName("middle_of_sentence")
        self.horizontalLayout_2.addWidget(self.middle_of_sentence)
        self.removenull_spinbox = QtWidgets.QSpinBox(self.removenull_widget)
        self.removenull_spinbox.setObjectName("removenull_spinbox")
        self.horizontalLayout_2.addWidget(self.removenull_spinbox)
        self.end_of_sentence = QtWidgets.QLabel(self.removenull_widget)
        self.end_of_sentence.setObjectName("end_of_sentence")
        self.horizontalLayout_2.addWidget(self.end_of_sentence)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.removenull_vlayout.addWidget(self.removenull_widget)
        self.verticalLayout.addLayout(self.removenull_vlayout)
        self.verticalLayout_8.addWidget(self.removenull)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem2)


        self.removenull.setTitle(_translate("MainWindow", "Remove Null"))
        self.removenull_choosedata_label.setText(_translate("MainWindow", "Choose data:"))
        self.removenull_choosedata.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.removenull_choosedata.setItemText(1, _translate("MainWindow", "Known Data"))
        self.start_of_sentence.setText(_translate("MainWindow", "Each"))
        self.rowcol_comboBox.setItemText(0, _translate("MainWindow", "Row"))
        self.rowcol_comboBox.setItemText(1, _translate("MainWindow", "Column"))
        self.middle_of_sentence.setText(_translate("MainWindow", "must have at least"))
        self.end_of_sentence.setText(_translate("MainWindow", "null values to be removed."))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



