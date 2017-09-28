


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
        self.get_mask = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.get_mask.setFont(font)
        self.get_mask.setObjectName("get_mask")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.get_mask)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_mask_label = QtWidgets.QLabel(self.get_mask)
        self.get_mask_label.setObjectName("get_mask_label")
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtWidgets.QLineEdit(self.get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName("get_mask_line_edit")
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtWidgets.QToolButton(self.get_mask)
        self.get_mask_button.setObjectName("get_mask_button")
        self.horizontalLayout.addWidget(self.get_mask_button)
        self.verticalLayout_8.addWidget(self.get_mask)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)


        self.get_mask.setTitle(_translate("MainWindow", "Mask File"))
        self.get_mask_label.setText(_translate("MainWindow", "File Name"))
        self.get_mask_line_edit.setText(_translate("MainWindow", "\n"
"                                                            *.csv\n"
"                                                        "))
        self.get_mask_button.setText(_translate("MainWindow", "..."))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



