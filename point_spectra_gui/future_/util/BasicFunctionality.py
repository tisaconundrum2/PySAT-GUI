from Qtickle import Qtickle


class Basics:
    """
    This class is regarded as the scaffolding class
    It is here to make sure that users remember to
    add the necessary, Basic, functionalities to
    each of their UI classes. This will serve as a
    reminder of what still needs to be added.

    *Note: Rigorous prototyping is still occurring
    So, naturally assume that something in this class
    is always getting changed or added to better serve
    all cases in each UI class.
    """
    data = {}  # initialize with an empty dict to hold data frames
    datakeys = []
    def __init__(self):
        """
        Since `Basics` is shared among all the UI
        classes it would make sense that we would have
        some variables, that are necessary among all these
        classes, be placed here in a high place where they
        can be referenced often.
        """


    def setupUi(self, Form):
        """
        Get the Ui_Form, it is like the HTML of the UI
        It will show the entire the styling of the UI
        :param Form:
        :return:
        """
        pass

    def get_widget(self):
        """
        In order to display the UI
        You need to return the UI where the styling was dumped
        use this function to get the variable responsible
        :return:
        """
        pass

    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        pass

    def getGuiParams(self):
        """
        Return the contents from lineEdits, comboBoxes, etc.
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        s = self.qt.guiSave()
        print(s)
        return s

    def function(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        pass

    def setDisabled(self, bool):
        """
        After every execution we want to prevent the user from changing something.
        So, disable the layout (grey it out)
        :param bool:
        :return:
        """
        pass

    def setComboBox(self, comboBox):
        """
        Sets up the information inside comboBox widgets
        :param choices:
        :param comboBox:
        :return:
        """
        for i, choice in enumerate(Basics.datakeys):
            comboBox.addItem("")
            comboBox.setItemText(i, str(choice))