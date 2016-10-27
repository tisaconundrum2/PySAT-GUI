




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
        self.unknown_data = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.unknown_data.setFont(font)
        self.unknown_data.setObjectName(_fromUtf8("unknown_data"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.unknown_data)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unknown_data_label = QtGui.QLabel(self.unknown_data)
        self.unknown_data_label.setObjectName(_fromUtf8("unknown_data_label"))
        self.horizontalLayout.addWidget(self.unknown_data_label)
        self.unknown_data_line_edit = QtGui.QLineEdit(self.unknown_data)
        self.unknown_data_line_edit.setReadOnly(True)
        self.unknown_data_line_edit.setObjectName(_fromUtf8("unknown_data_line_edit"))
        self.horizontalLayout.addWidget(self.unknown_data_line_edit)
        self.unknown_data_button = QtGui.QToolButton(self.unknown_data)
        self.unknown_data_button.setObjectName(_fromUtf8("unknown_data_button"))
        self.horizontalLayout.addWidget(self.unknown_data_button)
        self.verticalLayout_8.addWidget(self.unknown_data)


        self.unknown_data.setTitle(_translate("MainWindow", "Files", None))
        self.unknown_data_label.setText(_translate("MainWindow", "File Name", None))
        self.unknown_data_line_edit.setText(_translate("MainWindow", "*.csv", None))
        self.unknown_data_button.setText(_translate("MainWindow", "...", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

