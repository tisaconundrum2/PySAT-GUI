




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
        self.ransac = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.ransac.setFont(font)
        self.ransac.setObjectName(_fromUtf8("ransac"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.ransac)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ransac_vlayout_2 = QtGui.QVBoxLayout()
        self.ransac_vlayout_2.setMargin(11)
        self.ransac_vlayout_2.setSpacing(6)
        self.ransac_vlayout_2.setObjectName(_fromUtf8("ransac_vlayout_2"))
        self.ransac_loss_func_hlayout_2 = QtGui.QHBoxLayout()
        self.ransac_loss_func_hlayout_2.setMargin(11)
        self.ransac_loss_func_hlayout_2.setSpacing(6)
        self.ransac_loss_func_hlayout_2.setObjectName(_fromUtf8("ransac_loss_func_hlayout_2"))
        self.ransac_loss_func_2 = QtGui.QComboBox(self.ransac)
        self.ransac_loss_func_2.setObjectName(_fromUtf8("ransac_loss_func_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_loss_func_2)
        self.ransac_threshold_label_2 = QtGui.QLabel(self.ransac)
        self.ransac_threshold_label_2.setObjectName(_fromUtf8("ransac_threshold_label_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_label_2)
        self.ransac_threshold_2 = QtGui.QDoubleSpinBox(self.ransac)
        self.ransac_threshold_2.setObjectName(_fromUtf8("ransac_threshold_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_2)
        self.ransac_min_label_2 = QtGui.QLabel(self.ransac)
        self.ransac_min_label_2.setObjectName(_fromUtf8("ransac_min_label_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_label_2)
        self.ransac_min_2 = QtGui.QDoubleSpinBox(self.ransac)
        self.ransac_min_2.setObjectName(_fromUtf8("ransac_min_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_2)
        self.ransac_loss_func_hlayout_2.addItem(spacerItem)
        self.ransac_vlayout_2.addLayout(self.ransac_loss_func_hlayout_2)
        self.horizontalLayout.addLayout(self.ransac_vlayout_2)
        self.verticalLayout_8.addWidget(self.ransac)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.ransac.setTitle(_translate("MainWindow", "Files", None))
        self.ransac_loss_func_2.setItemText(0, _translate("MainWindow", "Loss Function", None))
        self.ransac_loss_func_2.setItemText(1, _translate("MainWindow", "Absolute Error", None))
        self.ransac_loss_func_2.setItemText(2, _translate("MainWindow", "Squared Error", None))
        self.ransac_threshold_label_2.setText(_translate("MainWindow", "Threshold", None))
        self.ransac_min_label_2.setText(_translate("MainWindow", "Minimum samples ", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))






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
        self.ransac = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.ransac.setFont(font)
        self.ransac.setObjectName(_fromUtf8("ransac"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.ransac)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ransac_vlayout_2 = QtGui.QVBoxLayout()
        self.ransac_vlayout_2.setMargin(11)
        self.ransac_vlayout_2.setSpacing(6)
        self.ransac_vlayout_2.setObjectName(_fromUtf8("ransac_vlayout_2"))
        self.ransac_loss_func_hlayout_2 = QtGui.QHBoxLayout()
        self.ransac_loss_func_hlayout_2.setMargin(11)
        self.ransac_loss_func_hlayout_2.setSpacing(6)
        self.ransac_loss_func_hlayout_2.setObjectName(_fromUtf8("ransac_loss_func_hlayout_2"))
        self.ransac_loss_func_2 = QtGui.QComboBox(self.ransac)
        self.ransac_loss_func_2.setObjectName(_fromUtf8("ransac_loss_func_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_loss_func_2)
        self.ransac_threshold_label_2 = QtGui.QLabel(self.ransac)
        self.ransac_threshold_label_2.setObjectName(_fromUtf8("ransac_threshold_label_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_label_2)
        self.ransac_threshold_2 = QtGui.QDoubleSpinBox(self.ransac)
        self.ransac_threshold_2.setObjectName(_fromUtf8("ransac_threshold_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_2)
        self.ransac_min_label_2 = QtGui.QLabel(self.ransac)
        self.ransac_min_label_2.setObjectName(_fromUtf8("ransac_min_label_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_label_2)
        self.ransac_min_2 = QtGui.QDoubleSpinBox(self.ransac)
        self.ransac_min_2.setObjectName(_fromUtf8("ransac_min_2"))
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_2)
        self.ransac_loss_func_hlayout_2.addItem(spacerItem)
        self.ransac_vlayout_2.addLayout(self.ransac_loss_func_hlayout_2)
        self.horizontalLayout.addLayout(self.ransac_vlayout_2)
        self.verticalLayout_8.addWidget(self.ransac)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.ransac.setTitle(_translate("MainWindow", "Files", None))
        self.ransac_loss_func_2.setItemText(0, _translate("MainWindow", "Loss Function", None))
        self.ransac_loss_func_2.setItemText(1, _translate("MainWindow", "Absolute Error", None))
        self.ransac_loss_func_2.setItemText(2, _translate("MainWindow", "Squared Error", None))
        self.ransac_threshold_label_2.setText(_translate("MainWindow", "Threshold", None))
        self.ransac_min_label_2.setText(_translate("MainWindow", "Minimum samples ", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

