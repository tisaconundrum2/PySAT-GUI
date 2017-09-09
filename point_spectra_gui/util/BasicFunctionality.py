import sys

from Qtickle import Qtickle


class Basics:
    """
    This class is a scaffolding class, it holds global
    functionality for all classes inheriting from it.
    It is here to simplify and globalize certain
    variables and functionalities to each of the
    UI classes.

    *Note: Rigorous prototyping is still occurring
    So, naturally, assume that something in this class
    is always getting changed or added to better serve
    all cases in each UI class.

    ...

    Since `Basics` is shared among all the UI
    classes it would make sense that we would have
    some variables, that are necessary among all these
    classes, be put here in a high place where they
    can be referenced often.
    """
    data = {}  # initialize with an empty dict to hold data frames
    datakeys = []  # hold all the specific key for a specific data frame
    outpath = './'  # Default outpath; can be changed with OutputFolder.py
    figs = {}
    def __init__(self):
        self.qt = Qtickle.Qtickle(self)

    def setupUi(self, Form):
        """
        Get the Ui_Form, it is like the HTML of the UI
        It will show the styling of the UI. But buttons
        and widgets have no function. connectWidgets
        fixes this
        :param Form:
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "SetupUI()" was not found in this module ')

    def get_widget(self):
        """
        This function specifies the variable that holds the
        styling. Use this function to get the variable
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "get_widget()" was not found in this module')

    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "connectWidgets()" was not found in this module')

    def getGuiParams(self):
        """
        Return the contents from lineEdits, comboBoxes, etc.
        :return:
        """
        s = self.qt.guiSave()
        return s

    def function(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "function()" was not found in this module')

    def isEnabled(self):
        """
        Checks to see if current widget isEnabled or not
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "setDisabled()" was not found in this module')

    def setDisabled(self, bool):
        """
        After every execution we want to prevent the user from changing something.
        So, disable the layout by greying it out
        :param bool:
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "setDisabled()" was not found in this module')

    def setComboBox(self, comboBox, keyValues):
        """
        Sets up the information inside comboBox widgets
        This function does not need to be overridden.
        :param comboBox:
        :param keyValues:
        :return:
        """
        for i, choice in enumerate(keyValues):
            comboBox.addItem("")
            comboBox.setItemText(i, str(choice))

    def changeComboListVars(self, obj, newchoices):
        """
        Function changes combo boxes
        This function does not need to be overridden.
        :param obj:
        :param newchoices:
        :return:
        """
        obj.clear()
        for i in newchoices:
            if isinstance(i, tuple):
                obj.addItem(i[1])
            elif isinstance(i, str):
                obj.addItem(i)

    def setListWidget(self, obj, choices):
        """
        Function changes lists
        This function does not need to be overridden
        :param obj:
        :param choices:
        :return:
        """
        for item in choices:
            obj.addItem(item)

    def setProgressBar(self, progressBar):
        """
        This function makes it possible to reference the progress bar
        in MainWindow
        :param progressBar:
        :return:
        """
        self.progressBar = progressBar
