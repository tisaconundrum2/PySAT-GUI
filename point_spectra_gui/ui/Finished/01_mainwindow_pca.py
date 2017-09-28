


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
        self.pca = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.pca.setFont(font)
        self.pca.setObjectName("pca")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pca)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pca_vlayout = QtWidgets.QVBoxLayout()
        self.pca_vlayout.setContentsMargins(11, 11, 11, 11)
        self.pca_vlayout.setSpacing(6)
        self.pca_vlayout.setObjectName("pca_vlayout")
        self.pca_choose_data = QtWidgets.QComboBox(self.pca)
        self.pca_choose_data.setObjectName("pca_choose_data")
        self.pca_choose_data.addItem("")
        self.pca_choose_data.addItem("")
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtWidgets.QHBoxLayout()
        self.pca_hlayout.setContentsMargins(11, 11, 11, 11)
        self.pca_hlayout.setSpacing(6)
        self.pca_hlayout.setObjectName("pca_hlayout")
        self.pca_nc_label = QtWidgets.QLabel(self.pca)
        self.pca_nc_label.setObjectName("pca_nc_label")
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtWidgets.QSpinBox(self.pca)
        self.pca_nc.setObjectName("pca_nc")
        self.pca_hlayout.addWidget(self.pca_nc)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtWidgets.QPushButton(self.pca)
        self.pca_button.setObjectName("pca_button")
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout.addLayout(self.pca_vlayout)
        self.verticalLayout_8.addWidget(self.pca)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.pca.setTitle(_translate("MainWindow", "PCA"))
        self.pca_choose_data.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.pca_choose_data.setItemText(1, _translate("MainWindow", "Known Data"))
        self.pca_button.setText(_translate("MainWindow", "Do PCA"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



