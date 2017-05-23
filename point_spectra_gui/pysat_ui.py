from PyQt5 import QtGui, QtCore, QtWidgets, QtGui
from point_spectra_gui import ui_modules
from point_spectra_gui.pysat_func import pysat_func
import pickle


class pysat_ui(object):
    def __init__(self):
        self.pysat_fun = pysat_func()
        self.ui_list = []
        self.restore_list = None
        self.flag = False
        self.restore_flag = False

    """ =============================================
    This is the backbone of the UI, without this portion we have nothing to work with
    ============================================== """

    def main_window(self, MainWindow):
        MainWindow.setObjectName(("MainWindow"))
        MainWindow.resize(800, 1000)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName(("centralWidget"))
        self.scrollarea_layout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.scrollarea_layout.setContentsMargins(11, 11, 11, 11)
        self.scrollarea_layout.setSpacing(6)
        self.scrollarea_layout.setObjectName(("scrollarea_layout"))
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 557, 800))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setStyleSheet(("QGroupBox {\n"
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
        self.scrollAreaWidgetContents_2.setObjectName(("scrollAreaWidgetContents_2"))
        self.module_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.module_layout.setContentsMargins(11, 11, 11, 11)
        self.module_layout.setSpacing(6)
        self.module_layout.setObjectName(("module_layout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollarea_layout.addWidget(self.scrollArea)
        self.OK = QtWidgets.QGroupBox(self.centralWidget)
        self.OK.setObjectName(("OK"))
        self.ok = QtWidgets.QHBoxLayout(self.OK)
        self.ok.setContentsMargins(11, 11, 11, 11)
        self.ok.setSpacing(6)
        self.ok.setObjectName(("ok"))
        self.progressBar = QtWidgets.QProgressBar(self.OK)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(("progressBar"))
        self.ok.addWidget(self.progressBar)
        self.delButton = QtWidgets.QPushButton(self.OK)
        self.okButton = QtWidgets.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.delButton.setFont(font)
        self.delButton.setMouseTracking(False)
        self.delButton.setObjectName("delButton")
        self.ok.addWidget(self.delButton)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName(("okButton"))
        self.ok.addWidget(self.okButton)
        self.scrollarea_layout.addWidget(self.OK)

        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName(("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menuBar.setObjectName(("menuBar"))
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName(("menuFile"))
        self.menuPreprocessing = QtWidgets.QMenu(self.menuBar)
        self.menuPreprocessing.setObjectName(("menuPreprocessing"))
        self.menuRegression = QtWidgets.QMenu(self.menuBar)
        self.menuRegression.setObjectName(("menuRegression"))
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName(("menuHelp"))
        self.menuVisualization = QtWidgets.QMenu(self.menuBar)
        self.menuVisualization.setObjectName(("menuVisualization"))
        MainWindow.setMenuBar(self.menuBar)

        # set up data actions
        self.actionRead_ccam = QtWidgets.QAction(MainWindow)
        self.actionRead_ccam.setObjectName(("actionRead_ccam"))
        self.actionLoadData = QtWidgets.QAction(MainWindow)
        self.actionLoadData.setObjectName(("actionLoadData"))
        self.actionSave_Current_Workflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName(("actionSave_Current_Workflow"))
        self.actionSave_Current_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName(("actionSave_Current_Data"))
        self.actionCreate_New_Workflow = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName(("actionCreate_New_Workflow"))
        self.actionOpen_Workflow = QtWidgets.QAction(MainWindow)
        self.actionOpen_Workflow.setObjectName(("actionOpen_Workflow"))
        self.actionSet_output_location = QtWidgets.QAction(MainWindow)
        self.actionSet_output_location.setObjectName(("actionSet_output_location"))

        # set up preprocessing actions
        self.actionRemoveNull = QtWidgets.QAction(MainWindow)
        self.actionRemoveNull.setObjectName(("actionRemoveNull"))
        self.actionApply_Mask = QtWidgets.QAction(MainWindow)
        self.actionApply_Mask.setObjectName(("actionApply_Mask"))
        self.actionMultiply_Vector = QtWidgets.QAction(MainWindow)
        self.actionMultiply_Vector.setObjectName(("actionMultiply_Vector"))
        self.actionInterpolate = QtWidgets.QAction(MainWindow)
        self.actionInterpolate.setObjectName(("actionInterpolate"))
        self.actionStratified_Folds = QtWidgets.QAction(MainWindow)
        self.actionStratified_Folds.setObjectName(("actionStratified_Folds"))
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName(("actionAbout"))
        self.actionAbout_QtCreator = QtWidgets.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(("actionAbout_QtCreator"))
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName(("actionExit"))
        self.actionNormalization = QtWidgets.QAction(MainWindow)
        self.actionNormalization.setObjectName(("actionNormalization"))
        self.actionDimRed = QtWidgets.QAction(MainWindow)
        self.actionDimRed.setObjectName(("actionDimRed"))

        # set up regression actions
        self.actionCross_Validation = QtWidgets.QAction(MainWindow)
        self.actionCross_Validation.setObjectName(("actionCross_Validation"))
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName(("actionTrain"))
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName(("actionPredict"))

        # set up plotting actions
        self.actionPlot = QtWidgets.QAction(MainWindow)
        self.actionPlot.setObjectName(("actionPlot"))
        self.actionPlotSpect = QtWidgets.QAction(MainWindow)
        self.actionPlotSpect.setObjectName(("actionPlotSpect"))


        self.actionPlotDimRed = QtWidgets.QAction(MainWindow)
        self.actionPlotDimRed.setObjectName(("actionPlot"))

        self.actionTrain_Submodels = QtWidgets.QAction(MainWindow)
        self.actionTrain_Submodels.setObjectName(("actionTrain_Submodels"))
        self.actionSubmodelPredict = QtWidgets.QAction(MainWindow)
        self.actionSubmodelPredict.setObjectName(("actionSubmodelPredict"))

        # add actions to file menu
        self.menuFile.addAction(self.actionRead_ccam)
        self.menuFile.addAction(self.actionLoadData)
        self.menuFile.addAction(self.actionSet_output_location)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
        self.menuFile.addAction(self.actionOpen_Workflow)
        self.menuFile.addAction(self.actionSave_Current_Workflow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        # add actions to preprocessing
        self.menuPreprocessing.addAction(self.actionRemoveNull)
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionApply_Mask)
        self.menuPreprocessing.addAction(self.actionMultiply_Vector)
        self.menuPreprocessing.addAction(self.actionNormalization)
        self.menuPreprocessing.addAction(self.actionDimRed)
        self.menuPreprocessing.addAction(self.actionStratified_Folds)

        # add actions to regression menu
        self.menuRegression.addAction(self.actionCross_Validation)
        self.menuRegression.addAction(self.actionTrain)
        self.menuRegression.addAction(self.actionSubmodelPredict)
        self.menuRegression.addAction(self.actionPredict)

        # add actions to help menu
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_QtCreator)

        # add actions to plot menu
        self.menuVisualization.addAction(self.actionPlot)
        self.menuVisualization.addAction(self.actionPlotSpect)
        self.menuVisualization.addAction(self.actionPlotDimRed)

        # add menu actions
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreprocessing.menuAction())
        self.menuBar.addAction(self.menuRegression.menuAction())
        self.menuBar.addAction(self.menuVisualization.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle("PYSAT")
        self.okButton.setText("OK")
        self.delButton.setText("Delete Module")
        self.menuFile.setTitle("File")
        self.menuPreprocessing.setTitle("Preprocessing")
        self.menuRegression.setTitle("Regression")
        self.menuHelp.setTitle("Help")
        self.menuVisualization.setTitle("Visualization")
        self.actionRead_ccam.setText("Read ChemCam Data")
        self.actionLoadData.setText("Load Data")
        self.actionSave_Current_Workflow.setText("Save Current Workflow")
        self.actionSave_Current_Data.setText("Save Current Data")
        self.actionCreate_New_Workflow.setText("Create New Workflow")
        self.actionOpen_Workflow.setText("Restore Workflow")
        self.actionApply_Mask.setText("Apply Mask")
        self.actionMultiply_Vector.setText("Multiply by Vector")
        self.actionInterpolate.setText("Interpolate")
        self.actionRemoveNull.setText("Remove Null Data")
        self.actionDimRed.setText(("Dimensionality Reduction"))
        self.actionAbout.setText("About...")
        self.actionAbout_QtCreator.setText("About Qt...")
        self.actionExit.setText("Exit")
        self.actionNormalization.setText("Normalization")
        self.actionCross_Validation.setText("Cross Validation")
        self.actionTrain.setText("Train")
        self.actionSubmodelPredict.setText("Submodel Predict")
        self.actionPredict.setText("Predict")
        self.actionPlot.setText("Plot")
        self.actionPlotSpect.setText("Plot Spectra")
        self.actionPlotDimRed.setText("Plot ICA/PCA")

        self.actionSet_output_location.setText("Set Output Path")

        self.actionStratified_Folds.setText("Stratified Folds")
        self.okButton.clicked.connect(lambda: self.on_okButton_clicked())
        self.delButton.clicked.connect(lambda: self.pysat_fun.del_layout())

    def do_get_data(self, arg_list=None, kw_list=None):
        self.flag = ui_modules.get_data_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_read_ccam(self, arg_list=None, kw_list=None):
        self.flag = ui_modules.read_ccam_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_mask(self, arg_list=None, kw_list=None):
        ui_modules.get_mask_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_multiply_vector(self, arg_list=None, kw_list=None):
        ui_modules.multiply_vector_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_write_data(self):
        self.flag = ui_modules.write_data_(self.pysat_fun, self.module_layout)

    def file_outpath(self, arg_list=None, kw_list=None):
        self.flag = ui_modules.file_outpath_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_removenull(self, arg_list=None, kw_list=None):
        ui_modules.removenull_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def normalization(self, arg_list=None, kw_list=None):
        ui_modules.normalization_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_strat_folds(self, arg_list=None, kw_list=None):
        ui_modules.strat_folds_(self.pysat_fun, self.module_layout, arg_list, kw_list)
    def do_dim_red(self, arg_list=None, kw_list=None):
        ui_modules.dim_reduction_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_regression_train(self, arg_list=None, kw_list=None):
        ui_modules.regression_train_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_regression_predict(self, arg_list=None, kw_list=None):
        ui_modules.regression_predict_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_submodel_predict(self, arg_list=None, kw_list=None):
        ui_modules.sm_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_plot(self, arg_list=None, kw_list=None):
        ui_modules.plot_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_plot_spect(self, arg_list=None, kw_list=None):
        ui_modules.plot_spectra_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_plot_dim_red(self, arg_list=None, kw_list=None):
        ui_modules.dim_red_plot_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_cv(self, arg_list=None, kw_list=None):
        ui_modules.cv_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    def do_interp(self, arg_list=None, kw_list=None):
        ui_modules.interpolation_(self.pysat_fun, self.module_layout, arg_list, kw_list)

    """ =============================================
    Please do not delete the functions below this line!
    These functions are the working functions
    that allow the UI to operate and do work!
    ============================================== """

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")

    def menu_item_functions(self, MainWindow):
        self.actionRead_ccam.triggered.connect(lambda: pysat_ui.do_read_ccam(self))
        self.actionSet_output_location.triggered.connect(lambda: pysat_ui.file_outpath(self))  # output location
        self.actionLoadData.triggered.connect(lambda: pysat_ui.do_get_data(self))  # load data
        self.actionSave_Current_Data.triggered.connect(lambda: pysat_ui.do_write_data(self))
        self.actionNormalization.triggered.connect(lambda: pysat_ui.normalization(self))  # submodel
        self.actionApply_Mask.triggered.connect(lambda: pysat_ui.do_mask(self))  # get_mask
        self.actionMultiply_Vector.triggered.connect(lambda: pysat_ui.do_multiply_vector(self))  # multiply by vector
        self.actionRemoveNull.triggered.connect(lambda: pysat_ui.do_removenull(self))
        self.actionStratified_Folds.triggered.connect(lambda: pysat_ui.do_strat_folds(self))  # strat folds
        self.actionStratified_Folds.triggered.connect(lambda: self.actionCross_Validation.setDisabled(False))
        self.actionTrain.triggered.connect(lambda: pysat_ui.do_regression_train(self))  # regression train
        self.actionPredict.triggered.connect(lambda: pysat_ui.do_regression_predict(self))  # regression predict
        self.actionInterpolate.triggered.connect(lambda: pysat_ui.do_interp(self))
        self.actionPlot.triggered.connect(lambda: pysat_ui.do_plot(self))
        self.actionPlotSpect.triggered.connect(lambda: pysat_ui.do_plot_spect(self))
        self.actionPlotDimRed.triggered.connect(lambda: pysat_ui.do_plot_dim_red(self))
        self.actionCross_Validation.triggered.connect(lambda: pysat_ui.do_cv(self))
        self.actionSubmodelPredict.triggered.connect(lambda: pysat_ui.do_submodel_predict(self))
        self.actionDimRed.triggered.connect(lambda: pysat_ui.do_dim_red(self))
        self.actionOpen_Workflow.triggered.connect(lambda: self.on_load_clicked())
        self.actionSave_Current_Workflow.triggered.connect(lambda: self.on_save_clicked())
        self.set_greyed_out_items(True)
        self.actionCross_Validation.setDisabled(True)

    #        self.set_visible_items()

    # TODO add auto scroll down feature
    # self.scrollArea.findChildren().triggered.connect(self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().value()+10))

    # These are the Restore functions
    # self.actionRemoveNull.triggered.connect(lambda: self.set_ui_list("do_removenull"))
    # self.actionPredict.triggered.connect(lambda: self.set_ui_list("do_regression_predict"))  # regression predict
    # self.actionPlot.triggered.connect(lambda: self.set_ui_list("do_plot"))
    # self.actionCross_Validation.triggered.connect(lambda: self.set_ui_list("do_cv"))

    def set_greyed_out_items(self, bool):
        self.actionTrain.setDisabled(bool)
        self.actionPredict.setDisabled(bool)
        self.actionNormalization.setDisabled(bool)
        self.actionApply_Mask.setDisabled(bool)
        self.actionMultiply_Vector.setDisabled(bool)
        self.actionStratified_Folds.setDisabled(bool)
        self.actionTrain.setDisabled(bool)
        self.actionPredict.setDisabled(bool)
        self.actionInterpolate.setDisabled(bool)
        self.actionPlot.setDisabled(bool)
        self.actionPlotSpect.setDisabled(bool)
        self.actionRemoveNull.setDisabled(bool)
        #self.actionCross_Validation.setDisabled(bool)
        self.actionSubmodelPredict.setDisabled(bool)
        self.actionSave_Current_Data.setDisabled(bool)
        self.actionDimRed.setDisabled(bool)
        self.actionPlotDimRed.setDisabled(bool)

    #    def set_visible_items(self):
    #    def set_visible_items(self):
    # self.actionNoise_Reduction.setVisible(False)
    # self.actionInstrument_Response.setVisible(False)
    # self.menuBaseline_Removal.deleteLater()
    # self.menuCalibration_Transfer.deleteLater()
    # self.actionICA.setVisible(False)
    # self.actionPCA.setVisible(False)
    # self.actionICA_2.setVisible(False)
    # self.actionPCA_2.setVisible(False)
    # self.menuClassification.setTitle("")

    def handleMenuHovered(self, action):
        QtWidgets.QToolTip.showText(self, None, action, None)

    def on_okButton_clicked(self):
        if self.flag:
            self.set_greyed_out_items(False)
            self.onStart()
            self.pysat_fun.taskFinished.connect(self.onFinished)

    ################# Restoration toolset below

    def on_save_clicked(self):
        try:
            filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Choose where you want save your file", '.',
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump(self.pysat_fun.get_list(), fp)
        except:
            print("File not loaded")

    def on_load_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Workflow File", '.', "(*.wrf)")
        print(filename)
        try:
            with open(filename, 'rb') as fp:
                self.restore_list = pickle.load(fp)
        except:
            ui_modules.error_print("File was not loaded")
        self.restore_first()

    def restore_first(self):   #This function should no longer be necessary once we have error handling with restoration working smoothly

        # first run a single or double instance of getattr depending on what data is in the queue
        #   We'll need to remember 'i' so we don't accidentally run the instance too many times
        # then press ok
        # then we'll have another loop continue on it's merry way adding everything in.

        # TODO: Don't run the function until the UI has been loaded
        # TODO: allow set outpath to be run before loading data


        try:
            self.r_list = self.restore_list.pop()
            while self.r_list[1] == "do_get_data" or self.r_list[1] == 'do_read_ccam':
                getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
                print(self.r_list)
                self.r_list = self.restore_list.pop()
            self.on_okButton_clicked()
            self.pysat_fun.taskFinished.connect(self.restore_rest)
        except Exception as e:
            print(e)

    def restore_rest(self):
        if self.restore_flag is False:
            getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
            for i in range(len(self.restore_list)):
                self.r_list = self.restore_list.pop()
                print(self.r_list)
                getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
            self.restore_flag = True

    ################# Progress bar toolset below

    def onStart(self):  # onStart function
        self.progressBar.setRange(0, 0)  # make the bar pulse green
        self.pysat_fun.start()  # TaskThread.start()
        # This is multithreading thus run() == start()




    def onFinished(self):  # onFinished function
        self.progressBar.setRange(0, 1)  # stop the bar pulsing green
        self.progressBar.setValue(1)  # displays 100% after process is finished.
