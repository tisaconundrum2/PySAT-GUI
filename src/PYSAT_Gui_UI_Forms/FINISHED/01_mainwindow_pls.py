




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
        self.pls = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.pls.setFont(font)
        self.pls.setObjectName(_fromUtf8("pls"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.pls)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pls_label = QtGui.QLabel(self.pls)
        self.pls_label.setObjectName(_fromUtf8("pls_label"))
        self.horizontalLayout.addWidget(self.pls_label)
        self.pls_spinbox = QtGui.QSpinBox(self.pls)
        self.pls_spinbox.setObjectName(_fromUtf8("pls_spinbox"))
        self.horizontalLayout.addWidget(self.pls_spinbox)
        self.verticalLayout_8.addWidget(self.pls)


        self.pls.setTitle(_translate("MainWindow", "PLS", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

