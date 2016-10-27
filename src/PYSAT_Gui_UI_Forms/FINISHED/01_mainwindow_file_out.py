




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
        self.file_out_path = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.file_out_path.setFont(font)
        self.file_out_path.setObjectName(_fromUtf8("file_out_path"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.file_out_path)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_out_path_label = QtGui.QLabel(self.file_out_path)
        self.file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtGui.QLineEdit(self.file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtGui.QToolButton(self.file_out_path)
        self.file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
        self.horizontalLayout.addWidget(self.file_out_path_button)
        self.verticalLayout_8.addWidget(self.file_out_path)


        self.file_out_path.setTitle(_translate("MainWindow", "Ouput Folder", None))
        self.file_out_path_label.setText(_translate("MainWindow", "Folder Name", None))
        self.file_out_path_line_edit.setText(_translate("MainWindow", "*/", None))
        self.file_out_path_button.setText(_translate("MainWindow", "...", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

