


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
        self.file_out_path = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.file_out_path.setFont(font)
        self.file_out_path.setObjectName("file_out_path")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.file_out_path)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_out_path_label = QtWidgets.QLabel(self.file_out_path)
        self.file_out_path_label.setObjectName("file_out_path_label")
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtWidgets.QLineEdit(self.file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName("file_out_path_line_edit")
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtWidgets.QToolButton(self.file_out_path)
        self.file_out_path_button.setObjectName("file_out_path_button")
        self.horizontalLayout.addWidget(self.file_out_path_button)
        self.verticalLayout_8.addWidget(self.file_out_path)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)


        self.file_out_path.setTitle(_translate("MainWindow", "Ouput Folder"))
        self.file_out_path_label.setText(_translate("MainWindow", "Folder Name"))
        self.file_out_path_line_edit.setText(_translate("MainWindow", "\n"
"                                                            */\n"
"                                                        "))
        self.file_out_path_button.setText(_translate("MainWindow", "..."))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



