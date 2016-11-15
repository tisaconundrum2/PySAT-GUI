from PyQt4 import QtCore, QtGui
from PYSAT_UI_MODULES.Error_ import error_print

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


# Normalization creates a UI
# and many smaller pieces of the UI called min_max
#
# normalization
#     |_ min_max
#     |_ min_max
#     |_ min_max
#
# each of these min_max's have connections that tell us what was updated
# each of these updates should return a value back to normalization so we can add it to a list
#
#      |---------------------|           |----------------------|
#      |    Normalization    |           |       min_max        |
#      |---------------------|           |----------------------|
#      | returned val in lst | <-------- | return value and pos |
#      | load UI/Boxes       | --------> |                      |
#      |---------------------|           |----------------------|
#
# every time we change boxes, we should know which box is getting updated, and what the updated value is
# so for example
#
#     min [      ]  max [      ]
#     min [      ]  max [ 1000 ]*
#     min [      ]  max [      ]
# the above box* was update4d
# it's position is data[1], max_lineEdit, and it's value is 1000
class normalization_:
    def __init__(self, pysat_fun, verticalLayout):
        self.min
        self.max
        self.main()

    def main(self):
        pass

    def add_ranges(self):
        Add_ranges.add_boxes()

    def del_ranges(self):
        Del_ranges.del_boxes()

class Add_ranges(normalization_):
    def __init__(self, pysat_fun, verticalLayout):
        super().__init__(pysat_fun, verticalLayout)
        self.min
        self.max
        self.add_boxes()


    def add_boxes(self):
        pass


class Del_ranges(normalization_):
    def __init__(self, pysat_fun, verticalLayout):
        super().__init__(pysat_fun, verticalLayout)
        self.del_boxes()

    def del_boxes(self):
        pass