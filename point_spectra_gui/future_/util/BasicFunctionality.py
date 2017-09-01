from Qtickle import Qtickle


class Basics:
    def __init__(self):
        self.data = {}  # initialize with an empty dict to hold data frames
        self.datakeys = []

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
        For every single click, movement, keyboard click - there will be a state change
        Get these changes and react
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)

    def getGuiParams(self):
        """
        Return the contents from lineEdits, comboBoxes, etc.
        :return:
        """
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
