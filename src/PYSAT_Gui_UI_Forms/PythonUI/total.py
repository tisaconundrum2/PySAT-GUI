# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\00_mainframe_ok.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
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
        self.scrollAreaContents = QtGui.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 561, 742))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaContents.setFont(font)
        self.scrollAreaContents.setStyleSheet(_fromUtf8("QGroupBox {\n"
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
        self.scrollAreaContents.setObjectName(_fromUtf8("scrollAreaContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea.setWidget(self.scrollAreaContents)
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
        self.actionPolyFit = QtGui.QAction(MainWindow)
        self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
        self.actionAirPLS = QtGui.QAction(MainWindow)
        self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
        self.actionFABC = QtGui.QAction(MainWindow)
        self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
        self.actionKK = QtGui.QAction(MainWindow)
        self.actionKK.setObjectName(_fromUtf8("actionKK"))
        self.actionMario = QtGui.QAction(MainWindow)
        self.actionMario.setObjectName(_fromUtf8("actionMario"))
        self.actionMedian = QtGui.QAction(MainWindow)
        self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
        self.actionRubberband = QtGui.QAction(MainWindow)
        self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
        self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
        self.actionRatio = QtGui.QAction(MainWindow)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
        self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName(_fromUtf8("actionPiecewise_Direct_Standardization"))
        self.actionPCA = QtGui.QAction(MainWindow)
        self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
        self.actionICA = QtGui.QAction(MainWindow)
        self.actionICA.setObjectName(_fromUtf8("actionICA"))
        self.actionK_Means = QtGui.QAction(MainWindow)
        self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
        self.actionHierarchical = QtGui.QAction(MainWindow)
        self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
        self.actionOthers = QtGui.QAction(MainWindow)
        self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
        self.actionOthers_2 = QtGui.QAction(MainWindow)
        self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
        self.actionOthers_3 = QtGui.QAction(MainWindow)
        self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
        self.actionPLS = QtGui.QAction(MainWindow)
        self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
        self.actionSM_PLS = QtGui.QAction(MainWindow)
        self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
        self.actionICA_Regression = QtGui.QAction(MainWindow)
        self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
        self.actionGaussian_Process = QtGui.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
        self.actionMLP = QtGui.QAction(MainWindow)
        self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
        self.actionSVM = QtGui.QAction(MainWindow)
        self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
        self.actionOthers_4 = QtGui.QAction(MainWindow)
        self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
        self.actionOthers_5 = QtGui.QAction(MainWindow)
        self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
        self.actionContent_2 = QtGui.QAction(MainWindow)
        self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNormalization = QtGui.QAction(MainWindow)
        self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
        self.actionICA_2 = QtGui.QAction(MainWindow)
        self.actionICA_2.setObjectName(_fromUtf8("actionICA_2"))
        self.actionPCA_2 = QtGui.QAction(MainWindow)
        self.actionPCA_2.setObjectName(_fromUtf8("actionPCA_2"))
        self.actionPLS_DA = QtGui.QAction(MainWindow)
        self.actionPLS_DA.setObjectName(_fromUtf8("actionPLS_DA"))
        self.actionSIMCA = QtGui.QAction(MainWindow)
        self.actionSIMCA.setObjectName(_fromUtf8("actionSIMCA"))
        self.actionK_means = QtGui.QAction(MainWindow)
        self.actionK_means.setObjectName(_fromUtf8("actionK_means"))
        self.actionHierarchical_2 = QtGui.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName(_fromUtf8("actionHierarchical_2"))
        self.actionCross_Validation = QtGui.QAction(MainWindow)
        self.actionCross_Validation.setObjectName(_fromUtf8("actionCross_Validation"))
        self.actionTrain = QtGui.QAction(MainWindow)
        self.actionTrain.setObjectName(_fromUtf8("actionTrain"))
        self.actionPredict = QtGui.QAction(MainWindow)
        self.actionPredict.setObjectName(_fromUtf8("actionPredict"))
        self.actionLine_Plot = QtGui.QAction(MainWindow)
        self.actionLine_Plot.setObjectName(_fromUtf8("actionLine_Plot"))
        self.action1_to_1_Plot = QtGui.QAction(MainWindow)
        self.action1_to_1_Plot.setObjectName(_fromUtf8("action1_to_1_Plot"))
        self.actionScatter_Plot = QtGui.QAction(MainWindow)
        self.actionScatter_Plot.setObjectName(_fromUtf8("actionScatter_Plot"))
        self.actionSet_output_location = QtGui.QAction(MainWindow)
        self.actionSet_output_location.setObjectName(_fromUtf8("actionSet_output_location"))
        self.actionCreate_N_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName(_fromUtf8("actionCreate_N_Folds"))
        self.actionCreate_Test_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName(_fromUtf8("actionCreate_Test_Folds"))
        self.actionSubmodel_Ranges = QtGui.QAction(MainWindow)
        self.actionSubmodel_Ranges.setObjectName(_fromUtf8("actionSubmodel_Ranges"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data", None))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)", None))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
        self.actionALS.setText(_translate("MainWindow", "ALS", None))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
        self.actionFABC.setText(_translate("MainWindow", "FABC", None))
        self.actionKK.setText(_translate("MainWindow", "KK", None))
        self.actionMario.setText(_translate("MainWindow", "Mario", None))
        self.actionMedian.setText(_translate("MainWindow", "Median", None))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
        self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization", None))
        self.actionPCA.setText(_translate("MainWindow", "PCA", None))
        self.actionICA.setText(_translate("MainWindow", "ICA", None))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionOthers.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
        self.actionPLS.setText(_translate("MainWindow", "PLS", None))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
        self.actionMLP.setText(_translate("MainWindow", "MLP", None))
        self.actionSVM.setText(_translate("MainWindow", "SVM", None))
        self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
        self.actionIndex.setText(_translate("MainWindow", "Index", None))
        self.actionContent_2.setText(_translate("MainWindow", "Content", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))
        self.actionICA_2.setText(_translate("MainWindow", "ICA", None))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA", None))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA", None))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA", None))
        self.actionK_means.setText(_translate("MainWindow", "K-means", None))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation", None))
        self.actionTrain.setText(_translate("MainWindow", "Train", None))
        self.actionPredict.setText(_translate("MainWindow", "Predict", None))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot", None))
        self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot", None))
        self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot", None))
        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location", None))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds", None))
        self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds", None))
        self.actionSubmodel_Ranges.setText(_translate("MainWindow", "Submodel Ranges", None))
