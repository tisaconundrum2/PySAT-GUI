




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
        self.get_data = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        font = QtGui.QFont()
        self.get_data.setFont(font)
        self.get_data.setObjectName(_fromUtf8("get_data"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.get_data)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_data_label = QtGui.QLabel(self.get_data)
        self.get_data_label.setObjectName(_fromUtf8("get_data_label"))
        self.horizontalLayout.addWidget(self.get_data_label)
        self.get_data_line_edit = QtGui.QLineEdit(self.get_data)
        self.get_data_line_edit.setReadOnly(True)
        self.get_data_line_edit.setObjectName(_fromUtf8("get_data_line_edit"))
        self.horizontalLayout.addWidget(self.get_data_line_edit)
        self.get_data_button = QtGui.QToolButton(self.get_data)
        self.get_data_button.setObjectName(_fromUtf8("get_data_button"))
        self.horizontalLayout.addWidget(self.get_data_button)
        self.verticalLayout_8.addWidget(self.get_data)


        self.get_data.setTitle(_translate("MainWindow", "Files", None))
        self.get_data_label.setText(_translate("MainWindow", "File Name", None))
        self.get_data_line_edit.setText(_translate("MainWindow", "*.csv", None))
        self.get_data_button.setText(_translate("MainWindow", "...", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

