


        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 557, 695))
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
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_8.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 26))


        self.groupBox.setTitle(_translate("MainWindow", "Scores and Loadings Plot"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Data (populate this from\n"
"                                                                        self.datakeys)\n"
"                                                                    "))
        self.label.setText(_translate("MainWindow", "Choose Method:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "PCA"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "FastICA"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ICA-JADE"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Choose X (populate this from column\n"
"                                                                                names under the appropriate method name)\n"
"                                                                            "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Choose Y (populate this the same as\n"
"                                                                                X)\n"
"                                                                            "))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