class Ui_file_out_path(object):
    def setupUi(self, file_out_path):
        file_out_path.setObjectName(_fromUtf8("file_out_path"))
        file_out_path.resize(600, 150)
        file_out_path.setMinimumSize(QtCore.QSize(600, 150))
        file_out_path.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalLayout = QtGui.QHBoxLayout(file_out_path)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_out_path_label = QtGui.QLabel(file_out_path)
        self.file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtGui.QLineEdit(file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtGui.QToolButton(file_out_path)
        self.file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
        self.horizontalLayout.addWidget(self.file_out_path_button)

        self.retranslateUi(file_out_path)
        QtCore.QMetaObject.connectSlotsByName(file_out_path)

    def retranslateUi(self, file_out_path):
        file_out_path.setWindowTitle(_translate("file_out_path", "PCA", None))
        file_out_path.setTitle(_translate("file_out_path", "Output Folder", None))
        self.file_out_path_label.setText(_translate("file_out_path", "File Name", None))
        self.file_out_path_line_edit.setText(_translate("file_out_path", "*/", None))
        self.file_out_path_button.setText(_translate("file_out_path", "...", None))
class Ui_get_mask(object):
    def setupUi(self, get_mask):
        get_mask.setObjectName(_fromUtf8("get_mask"))
        get_mask.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_mask)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_mask_label = QtGui.QLabel(get_mask)
        self.get_mask_label.setObjectName(_fromUtf8("get_mask_label"))
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtGui.QLineEdit(get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName(_fromUtf8("get_mask_line_edit"))
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtGui.QToolButton(get_mask)
        self.get_mask_button.setObjectName(_fromUtf8("get_mask_button"))
        self.horizontalLayout.addWidget(self.get_mask_button)

        self.retranslateUi(get_mask)
        QtCore.QMetaObject.connectSlotsByName(get_mask)

    def retranslateUi(self, get_mask):
        get_mask.setWindowTitle(_translate("get_mask", "GroupBox", None))
        get_mask.setTitle(_translate("get_mask", "Get Mask File", None))
        self.get_mask_label.setText(_translate("get_mask", "File Name", None))
        self.get_mask_line_edit.setText(_translate("get_mask", "*.csv", None))
        self.get_mask_button.setText(_translate("get_mask", "...", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_pca.ui'
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

class Ui_pca(object):
    def setupUi(self, pca):
        pca.setObjectName(_fromUtf8("pca"))
        pca.resize(614, 150)
        pca.setMinimumSize(QtCore.QSize(600, 150))
        pca.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(pca)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pca_vlayout = QtGui.QVBoxLayout()
        self.pca_vlayout.setObjectName(_fromUtf8("pca_vlayout"))
        self.pca_choose_data = QtGui.QComboBox(pca)
        self.pca_choose_data.setObjectName(_fromUtf8("pca_choose_data"))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtGui.QHBoxLayout()
        self.pca_hlayout.setObjectName(_fromUtf8("pca_hlayout"))
        self.pca_nc_label = QtGui.QLabel(pca)
        self.pca_nc_label.setObjectName(_fromUtf8("pca_nc_label"))
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtGui.QSpinBox(pca)
        self.pca_nc.setObjectName(_fromUtf8("pca_nc"))
        self.pca_hlayout.addWidget(self.pca_nc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtGui.QPushButton(pca)
        self.pca_button.setObjectName(_fromUtf8("pca_button"))
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout_2.addLayout(self.pca_vlayout)

        self.retranslateUi(pca)
        QtCore.QMetaObject.connectSlotsByName(pca)

    def retranslateUi(self, pca):
        pca.setWindowTitle(_translate("pca", "PCA", None))
        pca.setTitle(_translate("pca", "PCA", None))
        self.pca_choose_data.setItemText(0, _translate("pca", "Choose Data", None))
        self.pca_choose_data.setItemText(1, _translate("pca", "Known Data", None))
        self.pca_nc_label.setText(_translate("pca", "# of components", None))
        self.pca_button.setText(_translate("pca", "Do PCA", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_pls.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(254, 54)
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 10, 81, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "# of components", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_ransac.ui'
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

class Ui_ransac(object):
    def setupUi(self, ransac):
        ransac.setObjectName(_fromUtf8("ransac"))
        ransac.resize(676, 100)
        ransac.setMinimumSize(QtCore.QSize(600, 100))
        ransac.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ransac)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ransac_vlayout = QtGui.QVBoxLayout()
        self.ransac_vlayout.setObjectName(_fromUtf8("ransac_vlayout"))
        self.ransac_loss_func_hlayout = QtGui.QHBoxLayout()
        self.ransac_loss_func_hlayout.setObjectName(_fromUtf8("ransac_loss_func_hlayout"))
        self.ransac_loss_func = QtGui.QComboBox(ransac)
        self.ransac_loss_func.setObjectName(_fromUtf8("ransac_loss_func"))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_loss_func)
        self.ransac_threshold_label = QtGui.QLabel(ransac)
        self.ransac_threshold_label.setObjectName(_fromUtf8("ransac_threshold_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold_label)
        self.ransac_threshold = QtGui.QDoubleSpinBox(ransac)
        self.ransac_threshold.setObjectName(_fromUtf8("ransac_threshold"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold)
        self.ransac_min_label = QtGui.QLabel(ransac)
        self.ransac_min_label.setObjectName(_fromUtf8("ransac_min_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min_label)
        self.ransac_min = QtGui.QDoubleSpinBox(ransac)
        self.ransac_min.setObjectName(_fromUtf8("ransac_min"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_loss_func_hlayout.addItem(spacerItem)
        self.ransac_vlayout.addLayout(self.ransac_loss_func_hlayout)
        self.verticalLayout_2.addLayout(self.ransac_vlayout)

        self.retranslateUi(ransac)
        QtCore.QMetaObject.connectSlotsByName(ransac)

    def retranslateUi(self, ransac):
        ransac.setWindowTitle(_translate("ransac", "RANSAC", None))
        ransac.setTitle(_translate("ransac", "RANSAC", None))
        self.ransac_loss_func.setItemText(0, _translate("ransac", "Loss Function", None))
        self.ransac_loss_func.setItemText(1, _translate("ransac", "Absolute Error", None))
        self.ransac_loss_func.setItemText(2, _translate("ransac", "Squared Error", None))
        self.ransac_threshold_label.setText(_translate("ransac", "Threshold", None))
        self.ransac_min_label.setText(_translate("ransac", "Minimum samples ", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_regression.ui'
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

class Ui_regression(object):
    def setupUi(self, regression):
        regression.setObjectName(_fromUtf8("regression"))
        regression.resize(644, 525)
        regression.setMinimumSize(QtCore.QSize(600, 150))
        regression.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtGui.QVBoxLayout(regression)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.regression_vlayout = QtGui.QVBoxLayout()
        self.regression_vlayout.setObjectName(_fromUtf8("regression_vlayout"))
        self.regression_choosedata_hlayout = QtGui.QHBoxLayout()
        self.regression_choosedata_hlayout.setObjectName(_fromUtf8("regression_choosedata_hlayout"))
        self.label = QtGui.QLabel(regression)
        self.label.setObjectName(_fromUtf8("label"))
        self.regression_choosedata_hlayout.addWidget(self.label)
        self.regression_choosedata = QtGui.QComboBox(regression)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
        self.regression_choosedata.addItem(_fromUtf8(""))
        self.regression_choosedata.addItem(_fromUtf8(""))
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        self.regression_choosevars_hlayout = QtGui.QHBoxLayout()
        self.regression_choosevars_hlayout.setObjectName(_fromUtf8("regression_choosevars_hlayout"))
        self.regression_train_choosex_label = QtGui.QLabel(regression)
        self.regression_train_choosex_label.setObjectName(_fromUtf8("regression_train_choosex_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex_label)
        self.regression_train_choosex = QtGui.QListWidget(regression)
        self.regression_train_choosex.setObjectName(_fromUtf8("regression_train_choosex"))
        item = QtGui.QListWidgetItem()
        self.regression_train_choosex.addItem(item)
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex)
        self.regression_train_choosey_label = QtGui.QLabel(regression)
        self.regression_train_choosey_label.setObjectName(_fromUtf8("regression_train_choosey_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey_label)
        self.regression_train_choosey = QtGui.QListWidget(regression)
        self.regression_train_choosey.setObjectName(_fromUtf8("regression_train_choosey"))
        item = QtGui.QListWidgetItem()
        self.regression_train_choosey.addItem(item)
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosevars_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosevars_hlayout)
        self.regression_choosealg_hlayout = QtGui.QHBoxLayout()
        self.regression_choosealg_hlayout.setObjectName(_fromUtf8("regression_choosealg_hlayout"))
        self.regression_choosealg_label = QtGui.QLabel(regression)
        self.regression_choosealg_label.setObjectName(_fromUtf8("regression_choosealg_label"))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_choosealg = QtGui.QComboBox(regression)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName(_fromUtf8("regression_choosealg"))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(spacerItem2)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.pls_widget = QtGui.QWidget(regression)
        self.pls_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.pls_widget.setObjectName(_fromUtf8("pls_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.pls_widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pls_nc_label = QtGui.QLabel(self.pls_widget)
        self.pls_nc_label.setObjectName(_fromUtf8("pls_nc_label"))
        self.horizontalLayout_2.addWidget(self.pls_nc_label)
        self.pls_nc_spinbox = QtGui.QSpinBox(self.pls_widget)
        self.pls_nc_spinbox.setObjectName(_fromUtf8("pls_nc_spinbox"))
        self.horizontalLayout_2.addWidget(self.pls_nc_spinbox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.regression_vlayout.addWidget(self.pls_widget)
        self.gp_widget = QtGui.QWidget(regression)
        self.gp_widget.setObjectName(_fromUtf8("gp_widget"))
        self.gp_vlayout = QtGui.QVBoxLayout(self.gp_widget)
        self.gp_vlayout.setObjectName(_fromUtf8("gp_vlayout"))
        self.gp_dim_red_hlayout = QtGui.QHBoxLayout()
        self.gp_dim_red_hlayout.setObjectName(_fromUtf8("gp_dim_red_hlayout"))
        self.gp_dim_red_label = QtGui.QLabel(self.gp_widget)
        self.gp_dim_red_label.setObjectName(_fromUtf8("gp_dim_red_label"))
        self.gp_dim_red_hlayout.addWidget(self.gp_dim_red_label)
        self.gp_dim_red_combobox = QtGui.QComboBox(self.gp_widget)
        self.gp_dim_red_combobox.setObjectName(_fromUtf8("gp_dim_red_combobox"))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_hlayout.addWidget(self.gp_dim_red_combobox)
        self.gp_vlayout.addLayout(self.gp_dim_red_hlayout)
        self.gp_rand_starts_hlayout = QtGui.QHBoxLayout()
        self.gp_rand_starts_hlayout.setObjectName(_fromUtf8("gp_rand_starts_hlayout"))
        self.gp_rand_starts_label = QtGui.QLabel(self.gp_widget)
        self.gp_rand_starts_label.setObjectName(_fromUtf8("gp_rand_starts_label"))
        self.gp_rand_starts_hlayout.addWidget(self.gp_rand_starts_label)
        self.gp_rand_starts_spin = QtGui.QSpinBox(self.gp_widget)
        self.gp_rand_starts_spin.setObjectName(_fromUtf8("gp_rand_starts_spin"))
        self.gp_rand_starts_hlayout.addWidget(self.gp_rand_starts_spin)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gp_rand_starts_hlayout.addItem(spacerItem4)
        self.gp_vlayout.addLayout(self.gp_rand_starts_hlayout)
        self.gp_theta_hlayout = QtGui.QHBoxLayout()
        self.gp_theta_hlayout.setObjectName(_fromUtf8("gp_theta_hlayout"))
        self.gp_theta0_label = QtGui.QLabel(self.gp_widget)
        self.gp_theta0_label.setObjectName(_fromUtf8("gp_theta0_label"))
        self.gp_theta_hlayout.addWidget(self.gp_theta0_label)
        self.gp_theta0_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_theta0_spin.setObjectName(_fromUtf8("gp_theta0_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_theta0_spin)
        self.gp_thetaL_label = QtGui.QLabel(self.gp_widget)
        self.gp_thetaL_label.setObjectName(_fromUtf8("gp_thetaL_label"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaL_label)
        self.gp_thetaL_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_thetaL_spin.setObjectName(_fromUtf8("gp_thetaL_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaL_spin)
        self.gp_thetaU_label = QtGui.QLabel(self.gp_widget)
        self.gp_thetaU_label.setObjectName(_fromUtf8("gp_thetaU_label"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaU_label)
        self.gp_thetaU_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_thetaU_spin.setObjectName(_fromUtf8("gp_thetaU_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaU_spin)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gp_theta_hlayout.addItem(spacerItem5)
        self.gp_vlayout.addLayout(self.gp_theta_hlayout)
        self.regression_vlayout.addWidget(self.gp_widget)
        self.regression_ransac_checkbox = QtGui.QCheckBox(regression)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.regression_vlayout.addWidget(self.regression_ransac_checkbox)
        self.ransac_vlayout = QtGui.QVBoxLayout()
        self.ransac_vlayout.setObjectName(_fromUtf8("ransac_vlayout"))
        self.ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
        self.ransac_lossfunc_hlayout.setObjectName(_fromUtf8("ransac_lossfunc_hlayout"))
        self.ransac_lossfunc_label = QtGui.QLabel(regression)
        self.ransac_lossfunc_label.setObjectName(_fromUtf8("ransac_lossfunc_label"))
        self.ransac_lossfunc_hlayout.addWidget(self.ransac_lossfunc_label)
        self.ransac_lossfunc_combobox = QtGui.QComboBox(regression)
        self.ransac_lossfunc_combobox.setObjectName(_fromUtf8("ransac_lossfunc_combobox"))
        self.ransac_lossfunc_combobox.addItem(_fromUtf8(""))
        self.ransac_lossfunc_combobox.addItem(_fromUtf8(""))
        self.ransac_lossfunc_hlayout.addWidget(self.ransac_lossfunc_combobox)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_lossfunc_hlayout.addItem(spacerItem6)
        self.ransac_vlayout.addLayout(self.ransac_lossfunc_hlayout)
        self.ransac_thresh_hlayout = QtGui.QHBoxLayout()
        self.ransac_thresh_hlayout.setObjectName(_fromUtf8("ransac_thresh_hlayout"))
        self.ransac_thresh_label = QtGui.QLabel(regression)
        self.ransac_thresh_label.setObjectName(_fromUtf8("ransac_thresh_label"))
        self.ransac_thresh_hlayout.addWidget(self.ransac_thresh_label)
        self.ransac_thresh_spin = QtGui.QDoubleSpinBox(regression)
        self.ransac_thresh_spin.setObjectName(_fromUtf8("ransac_thresh_spin"))
        self.ransac_thresh_hlayout.addWidget(self.ransac_thresh_spin)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_thresh_hlayout.addItem(spacerItem7)
        self.ransac_vlayout.addLayout(self.ransac_thresh_hlayout)
        self.regression_vlayout.addLayout(self.ransac_vlayout)
        self.regression_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.regression_trainbutton_hlayout.setObjectName(_fromUtf8("regression_trainbutton_hlayout"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_trainbutton_hlayout.addItem(spacerItem8)
        self.regression_trainbutton = QtGui.QPushButton(regression)
        self.regression_trainbutton.setObjectName(_fromUtf8("regression_trainbutton"))
        self.regression_trainbutton_hlayout.addWidget(self.regression_trainbutton)
        self.regression_vlayout.addLayout(self.regression_trainbutton_hlayout)
        self.verticalLayout_2.addLayout(self.regression_vlayout)

        self.retranslateUi(regression)
        QtCore.QMetaObject.connectSlotsByName(regression)

    def retranslateUi(self, regression):
        regression.setWindowTitle(_translate("regression", "Regression", None))
        regression.setTitle(_translate("regression", "Regression", None))
        self.label.setText(_translate("regression", "Choose data: ", None))
        self.regression_choosedata.setItemText(0, _translate("regression", "Choose Data", None))
        self.regression_choosedata.setItemText(1, _translate("regression", "Known Data", None))
        self.regression_train_choosex_label.setText(_translate("regression", "Choose X variable(s): ", None))
        __sortingEnabled = self.regression_train_choosex.isSortingEnabled()
        self.regression_train_choosex.setSortingEnabled(False)
        item = self.regression_train_choosex.item(0)
        item.setText(_translate("regression", "Choose X", None))
        self.regression_train_choosex.setSortingEnabled(__sortingEnabled)
        self.regression_train_choosey_label.setText(_translate("regression", "Choose Y variable(s):", None))
        __sortingEnabled = self.regression_train_choosey.isSortingEnabled()
        self.regression_train_choosey.setSortingEnabled(False)
        item = self.regression_train_choosey.item(0)
        item.setText(_translate("regression", "Choose Y", None))
        self.regression_train_choosey.setSortingEnabled(__sortingEnabled)
        self.regression_choosealg_label.setText(_translate("regression", "Choose Algorithm: ", None))
        self.regression_choosealg.setItemText(0, _translate("regression", "PLS", None))
        self.regression_choosealg.setItemText(1, _translate("regression", "GP", None))
        self.regression_choosealg.setItemText(2, _translate("regression", "Others coming soon...", None))
        self.pls_nc_label.setText(_translate("regression", "# of Components: ", None))
        self.gp_dim_red_label.setText(_translate("regression", "Dimensionality reduction method:", None))
        self.gp_dim_red_combobox.setItemText(0, _translate("regression", "PCA", None))
        self.gp_dim_red_combobox.setItemText(1, _translate("regression", "FastICA", None))
        self.gp_dim_red_combobox.setItemText(2, _translate("regression", "ICA - JADE", None))
        self.gp_dim_red_combobox.setItemText(3, _translate("regression", "None", None))
        self.gp_rand_starts_label.setText(_translate("regression", "# of random starts:", None))
        self.gp_theta0_label.setText(_translate("regression", "theta_0", None))
        self.gp_thetaL_label.setText(_translate("regression", "theta_L", None))
        self.gp_thetaU_label.setText(_translate("regression", "theta_U", None))
        self.regression_ransac_checkbox.setText(_translate("regression", "RANSAC", None))
        self.ransac_lossfunc_label.setText(_translate("regression", "Loss function:", None))
        self.ransac_lossfunc_combobox.setItemText(0, _translate("regression", "Squared", None))
        self.ransac_lossfunc_combobox.setItemText(1, _translate("regression", "Absolute", None))
        self.ransac_thresh_label.setText(_translate("regression", "Threshold:", None))
        self.regression_trainbutton.setText(_translate("regression", "Train", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_strat_folds.ui'
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

class Ui_strat_folds(object):
    def setupUi(self, strat_folds):
        strat_folds.setObjectName(_fromUtf8("strat_folds"))
        strat_folds.resize(602, 150)
        strat_folds.setMinimumSize(QtCore.QSize(600, 150))
        strat_folds.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(strat_folds)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout()
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_data.setObjectName(_fromUtf8("strat_folds_choose_data"))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_element = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_element.setObjectName(_fromUtf8("strat_folds_choose_element"))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_element)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_spin = QtGui.QSpinBox(strat_folds)
        self.test_fold_spin.setObjectName(_fromUtf8("test_fold_spin"))
        self.strat_folds_hlayout.addWidget(self.test_fold_spin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(spacerItem)
        self.create_folds = QtGui.QPushButton(strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout_2.addLayout(self.strat_folds_vlayout)

        self.retranslateUi(strat_folds)
        QtCore.QMetaObject.connectSlotsByName(strat_folds)

    def retranslateUi(self, strat_folds):
        strat_folds.setWindowTitle(_translate("strat_folds", "Stratified Folds", None))
        strat_folds.setTitle(_translate("strat_folds", "Stratified Folds", None))
        self.strat_folds_choose_data.setItemText(0, _translate("strat_folds", "Choose Data", None))
        self.strat_folds_choose_data.setItemText(1, _translate("strat_folds", "Unknown Data", None))
        self.strat_folds_choose_data.setItemText(2, _translate("strat_folds", "Known Data", None))
        self.strat_folds_choose_element.setItemText(0, _translate("strat_folds", "Choose Element to Stratify On", None))
        self.strat_folds_choose_element.setItemText(1, _translate("strat_folds", "SiO2", None))
        self.strat_folds_choose_element.setItemText(2, _translate("strat_folds", "TiO2", None))
        self.strat_folds_choose_element.setItemText(3, _translate("strat_folds", "Al2O3", None))
        self.strat_folds_choose_element.setItemText(4, _translate("strat_folds", "FeOT", None))
        self.strat_folds_choose_element.setItemText(5, _translate("strat_folds", "MgO", None))
        self.strat_folds_choose_element.setItemText(6, _translate("strat_folds", "CaO", None))
        self.strat_folds_choose_element.setItemText(7, _translate("strat_folds", "Na2O", None))
        self.strat_folds_choose_element.setItemText(8, _translate("strat_folds", "K2O", None))
        self.nfolds_label.setText(_translate("strat_folds", "N folds", None))
        self.test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_submodel.ui'
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

class Ui_submodel(object):
    def setupUi(self, submodel):
        submodel.setObjectName(_fromUtf8("submodel"))
        submodel.resize(644, 238)
        submodel.setMinimumSize(QtCore.QSize(600, 150))
        submodel.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtGui.QVBoxLayout(submodel)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.submodel_vlayout = QtGui.QVBoxLayout()
        self.submodel_vlayout.setObjectName(_fromUtf8("submodel_vlayout"))
        self.submodel_choosedata_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosedata_hlayout.setObjectName(_fromUtf8("submodel_choosedata_hlayout"))
        self.submodel_choosedata = QtGui.QComboBox(submodel)
        self.submodel_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosedata.setObjectName(_fromUtf8("submodel_choosedata"))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata_hlayout.addWidget(self.submodel_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosedata_hlayout.addItem(spacerItem)
        self.submodel_vlayout.addLayout(self.submodel_choosedata_hlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(submodel)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(submodel)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(submodel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(submodel)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.submodel_vlayout.addLayout(self.horizontalLayout)
        self.submodel_choosealg_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosealg_hlayout.setObjectName(_fromUtf8("submodel_choosealg_hlayout"))
        self.submodel_choosealg = QtGui.QComboBox(submodel)
        self.submodel_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosealg.setObjectName(_fromUtf8("submodel_choosealg"))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg_hlayout.addWidget(self.submodel_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosealg_hlayout.addItem(spacerItem2)
        self.submodel_vlayout.addLayout(self.submodel_choosealg_hlayout)
        self.regression_ransac_checkbox = QtGui.QCheckBox(submodel)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.submodel_vlayout.addWidget(self.regression_ransac_checkbox)
        self.submodel_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.submodel_trainbutton_hlayout.setObjectName(_fromUtf8("submodel_trainbutton_hlayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_trainbutton_hlayout.addItem(spacerItem3)
        self.submodel_trainbutton = QtGui.QPushButton(submodel)
        self.submodel_trainbutton.setObjectName(_fromUtf8("submodel_trainbutton"))
        self.submodel_trainbutton_hlayout.addWidget(self.submodel_trainbutton)
        self.submodel_vlayout.addLayout(self.submodel_trainbutton_hlayout)
        self.verticalLayout_2.addLayout(self.submodel_vlayout)

        self.retranslateUi(submodel)
        QtCore.QMetaObject.connectSlotsByName(submodel)

    def retranslateUi(self, submodel):
        submodel.setWindowTitle(_translate("submodel", "Regression", None))
        submodel.setTitle(_translate("submodel", "Regression", None))
        self.submodel_choosedata.setItemText(0, _translate("submodel", "Choose Data", None))
        self.submodel_choosedata.setItemText(1, _translate("submodel", "Known Data", None))
        self.label.setText(_translate("submodel", "Min", None))
        self.label_2.setText(_translate("submodel", "Max", None))
        self.submodel_choosealg.setItemText(0, _translate("submodel", "Choose Algorithm", None))
        self.submodel_choosealg.setItemText(1, _translate("submodel", "PLS", None))
        self.submodel_choosealg.setItemText(2, _translate("submodel", "GP", None))
        self.submodel_choosealg.setItemText(3, _translate("submodel", "Others coming soon...", None))
        self.regression_ransac_checkbox.setText(_translate("submodel", "RANSAC", None))
        self.submodel_trainbutton.setText(_translate("submodel", "Train Submodels", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_unknown_data.ui'
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

class Ui_unknown_data(object):
    def setupUi(self, unknown_data):
        unknown_data.setObjectName(_fromUtf8("unknown_data"))
        unknown_data.resize(362, 164)
        self.horizontalLayout = QtGui.QHBoxLayout(unknown_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unknown_data_label = QtGui.QLabel(unknown_data)
        self.unknown_data_label.setObjectName(_fromUtf8("unknown_data_label"))
        self.horizontalLayout.addWidget(self.unknown_data_label)
        self.unknown_data_line_edit = QtGui.QLineEdit(unknown_data)
        self.unknown_data_line_edit.setReadOnly(True)
        self.unknown_data_line_edit.setObjectName(_fromUtf8("unknown_data_line_edit"))
        self.horizontalLayout.addWidget(self.unknown_data_line_edit)
        self.unknown_data_button = QtGui.QToolButton(unknown_data)
        self.unknown_data_button.setObjectName(_fromUtf8("unknown_data_button"))
        self.horizontalLayout.addWidget(self.unknown_data_button)

        self.retranslateUi(unknown_data)
        QtCore.QMetaObject.connectSlotsByName(unknown_data)

    def retranslateUi(self, unknown_data):
        unknown_data.setWindowTitle(_translate("unknown_data", "GroupBox", None))
        unknown_data.setTitle(_translate("unknown_data", "Unknown Data", None))
        self.unknown_data_label.setText(_translate("unknown_data", "File Name", None))
        self.unknown_data_line_edit.setText(_translate("unknown_data", "*.csv", None))
        self.unknown_data_button.setText(_translate("unknown_data", "...", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\00_mainframe_ok.ui'
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
        self.scrollAreaContents = QtGui.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 561, 742))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaContents.setFont(font)
        self.scrollAreaContents.setStyleSheet(_fromUtf8("QGroupBox {\n"
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
        self.scrollAreaContents.setObjectName(_fromUtf8("scrollAreaContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea.setWidget(self.scrollAreaContents)
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
        self.actionPolyFit = QtGui.QAction(MainWindow)
        self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
        self.actionAirPLS = QtGui.QAction(MainWindow)
        self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
        self.actionFABC = QtGui.QAction(MainWindow)
        self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
        self.actionKK = QtGui.QAction(MainWindow)
        self.actionKK.setObjectName(_fromUtf8("actionKK"))
        self.actionMario = QtGui.QAction(MainWindow)
        self.actionMario.setObjectName(_fromUtf8("actionMario"))
        self.actionMedian = QtGui.QAction(MainWindow)
        self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
        self.actionRubberband = QtGui.QAction(MainWindow)
        self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
        self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
        self.actionRatio = QtGui.QAction(MainWindow)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
        self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName(_fromUtf8("actionPiecewise_Direct_Standardization"))
        self.actionPCA = QtGui.QAction(MainWindow)
        self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
        self.actionICA = QtGui.QAction(MainWindow)
        self.actionICA.setObjectName(_fromUtf8("actionICA"))
        self.actionK_Means = QtGui.QAction(MainWindow)
        self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
        self.actionHierarchical = QtGui.QAction(MainWindow)
        self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
        self.actionOthers = QtGui.QAction(MainWindow)
        self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
        self.actionOthers_2 = QtGui.QAction(MainWindow)
        self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
        self.actionOthers_3 = QtGui.QAction(MainWindow)
        self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
        self.actionPLS = QtGui.QAction(MainWindow)
        self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
        self.actionSM_PLS = QtGui.QAction(MainWindow)
        self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
        self.actionICA_Regression = QtGui.QAction(MainWindow)
        self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
        self.actionGaussian_Process = QtGui.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
        self.actionMLP = QtGui.QAction(MainWindow)
        self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
        self.actionSVM = QtGui.QAction(MainWindow)
        self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
        self.actionOthers_4 = QtGui.QAction(MainWindow)
        self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
        self.actionOthers_5 = QtGui.QAction(MainWindow)
        self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
        self.actionContent_2 = QtGui.QAction(MainWindow)
        self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNormalization = QtGui.QAction(MainWindow)
        self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
        self.actionICA_2 = QtGui.QAction(MainWindow)
        self.actionICA_2.setObjectName(_fromUtf8("actionICA_2"))
        self.actionPCA_2 = QtGui.QAction(MainWindow)
        self.actionPCA_2.setObjectName(_fromUtf8("actionPCA_2"))
        self.actionPLS_DA = QtGui.QAction(MainWindow)
        self.actionPLS_DA.setObjectName(_fromUtf8("actionPLS_DA"))
        self.actionSIMCA = QtGui.QAction(MainWindow)
        self.actionSIMCA.setObjectName(_fromUtf8("actionSIMCA"))
        self.actionK_means = QtGui.QAction(MainWindow)
        self.actionK_means.setObjectName(_fromUtf8("actionK_means"))
        self.actionHierarchical_2 = QtGui.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName(_fromUtf8("actionHierarchical_2"))
        self.actionCross_Validation = QtGui.QAction(MainWindow)
        self.actionCross_Validation.setObjectName(_fromUtf8("actionCross_Validation"))
        self.actionTrain = QtGui.QAction(MainWindow)
        self.actionTrain.setObjectName(_fromUtf8("actionTrain"))
        self.actionPredict = QtGui.QAction(MainWindow)
        self.actionPredict.setObjectName(_fromUtf8("actionPredict"))
        self.actionLine_Plot = QtGui.QAction(MainWindow)
        self.actionLine_Plot.setObjectName(_fromUtf8("actionLine_Plot"))
        self.action1_to_1_Plot = QtGui.QAction(MainWindow)
        self.action1_to_1_Plot.setObjectName(_fromUtf8("action1_to_1_Plot"))
        self.actionScatter_Plot = QtGui.QAction(MainWindow)
        self.actionScatter_Plot.setObjectName(_fromUtf8("actionScatter_Plot"))
        self.actionSet_output_location = QtGui.QAction(MainWindow)
        self.actionSet_output_location.setObjectName(_fromUtf8("actionSet_output_location"))
        self.actionCreate_N_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName(_fromUtf8("actionCreate_N_Folds"))
        self.actionCreate_Test_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName(_fromUtf8("actionCreate_Test_Folds"))
        self.actionSubmodel_Ranges = QtGui.QAction(MainWindow)
        self.actionSubmodel_Ranges.setObjectName(_fromUtf8("actionSubmodel_Ranges"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data", None))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)", None))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
        self.actionALS.setText(_translate("MainWindow", "ALS", None))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
        self.actionFABC.setText(_translate("MainWindow", "FABC", None))
        self.actionKK.setText(_translate("MainWindow", "KK", None))
        self.actionMario.setText(_translate("MainWindow", "Mario", None))
        self.actionMedian.setText(_translate("MainWindow", "Median", None))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
        self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization", None))
        self.actionPCA.setText(_translate("MainWindow", "PCA", None))
        self.actionICA.setText(_translate("MainWindow", "ICA", None))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionOthers.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
        self.actionPLS.setText(_translate("MainWindow", "PLS", None))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
        self.actionMLP.setText(_translate("MainWindow", "MLP", None))
        self.actionSVM.setText(_translate("MainWindow", "SVM", None))
        self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
        self.actionIndex.setText(_translate("MainWindow", "Index", None))
        self.actionContent_2.setText(_translate("MainWindow", "Content", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))
        self.actionICA_2.setText(_translate("MainWindow", "ICA", None))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA", None))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA", None))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA", None))
        self.actionK_means.setText(_translate("MainWindow", "K-means", None))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation", None))
        self.actionTrain.setText(_translate("MainWindow", "Train", None))
        self.actionPredict.setText(_translate("MainWindow", "Predict", None))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot", None))
        self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot", None))
        self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot", None))
        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location", None))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds", None))
        self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds", None))
        self.actionSubmodel_Ranges.setText(_translate("MainWindow", "Submodel Ranges", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_file_out.ui'
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

class Ui_file_out_path(object):
    def setupUi(self, file_out_path):
        file_out_path.setObjectName(_fromUtf8("file_out_path"))
        file_out_path.resize(600, 150)
        file_out_path.setMinimumSize(QtCore.QSize(600, 150))
        file_out_path.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalLayout = QtGui.QHBoxLayout(file_out_path)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_out_path_label = QtGui.QLabel(file_out_path)
        self.file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtGui.QLineEdit(file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtGui.QToolButton(file_out_path)
        self.file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
        self.horizontalLayout.addWidget(self.file_out_path_button)

        self.retranslateUi(file_out_path)
        QtCore.QMetaObject.connectSlotsByName(file_out_path)

    def retranslateUi(self, file_out_path):
        file_out_path.setWindowTitle(_translate("file_out_path", "PCA", None))
        file_out_path.setTitle(_translate("file_out_path", "Output Folder", None))
        self.file_out_path_label.setText(_translate("file_out_path", "File Name", None))
        self.file_out_path_line_edit.setText(_translate("file_out_path", "*/", None))
        self.file_out_path_button.setText(_translate("file_out_path", "...", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_get_mask.ui'
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

class Ui_get_mask(object):
    def setupUi(self, get_mask):
        get_mask.setObjectName(_fromUtf8("get_mask"))
        get_mask.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(get_mask)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_mask_label = QtGui.QLabel(get_mask)
        self.get_mask_label.setObjectName(_fromUtf8("get_mask_label"))
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtGui.QLineEdit(get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName(_fromUtf8("get_mask_line_edit"))
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtGui.QToolButton(get_mask)
        self.get_mask_button.setObjectName(_fromUtf8("get_mask_button"))
        self.horizontalLayout.addWidget(self.get_mask_button)

        self.retranslateUi(get_mask)
        QtCore.QMetaObject.connectSlotsByName(get_mask)

    def retranslateUi(self, get_mask):
        get_mask.setWindowTitle(_translate("get_mask", "GroupBox", None))
        get_mask.setTitle(_translate("get_mask", "Get Mask File", None))
        self.get_mask_label.setText(_translate("get_mask", "File Name", None))
        self.get_mask_line_edit.setText(_translate("get_mask", "*.csv", None))
        self.get_mask_button.setText(_translate("get_mask", "...", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_pca.ui'
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

class Ui_pca(object):
    def setupUi(self, pca):
        pca.setObjectName(_fromUtf8("pca"))
        pca.resize(614, 150)
        pca.setMinimumSize(QtCore.QSize(600, 150))
        pca.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(pca)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pca_vlayout = QtGui.QVBoxLayout()
        self.pca_vlayout.setObjectName(_fromUtf8("pca_vlayout"))
        self.pca_choose_data = QtGui.QComboBox(pca)
        self.pca_choose_data.setObjectName(_fromUtf8("pca_choose_data"))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_choose_data.addItem(_fromUtf8(""))
        self.pca_vlayout.addWidget(self.pca_choose_data)
        self.pca_hlayout = QtGui.QHBoxLayout()
        self.pca_hlayout.setObjectName(_fromUtf8("pca_hlayout"))
        self.pca_nc_label = QtGui.QLabel(pca)
        self.pca_nc_label.setObjectName(_fromUtf8("pca_nc_label"))
        self.pca_hlayout.addWidget(self.pca_nc_label)
        self.pca_nc = QtGui.QSpinBox(pca)
        self.pca_nc.setObjectName(_fromUtf8("pca_nc"))
        self.pca_hlayout.addWidget(self.pca_nc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.pca_hlayout.addItem(spacerItem)
        self.pca_button = QtGui.QPushButton(pca)
        self.pca_button.setObjectName(_fromUtf8("pca_button"))
        self.pca_hlayout.addWidget(self.pca_button)
        self.pca_vlayout.addLayout(self.pca_hlayout)
        self.verticalLayout_2.addLayout(self.pca_vlayout)

        self.retranslateUi(pca)
        QtCore.QMetaObject.connectSlotsByName(pca)

    def retranslateUi(self, pca):
        pca.setWindowTitle(_translate("pca", "PCA", None))
        pca.setTitle(_translate("pca", "PCA", None))
        self.pca_choose_data.setItemText(0, _translate("pca", "Choose Data", None))
        self.pca_choose_data.setItemText(1, _translate("pca", "Known Data", None))
        self.pca_nc_label.setText(_translate("pca", "# of components", None))
        self.pca_button.setText(_translate("pca", "Do PCA", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_pls.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(254, 54)
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 10, 81, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "# of components", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_ransac.ui'
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

class Ui_ransac(object):
    def setupUi(self, ransac):
        ransac.setObjectName(_fromUtf8("ransac"))
        ransac.resize(676, 100)
        ransac.setMinimumSize(QtCore.QSize(600, 100))
        ransac.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ransac)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ransac_vlayout = QtGui.QVBoxLayout()
        self.ransac_vlayout.setObjectName(_fromUtf8("ransac_vlayout"))
        self.ransac_loss_func_hlayout = QtGui.QHBoxLayout()
        self.ransac_loss_func_hlayout.setObjectName(_fromUtf8("ransac_loss_func_hlayout"))
        self.ransac_loss_func = QtGui.QComboBox(ransac)
        self.ransac_loss_func.setObjectName(_fromUtf8("ransac_loss_func"))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func.addItem(_fromUtf8(""))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_loss_func)
        self.ransac_threshold_label = QtGui.QLabel(ransac)
        self.ransac_threshold_label.setObjectName(_fromUtf8("ransac_threshold_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold_label)
        self.ransac_threshold = QtGui.QDoubleSpinBox(ransac)
        self.ransac_threshold.setObjectName(_fromUtf8("ransac_threshold"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_threshold)
        self.ransac_min_label = QtGui.QLabel(ransac)
        self.ransac_min_label.setObjectName(_fromUtf8("ransac_min_label"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min_label)
        self.ransac_min = QtGui.QDoubleSpinBox(ransac)
        self.ransac_min.setObjectName(_fromUtf8("ransac_min"))
        self.ransac_loss_func_hlayout.addWidget(self.ransac_min)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_loss_func_hlayout.addItem(spacerItem)
        self.ransac_vlayout.addLayout(self.ransac_loss_func_hlayout)
        self.verticalLayout_2.addLayout(self.ransac_vlayout)

        self.retranslateUi(ransac)
        QtCore.QMetaObject.connectSlotsByName(ransac)

    def retranslateUi(self, ransac):
        ransac.setWindowTitle(_translate("ransac", "RANSAC", None))
        ransac.setTitle(_translate("ransac", "RANSAC", None))
        self.ransac_loss_func.setItemText(0, _translate("ransac", "Loss Function", None))
        self.ransac_loss_func.setItemText(1, _translate("ransac", "Absolute Error", None))
        self.ransac_loss_func.setItemText(2, _translate("ransac", "Squared Error", None))
        self.ransac_threshold_label.setText(_translate("ransac", "Threshold", None))
        self.ransac_min_label.setText(_translate("ransac", "Minimum samples ", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_regression.ui'
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

class Ui_regression(object):
    def setupUi(self, regression):
        regression.setObjectName(_fromUtf8("regression"))
        regression.resize(644, 525)
        regression.setMinimumSize(QtCore.QSize(600, 150))
        regression.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtGui.QVBoxLayout(regression)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.regression_vlayout = QtGui.QVBoxLayout()
        self.regression_vlayout.setObjectName(_fromUtf8("regression_vlayout"))
        self.regression_choosedata_hlayout = QtGui.QHBoxLayout()
        self.regression_choosedata_hlayout.setObjectName(_fromUtf8("regression_choosedata_hlayout"))
        self.label = QtGui.QLabel(regression)
        self.label.setObjectName(_fromUtf8("label"))
        self.regression_choosedata_hlayout.addWidget(self.label)
        self.regression_choosedata = QtGui.QComboBox(regression)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
        self.regression_choosedata.addItem(_fromUtf8(""))
        self.regression_choosedata.addItem(_fromUtf8(""))
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        self.regression_choosevars_hlayout = QtGui.QHBoxLayout()
        self.regression_choosevars_hlayout.setObjectName(_fromUtf8("regression_choosevars_hlayout"))
        self.regression_train_choosex_label = QtGui.QLabel(regression)
        self.regression_train_choosex_label.setObjectName(_fromUtf8("regression_train_choosex_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex_label)
        self.regression_train_choosex = QtGui.QListWidget(regression)
        self.regression_train_choosex.setObjectName(_fromUtf8("regression_train_choosex"))
        item = QtGui.QListWidgetItem()
        self.regression_train_choosex.addItem(item)
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex)
        self.regression_train_choosey_label = QtGui.QLabel(regression)
        self.regression_train_choosey_label.setObjectName(_fromUtf8("regression_train_choosey_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey_label)
        self.regression_train_choosey = QtGui.QListWidget(regression)
        self.regression_train_choosey.setObjectName(_fromUtf8("regression_train_choosey"))
        item = QtGui.QListWidgetItem()
        self.regression_train_choosey.addItem(item)
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosevars_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosevars_hlayout)
        self.regression_choosealg_hlayout = QtGui.QHBoxLayout()
        self.regression_choosealg_hlayout.setObjectName(_fromUtf8("regression_choosealg_hlayout"))
        self.regression_choosealg_label = QtGui.QLabel(regression)
        self.regression_choosealg_label.setObjectName(_fromUtf8("regression_choosealg_label"))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_choosealg = QtGui.QComboBox(regression)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName(_fromUtf8("regression_choosealg"))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg.addItem(_fromUtf8(""))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(spacerItem2)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.pls_widget = QtGui.QWidget(regression)
        self.pls_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.pls_widget.setObjectName(_fromUtf8("pls_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.pls_widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pls_nc_label = QtGui.QLabel(self.pls_widget)
        self.pls_nc_label.setObjectName(_fromUtf8("pls_nc_label"))
        self.horizontalLayout_2.addWidget(self.pls_nc_label)
        self.pls_nc_spinbox = QtGui.QSpinBox(self.pls_widget)
        self.pls_nc_spinbox.setObjectName(_fromUtf8("pls_nc_spinbox"))
        self.horizontalLayout_2.addWidget(self.pls_nc_spinbox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.regression_vlayout.addWidget(self.pls_widget)
        self.gp_widget = QtGui.QWidget(regression)
        self.gp_widget.setObjectName(_fromUtf8("gp_widget"))
        self.gp_vlayout = QtGui.QVBoxLayout(self.gp_widget)
        self.gp_vlayout.setObjectName(_fromUtf8("gp_vlayout"))
        self.gp_dim_red_hlayout = QtGui.QHBoxLayout()
        self.gp_dim_red_hlayout.setObjectName(_fromUtf8("gp_dim_red_hlayout"))
        self.gp_dim_red_label = QtGui.QLabel(self.gp_widget)
        self.gp_dim_red_label.setObjectName(_fromUtf8("gp_dim_red_label"))
        self.gp_dim_red_hlayout.addWidget(self.gp_dim_red_label)
        self.gp_dim_red_combobox = QtGui.QComboBox(self.gp_widget)
        self.gp_dim_red_combobox.setObjectName(_fromUtf8("gp_dim_red_combobox"))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_combobox.addItem(_fromUtf8(""))
        self.gp_dim_red_hlayout.addWidget(self.gp_dim_red_combobox)
        self.gp_vlayout.addLayout(self.gp_dim_red_hlayout)
        self.gp_rand_starts_hlayout = QtGui.QHBoxLayout()
        self.gp_rand_starts_hlayout.setObjectName(_fromUtf8("gp_rand_starts_hlayout"))
        self.gp_rand_starts_label = QtGui.QLabel(self.gp_widget)
        self.gp_rand_starts_label.setObjectName(_fromUtf8("gp_rand_starts_label"))
        self.gp_rand_starts_hlayout.addWidget(self.gp_rand_starts_label)
        self.gp_rand_starts_spin = QtGui.QSpinBox(self.gp_widget)
        self.gp_rand_starts_spin.setObjectName(_fromUtf8("gp_rand_starts_spin"))
        self.gp_rand_starts_hlayout.addWidget(self.gp_rand_starts_spin)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gp_rand_starts_hlayout.addItem(spacerItem4)
        self.gp_vlayout.addLayout(self.gp_rand_starts_hlayout)
        self.gp_theta_hlayout = QtGui.QHBoxLayout()
        self.gp_theta_hlayout.setObjectName(_fromUtf8("gp_theta_hlayout"))
        self.gp_theta0_label = QtGui.QLabel(self.gp_widget)
        self.gp_theta0_label.setObjectName(_fromUtf8("gp_theta0_label"))
        self.gp_theta_hlayout.addWidget(self.gp_theta0_label)
        self.gp_theta0_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_theta0_spin.setObjectName(_fromUtf8("gp_theta0_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_theta0_spin)
        self.gp_thetaL_label = QtGui.QLabel(self.gp_widget)
        self.gp_thetaL_label.setObjectName(_fromUtf8("gp_thetaL_label"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaL_label)
        self.gp_thetaL_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_thetaL_spin.setObjectName(_fromUtf8("gp_thetaL_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaL_spin)
        self.gp_thetaU_label = QtGui.QLabel(self.gp_widget)
        self.gp_thetaU_label.setObjectName(_fromUtf8("gp_thetaU_label"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaU_label)
        self.gp_thetaU_spin = QtGui.QDoubleSpinBox(self.gp_widget)
        self.gp_thetaU_spin.setObjectName(_fromUtf8("gp_thetaU_spin"))
        self.gp_theta_hlayout.addWidget(self.gp_thetaU_spin)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gp_theta_hlayout.addItem(spacerItem5)
        self.gp_vlayout.addLayout(self.gp_theta_hlayout)
        self.regression_vlayout.addWidget(self.gp_widget)
        self.regression_ransac_checkbox = QtGui.QCheckBox(regression)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.regression_vlayout.addWidget(self.regression_ransac_checkbox)
        self.ransac_vlayout = QtGui.QVBoxLayout()
        self.ransac_vlayout.setObjectName(_fromUtf8("ransac_vlayout"))
        self.ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
        self.ransac_lossfunc_hlayout.setObjectName(_fromUtf8("ransac_lossfunc_hlayout"))
        self.ransac_lossfunc_label = QtGui.QLabel(regression)
        self.ransac_lossfunc_label.setObjectName(_fromUtf8("ransac_lossfunc_label"))
        self.ransac_lossfunc_hlayout.addWidget(self.ransac_lossfunc_label)
        self.ransac_lossfunc_combobox = QtGui.QComboBox(regression)
        self.ransac_lossfunc_combobox.setObjectName(_fromUtf8("ransac_lossfunc_combobox"))
        self.ransac_lossfunc_combobox.addItem(_fromUtf8(""))
        self.ransac_lossfunc_combobox.addItem(_fromUtf8(""))
        self.ransac_lossfunc_hlayout.addWidget(self.ransac_lossfunc_combobox)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_lossfunc_hlayout.addItem(spacerItem6)
        self.ransac_vlayout.addLayout(self.ransac_lossfunc_hlayout)
        self.ransac_thresh_hlayout = QtGui.QHBoxLayout()
        self.ransac_thresh_hlayout.setObjectName(_fromUtf8("ransac_thresh_hlayout"))
        self.ransac_thresh_label = QtGui.QLabel(regression)
        self.ransac_thresh_label.setObjectName(_fromUtf8("ransac_thresh_label"))
        self.ransac_thresh_hlayout.addWidget(self.ransac_thresh_label)
        self.ransac_thresh_spin = QtGui.QDoubleSpinBox(regression)
        self.ransac_thresh_spin.setObjectName(_fromUtf8("ransac_thresh_spin"))
        self.ransac_thresh_hlayout.addWidget(self.ransac_thresh_spin)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ransac_thresh_hlayout.addItem(spacerItem7)
        self.ransac_vlayout.addLayout(self.ransac_thresh_hlayout)
        self.regression_vlayout.addLayout(self.ransac_vlayout)
        self.regression_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.regression_trainbutton_hlayout.setObjectName(_fromUtf8("regression_trainbutton_hlayout"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_trainbutton_hlayout.addItem(spacerItem8)
        self.regression_trainbutton = QtGui.QPushButton(regression)
        self.regression_trainbutton.setObjectName(_fromUtf8("regression_trainbutton"))
        self.regression_trainbutton_hlayout.addWidget(self.regression_trainbutton)
        self.regression_vlayout.addLayout(self.regression_trainbutton_hlayout)
        self.verticalLayout_2.addLayout(self.regression_vlayout)

        self.retranslateUi(regression)
        QtCore.QMetaObject.connectSlotsByName(regression)

    def retranslateUi(self, regression):
        regression.setWindowTitle(_translate("regression", "Regression", None))
        regression.setTitle(_translate("regression", "Regression", None))
        self.label.setText(_translate("regression", "Choose data: ", None))
        self.regression_choosedata.setItemText(0, _translate("regression", "Choose Data", None))
        self.regression_choosedata.setItemText(1, _translate("regression", "Known Data", None))
        self.regression_train_choosex_label.setText(_translate("regression", "Choose X variable(s): ", None))
        __sortingEnabled = self.regression_train_choosex.isSortingEnabled()
        self.regression_train_choosex.setSortingEnabled(False)
        item = self.regression_train_choosex.item(0)
        item.setText(_translate("regression", "Choose X", None))
        self.regression_train_choosex.setSortingEnabled(__sortingEnabled)
        self.regression_train_choosey_label.setText(_translate("regression", "Choose Y variable(s):", None))
        __sortingEnabled = self.regression_train_choosey.isSortingEnabled()
        self.regression_train_choosey.setSortingEnabled(False)
        item = self.regression_train_choosey.item(0)
        item.setText(_translate("regression", "Choose Y", None))
        self.regression_train_choosey.setSortingEnabled(__sortingEnabled)
        self.regression_choosealg_label.setText(_translate("regression", "Choose Algorithm: ", None))
        self.regression_choosealg.setItemText(0, _translate("regression", "PLS", None))
        self.regression_choosealg.setItemText(1, _translate("regression", "GP", None))
        self.regression_choosealg.setItemText(2, _translate("regression", "Others coming soon...", None))
        self.pls_nc_label.setText(_translate("regression", "# of Components: ", None))
        self.gp_dim_red_label.setText(_translate("regression", "Dimensionality reduction method:", None))
        self.gp_dim_red_combobox.setItemText(0, _translate("regression", "PCA", None))
        self.gp_dim_red_combobox.setItemText(1, _translate("regression", "FastICA", None))
        self.gp_dim_red_combobox.setItemText(2, _translate("regression", "ICA - JADE", None))
        self.gp_dim_red_combobox.setItemText(3, _translate("regression", "None", None))
        self.gp_rand_starts_label.setText(_translate("regression", "# of random starts:", None))
        self.gp_theta0_label.setText(_translate("regression", "theta_0", None))
        self.gp_thetaL_label.setText(_translate("regression", "theta_L", None))
        self.gp_thetaU_label.setText(_translate("regression", "theta_U", None))
        self.regression_ransac_checkbox.setText(_translate("regression", "RANSAC", None))
        self.ransac_lossfunc_label.setText(_translate("regression", "Loss function:", None))
        self.ransac_lossfunc_combobox.setItemText(0, _translate("regression", "Squared", None))
        self.ransac_lossfunc_combobox.setItemText(1, _translate("regression", "Absolute", None))
        self.ransac_thresh_label.setText(_translate("regression", "Threshold:", None))
        self.regression_trainbutton.setText(_translate("regression", "Train", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_strat_folds.ui'
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

class Ui_strat_folds(object):
    def setupUi(self, strat_folds):
        strat_folds.setObjectName(_fromUtf8("strat_folds"))
        strat_folds.resize(602, 150)
        strat_folds.setMinimumSize(QtCore.QSize(600, 150))
        strat_folds.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalLayout_2 = QtGui.QVBoxLayout(strat_folds)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.strat_folds_vlayout = QtGui.QVBoxLayout()
        self.strat_folds_vlayout.setObjectName(_fromUtf8("strat_folds_vlayout"))
        self.strat_folds_choose_data = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_data.setObjectName(_fromUtf8("strat_folds_choose_data"))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_choose_data.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_data)
        self.strat_folds_choose_element = QtGui.QComboBox(strat_folds)
        self.strat_folds_choose_element.setObjectName(_fromUtf8("strat_folds_choose_element"))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_choose_element.addItem(_fromUtf8(""))
        self.strat_folds_vlayout.addWidget(self.strat_folds_choose_element)
        self.strat_folds_hlayout = QtGui.QHBoxLayout()
        self.strat_folds_hlayout.setObjectName(_fromUtf8("strat_folds_hlayout"))
        self.nfolds_label = QtGui.QLabel(strat_folds)
        self.nfolds_label.setObjectName(_fromUtf8("nfolds_label"))
        self.strat_folds_hlayout.addWidget(self.nfolds_label)
        self.nfolds_spin = QtGui.QSpinBox(strat_folds)
        self.nfolds_spin.setObjectName(_fromUtf8("nfolds_spin"))
        self.strat_folds_hlayout.addWidget(self.nfolds_spin)
        self.test_fold_label = QtGui.QLabel(strat_folds)
        self.test_fold_label.setObjectName(_fromUtf8("test_fold_label"))
        self.strat_folds_hlayout.addWidget(self.test_fold_label)
        self.test_fold_spin = QtGui.QSpinBox(strat_folds)
        self.test_fold_spin.setObjectName(_fromUtf8("test_fold_spin"))
        self.strat_folds_hlayout.addWidget(self.test_fold_spin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.strat_folds_hlayout.addItem(spacerItem)
        self.create_folds = QtGui.QPushButton(strat_folds)
        self.create_folds.setObjectName(_fromUtf8("create_folds"))
        self.strat_folds_hlayout.addWidget(self.create_folds)
        self.strat_folds_vlayout.addLayout(self.strat_folds_hlayout)
        self.verticalLayout_2.addLayout(self.strat_folds_vlayout)

        self.retranslateUi(strat_folds)
        QtCore.QMetaObject.connectSlotsByName(strat_folds)

    def retranslateUi(self, strat_folds):
        strat_folds.setWindowTitle(_translate("strat_folds", "Stratified Folds", None))
        strat_folds.setTitle(_translate("strat_folds", "Stratified Folds", None))
        self.strat_folds_choose_data.setItemText(0, _translate("strat_folds", "Choose Data", None))
        self.strat_folds_choose_data.setItemText(1, _translate("strat_folds", "Unknown Data", None))
        self.strat_folds_choose_data.setItemText(2, _translate("strat_folds", "Known Data", None))
        self.strat_folds_choose_element.setItemText(0, _translate("strat_folds", "Choose Element to Stratify On", None))
        self.strat_folds_choose_element.setItemText(1, _translate("strat_folds", "SiO2", None))
        self.strat_folds_choose_element.setItemText(2, _translate("strat_folds", "TiO2", None))
        self.strat_folds_choose_element.setItemText(3, _translate("strat_folds", "Al2O3", None))
        self.strat_folds_choose_element.setItemText(4, _translate("strat_folds", "FeOT", None))
        self.strat_folds_choose_element.setItemText(5, _translate("strat_folds", "MgO", None))
        self.strat_folds_choose_element.setItemText(6, _translate("strat_folds", "CaO", None))
        self.strat_folds_choose_element.setItemText(7, _translate("strat_folds", "Na2O", None))
        self.strat_folds_choose_element.setItemText(8, _translate("strat_folds", "K2O", None))
        self.nfolds_label.setText(_translate("strat_folds", "N folds", None))
        self.test_fold_label.setText(_translate("strat_folds", "Test Fold", None))
        self.create_folds.setText(_translate("strat_folds", "Create Folds", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_submodel.ui'
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

class Ui_submodel(object):
    def setupUi(self, submodel):
        submodel.setObjectName(_fromUtf8("submodel"))
        submodel.resize(644, 238)
        submodel.setMinimumSize(QtCore.QSize(600, 150))
        submodel.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.verticalLayout_2 = QtGui.QVBoxLayout(submodel)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.submodel_vlayout = QtGui.QVBoxLayout()
        self.submodel_vlayout.setObjectName(_fromUtf8("submodel_vlayout"))
        self.submodel_choosedata_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosedata_hlayout.setObjectName(_fromUtf8("submodel_choosedata_hlayout"))
        self.submodel_choosedata = QtGui.QComboBox(submodel)
        self.submodel_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosedata.setObjectName(_fromUtf8("submodel_choosedata"))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata.addItem(_fromUtf8(""))
        self.submodel_choosedata_hlayout.addWidget(self.submodel_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosedata_hlayout.addItem(spacerItem)
        self.submodel_vlayout.addLayout(self.submodel_choosedata_hlayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(submodel)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(submodel)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(submodel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(submodel)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.submodel_vlayout.addLayout(self.horizontalLayout)
        self.submodel_choosealg_hlayout = QtGui.QHBoxLayout()
        self.submodel_choosealg_hlayout.setObjectName(_fromUtf8("submodel_choosealg_hlayout"))
        self.submodel_choosealg = QtGui.QComboBox(submodel)
        self.submodel_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.submodel_choosealg.setObjectName(_fromUtf8("submodel_choosealg"))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg.addItem(_fromUtf8(""))
        self.submodel_choosealg_hlayout.addWidget(self.submodel_choosealg)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_choosealg_hlayout.addItem(spacerItem2)
        self.submodel_vlayout.addLayout(self.submodel_choosealg_hlayout)
        self.regression_ransac_checkbox = QtGui.QCheckBox(submodel)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.submodel_vlayout.addWidget(self.regression_ransac_checkbox)
        self.submodel_trainbutton_hlayout = QtGui.QHBoxLayout()
        self.submodel_trainbutton_hlayout.setObjectName(_fromUtf8("submodel_trainbutton_hlayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.submodel_trainbutton_hlayout.addItem(spacerItem3)
        self.submodel_trainbutton = QtGui.QPushButton(submodel)
        self.submodel_trainbutton.setObjectName(_fromUtf8("submodel_trainbutton"))
        self.submodel_trainbutton_hlayout.addWidget(self.submodel_trainbutton)
        self.submodel_vlayout.addLayout(self.submodel_trainbutton_hlayout)
        self.verticalLayout_2.addLayout(self.submodel_vlayout)

        self.retranslateUi(submodel)
        QtCore.QMetaObject.connectSlotsByName(submodel)

    def retranslateUi(self, submodel):
        submodel.setWindowTitle(_translate("submodel", "Regression", None))
        submodel.setTitle(_translate("submodel", "Regression", None))
        self.submodel_choosedata.setItemText(0, _translate("submodel", "Choose Data", None))
        self.submodel_choosedata.setItemText(1, _translate("submodel", "Known Data", None))
        self.label.setText(_translate("submodel", "Min", None))
        self.label_2.setText(_translate("submodel", "Max", None))
        self.submodel_choosealg.setItemText(0, _translate("submodel", "Choose Algorithm", None))
        self.submodel_choosealg.setItemText(1, _translate("submodel", "PLS", None))
        self.submodel_choosealg.setItemText(2, _translate("submodel", "GP", None))
        self.submodel_choosealg.setItemText(3, _translate("submodel", "Others coming soon...", None))
        self.regression_ransac_checkbox.setText(_translate("submodel", "RANSAC", None))
        self.submodel_trainbutton.setText(_translate("submodel", "Train Submodels", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\01_mainwindow_unknown_data.ui'
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

class Ui_unknown_data(object):
    def setupUi(self, unknown_data):
        unknown_data.setObjectName(_fromUtf8("unknown_data"))
        unknown_data.resize(362, 164)
        self.horizontalLayout = QtGui.QHBoxLayout(unknown_data)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unknown_data_label = QtGui.QLabel(unknown_data)
        self.unknown_data_label.setObjectName(_fromUtf8("unknown_data_label"))
        self.horizontalLayout.addWidget(self.unknown_data_label)
        self.unknown_data_line_edit = QtGui.QLineEdit(unknown_data)
        self.unknown_data_line_edit.setReadOnly(True)
        self.unknown_data_line_edit.setObjectName(_fromUtf8("unknown_data_line_edit"))
        self.horizontalLayout.addWidget(self.unknown_data_line_edit)
        self.unknown_data_button = QtGui.QToolButton(unknown_data)
        self.unknown_data_button.setObjectName(_fromUtf8("unknown_data_button"))
        self.horizontalLayout.addWidget(self.unknown_data_button)

        self.retranslateUi(unknown_data)
        QtCore.QMetaObject.connectSlotsByName(unknown_data)

    def retranslateUi(self, unknown_data):
        unknown_data.setWindowTitle(_translate("unknown_data", "GroupBox", None))
        unknown_data.setTitle(_translate("unknown_data", "Unknown Data", None))
        self.unknown_data_label.setText(_translate("unknown_data", "File Name", None))
        self.unknown_data_line_edit.setText(_translate("unknown_data", "*.csv", None))
        self.unknown_data_button.setText(_translate("unknown_data", "...", None))

# -*- coding: utf-8 -*-

# Form implementation generated fr