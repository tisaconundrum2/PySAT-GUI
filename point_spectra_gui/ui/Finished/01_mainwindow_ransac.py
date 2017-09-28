


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
        self.ransac = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.ransac.setFont(font)
        self.ransac.setObjectName("ransac")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ransac)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ransac_vlayout_2 = QtWidgets.QVBoxLayout()
        self.ransac_vlayout_2.setContentsMargins(11, 11, 11, 11)
        self.ransac_vlayout_2.setSpacing(6)
        self.ransac_vlayout_2.setObjectName("ransac_vlayout_2")
        self.ransac_loss_func_hlayout_2 = QtWidgets.QHBoxLayout()
        self.ransac_loss_func_hlayout_2.setContentsMargins(11, 11, 11, 11)
        self.ransac_loss_func_hlayout_2.setSpacing(6)
        self.ransac_loss_func_hlayout_2.setObjectName("ransac_loss_func_hlayout_2")
        self.ransac_loss_func_2 = QtWidgets.QComboBox(self.ransac)
        self.ransac_loss_func_2.setObjectName("ransac_loss_func_2")
        self.ransac_loss_func_2.addItem("")
        self.ransac_loss_func_2.addItem("")
        self.ransac_loss_func_2.addItem("")
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_loss_func_2)
        self.ransac_threshold_label_2 = QtWidgets.QLabel(self.ransac)
        self.ransac_threshold_label_2.setObjectName("ransac_threshold_label_2")
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_label_2)
        self.ransac_threshold_2 = QtWidgets.QDoubleSpinBox(self.ransac)
        self.ransac_threshold_2.setObjectName("ransac_threshold_2")
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_threshold_2)
        self.ransac_min_label_2 = QtWidgets.QLabel(self.ransac)
        self.ransac_min_label_2.setObjectName("ransac_min_label_2")
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_label_2)
        self.ransac_min_2 = QtWidgets.QDoubleSpinBox(self.ransac)
        self.ransac_min_2.setObjectName("ransac_min_2")
        self.ransac_loss_func_hlayout_2.addWidget(self.ransac_min_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ransac_loss_func_hlayout_2.addItem(spacerItem)
        self.ransac_vlayout_2.addLayout(self.ransac_loss_func_hlayout_2)
        self.horizontalLayout.addLayout(self.ransac_vlayout_2)
        self.verticalLayout_8.addWidget(self.ransac)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.ransac.setTitle(_translate("MainWindow", "Ransac"))
        self.ransac_loss_func_2.setItemText(0, _translate("MainWindow", "Loss Function"))
        self.ransac_loss_func_2.setItemText(1, _translate("MainWindow", "Absolute Error"))
        self.ransac_loss_func_2.setItemText(2, _translate("MainWindow", "Squared Error"))
        self.ransac_threshold_label_2.setText(_translate("MainWindow", "Threshold"))
        self.ransac_min_label_2.setText(_translate("MainWindow", "Minimum samples"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



