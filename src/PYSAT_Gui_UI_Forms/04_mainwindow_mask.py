# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Documents\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\04_mainwindow_mask.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(581, 843)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setMargin(11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 561, 721))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaWidgetContents_2.setFont(font)
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
""))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.masked = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.masked.setFont(font)
        self.masked.setObjectName(_fromUtf8("masked"))
        self.CrossValid_3 = QtGui.QVBoxLayout(self.masked)
        self.CrossValid_3.setMargin(11)
        self.CrossValid_3.setSpacing(6)
        self.CrossValid_3.setObjectName(_fromUtf8("CrossValid_3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setMargin(11)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setMargin(11)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.label_16 = QtGui.QLabel(self.masked)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_23.addWidget(self.label_16)
        self.horizontalLayout_12.addLayout(self.verticalLayout_23)
        self.CrossValid_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8.addWidget(self.masked)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.OK = QtGui.QGroupBox(self.centralWidget)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.ok = QtGui.QHBoxLayout(self.OK)
        self.ok.setMargin(11)
        self.ok.setSpacing(6)
        self.ok.setObjectName(_fromUtf8("ok"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.ok.addWidget(self.okButton)
        self.verticalLayout_9.addWidget(self.OK)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPreprocessing = QtGui.QMenu(self.menuBar)
        self.menuPreprocessing.setObjectName(_fromUtf8("menuPreprocessing"))
        self.menuBaseline_Removal = QtGui.QMenu(self.menuPreprocessing)
        self.menuBaseline_Removal.setObjectName(_fromUtf8("menuBaseline_Removal"))
        self.menuCalibration_Transfer = QtGui.QMenu(self.menuPreprocessing)
        self.menuCalibration_Transfer.setObjectName(_fromUtf8("menuCalibration_Transfer"))
        self.menuRegression = QtGui.QMenu(self.menuBar)
        self.menuRegression.setObjectName(_fromUtf8("menuRegression"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuClassification = QtGui.QMenu(self.menuBar)
        self.menuClassification.setObjectName(_fromUtf8("menuClassification"))
        self.menuSupervised = QtGui.QMenu(self.menuClassification)
        self.menuSupervised.setObjectName(_fromUtf8("menuSupervised"))
        self.menuClustering = QtGui.QMenu(self.menuClassification)
        self.menuClustering.setObjectName(_fromUtf8("menuClustering"))
        self.menuVisualization = QtGui.QMenu(self.menuBar)
        self.menuVisualization.setObjectName(_fromUtf8("menuVisualization"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_Refence_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Refence_Data.setObjectName(_fromUtf8("actionLoad_Refence_Data"))
        self.actionLoad_Unknown_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName(_fromUtf8("actionLoad_Unknown_Data"))
        self.actionSave_Current_Workflow = QtGui.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName(_fromUtf8("actionSave_Current_Workflow"))
        self.actionSave_Current_Plots = QtGui.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName(_fromUtf8("actionSave_Current_Plots"))
        self.actionSave_Current_Data = QtGui.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName(_fromUtf8("actionSave_Current_Data"))
        self.actionCreate_New_Workflow = QtGui.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName(_fromUtf8("actionCreate_New_Workflow"))
        self.actionNoise_Reduction = QtGui.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName(_fromUtf8("actionNoise_Reduction"))
        self.actionApply_Mask = QtGui.QAction(MainWindow)
        self.actionApply_Mask.setObjectName(_fromUtf8("actionApply_Mask"))
        self.actionInterpolate = QtGui.QAction(MainWindow)
        self.actionInterpolate.setObjectName(_fromUtf8("actionInterpolate"))
        self.actionInstrument_Response = QtGui.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName(_fromUtf8("actionInstrument_Response"))
        self.actionALS = QtGui.QAction(MainWindow)
        self.actionALS.setObjectName(_fromUtf8("actionALS"))
        self.actionDietrich = QtGui.QAction(MainWindow)
        self.actionDietrich.setObjectName(_fromUtf8("actionDietrich"))
