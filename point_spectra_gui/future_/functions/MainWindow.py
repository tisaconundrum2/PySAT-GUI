from PyQt5 import QtWidgets

from point_spectra_gui.ui import MainWindow


class Ui_MainWindow(MainWindow.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.menu_item_shortcuts()  # set up the shortcuts

    def addWidget(self, object):
        widget = object()
        widget.setupUi(self.scrollArea)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(widget.get_widget())

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionRestore_Workflow.setShortcut("ctrl+R")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")
