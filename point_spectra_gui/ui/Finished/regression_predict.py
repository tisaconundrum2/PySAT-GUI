


class Ui_regression(object):
    def setupUi(self, regression):
        regression.setObjectName("regression")
        regression.resize(438, 244)
        regression.setMinimumSize(QtCore.QSize(400, 150))
        regression.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(regression)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.regression_vlayout = QtWidgets.QVBoxLayout()
        self.regression_vlayout.setObjectName("regression_vlayout")
        self.regression_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosedata_hlayout.setObjectName("regression_choosedata_hlayout")
        self.regression_choosedata_label = QtWidgets.QLabel(regression)
        self.regression_choosedata_label.setObjectName("regression_choosedata_label")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtWidgets.QComboBox(regression)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata.addItem("")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        self.regression_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosealg_hlayout.setObjectName("regression_choosealg_hlayout")
        self.regression_choosealg_label = QtWidgets.QLabel(regression)
        self.regression_choosealg_label.setObjectName("regression_choosealg_label")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_choosealg = QtWidgets.QComboBox(regression)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName("regression_choosealg")
        self.regression_choosealg.addItem("")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.verticalLayout_2.addLayout(self.regression_vlayout)

        self.retranslateUi(regression)
        QtCore.QMetaObject.connectSlotsByName(regression)

    def retranslateUi(self, regression):
        regression.setWindowTitle(_translate("regression", "Regression"))
        regression.setTitle(_translate("regression", "Regression - Predict"))
        self.regression_choosedata_label.setText(_translate("regression", "Choose data:"))
        self.regression_choosedata.setItemText(0, _translate("regression", "Populate this list from the available data frames"))
        self.regression_choosealg_label.setText(_translate("regression", "Choose Model:"))
        self.regression_choosealg.setItemText(0, _translate("regression", "Populate this list from the list of models"))


    regression = QtWidgets.QGroupBox()
    ui = Ui_regression()
    ui.setupUi(regression)
    regression.show()

