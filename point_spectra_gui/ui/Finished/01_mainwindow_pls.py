


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
        self.pls = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.pls.setFont(font)
        self.pls.setObjectName("pls")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pls)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pls_label = QtWidgets.QLabel(self.pls)
        self.pls_label.setObjectName("pls_label")
        self.horizontalLayout.addWidget(self.pls_label)
        self.pls_spinbox = QtWidgets.QSpinBox(self.pls)
        self.pls_spinbox.setObjectName("pls_spinbox")
        self.horizontalLayout.addWidget(self.pls_spinbox)
        self.verticalLayout_8.addWidget(self.pls)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)


        self.pls.setTitle(_translate("MainWindow", "PLS"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



