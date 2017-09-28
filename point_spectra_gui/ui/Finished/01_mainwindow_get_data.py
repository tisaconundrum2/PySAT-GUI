


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
        self.get_data = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.get_data.setFont(font)
        self.get_data.setObjectName("get_data")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_data)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_data_label = QtWidgets.QLabel(self.get_data)
        self.get_data_label.setObjectName("get_data_label")
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtWidgets.QLineEdit(self.get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName("get_data_line_edit")
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtWidgets.QToolButton(self.get_data)
        self.get_data_button.setObjectName("get_data_button")
        self.horizontalLayout.addWidget(self.get_data_button)
        self.verticalLayout_8.addWidget(self.get_data)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)


        self.get_data.setTitle(_translate("MainWindow", "Load in <known> data file"))
        self.get_data_label.setText(_translate("MainWindow", "File Name"))
        self.get_data_line_edit.setText(_translate("MainWindow", "\n"
"                                                            *.csv\n"
"                                                        "))
        self.get_data_button.setText(_translate("MainWindow", "..."))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



