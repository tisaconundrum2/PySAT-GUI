


        MainWindow.resize(631, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionTest_2 = QtWidgets.QAction(MainWindow)
        self.actionTest_2.setObjectName("actionTest_2")
        self.menuFile.addAction(self.actionTest)
        self.menuFile.addAction(self.actionTest_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionTest_2.setText(_translate("MainWindow", "Test"))



