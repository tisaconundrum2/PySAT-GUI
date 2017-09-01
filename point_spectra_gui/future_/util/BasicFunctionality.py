from Qtickle import Qtickle


class Basics:
    def __init__(self):
        self.data = {}  # initialize with an empty dict to hold data frames
        self.datakeys = []

    def connectWidgets(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)

    def getGuiParams(self):
        """
        Return the contents of the UI
        :return:
        """
        s = self.qt.guiSave()
        print(s)
        return s

    def function(self):
        """
        Each Modules functionality
        :return:
        """
        pass
