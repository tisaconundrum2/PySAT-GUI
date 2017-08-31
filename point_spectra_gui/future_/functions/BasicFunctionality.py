from Qtickle import Qtickle


class Basics:
    def connectWidgets(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)

    def getGuiParams(self):
        # TODO put the parameters inside of a list/dictionary
        # TODO create a function that loads in the necessary module
        s = self.qt.guiSave()
        print(s)
        return s
