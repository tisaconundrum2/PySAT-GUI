




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
        self.pca = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.pca.setFont(font)
        self.pca.setObjectName(_fromUtf8("pca"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pca)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pca_vlayout = QtGui.QVBoxLayout()
        self.pca_vlayout.setMargin(11)
        self.pca_vlayout.setSpacing(6)
        self.pca_vlayout.setObjectName(_fromUtf8("pca_vlayout"))
        self.pca_choose_data = QtGui.QComboBox(self.pca)
        self.pca_choose_data.setObjectName(_fromUtf8("pca_choose_data"))
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtGui.QHBoxLayout()
        self.pca_hlayout.setMargin(11)
        self.pca_hlayout.setSpacing(6)
        self.pca_hlayout.setObjectName(_fromUtf8("pca_hlayout"))
        self.pca_nc_label = QtGui.QLabel(self.pca)
        self.pca_nc_label.setObjectName(_fromUtf8("pca_nc_label"))
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtGui.QSpinBox(self.pca)
        self.pca_nc.setObjectName(_fromUtf8("pca_nc"))
        self.pca_hlayout.addWidget(self.pca_nc)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtGui.QPushButton(self.pca)
        self.pca_button.setObjectName(_fromUtf8("pca_button"))
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout.addLayout(self.pca_vlayout)
        self.verticalLayout_8.addWidget(self.pca)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.pca.setTitle(_translate("MainWindow", "Files", None))
        self.pca_choose_data.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.pca_choose_data.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.pca_button.setText(_translate("MainWindow", "Do PCA", None))
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
        self.pca = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font.setPointSize(10)
        self.pca.setFont(font)
        self.pca.setObjectName(_fromUtf8("pca"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pca)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pca_vlayout = QtGui.QVBoxLayout()
        self.pca_vlayout.setMargin(11)
        self.pca_vlayout.setSpacing(6)
        self.pca_vlayout.setObjectName(_fromUtf8("pca_vlayout"))
        self.pca_choose_data = QtGui.QComboBox(self.pca)
        self.pca_choose_data.setObjectName(_fromUtf8("pca_choose_data"))
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtGui.QHBoxLayout()
        self.pca_hlayout.setMargin(11)
        self.pca_hlayout.setSpacing(6)
        self.pca_hlayout.setObjectName(_fromUtf8("pca_hlayout"))
        self.pca_nc_label = QtGui.QLabel(self.pca)
        self.pca_nc_label.setObjectName(_fromUtf8("pca_nc_label"))
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtGui.QSpinBox(self.pca)
        self.pca_nc.setObjectName(_fromUtf8("pca_nc"))
        self.pca_hlayout.addWidget(self.pca_nc)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtGui.QPushButton(self.pca)
        self.pca_button.setObjectName(_fromUtf8("pca_button"))
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout.addLayout(self.pca_vlayout)
        self.verticalLayout_8.addWidget(self.pca)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem1)


        self.pca.setTitle(_translate("MainWindow", "Files", None))
        self.pca_choose_data.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.pca_choose_data.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.pca_button.setText(_translate("MainWindow", "Do PCA", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))

