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


class normalization_:
    # Normalization creates a UI
    # and many smaller pieces of the UI called min_max
    #
    # normalization
    #     |_ min_max
    #     |_ min_max
    #     |_ min_max
    #
    #       each of these have connections that tell us what was updated
    # each of these updates should return a value back to normalization so we can add it to a list
    #
    #      |---------------------|           |----------------------|
    #      |    Normalization    |           |       min_max        |
    #      |---------------------|           |----------------------|
    #      |                     | <-------- | return value/pos     |
    #      | load UI/Boxes       | --------> |                      |
    #      |---------------------|           |----------------------|
    #
    # every time we change boxes, we should know which box is getting updated, and what the updated value is
    #
    # so for example
    #
    #     min [      ]  max [      ]
    #     min [      ]  max [ 100  ]*
    #     min [      ]  max [      ]
    # the above box* was update4d
    # it's position is data[1], max, and it's value is 100

    def __init__(self, pysat_fun, verticalLayout):
        # normalization needs a list. It will look like this [(0,0), (0,0), (0,0)]
        self.list = [(None, None)] * 24
        self.pysat_fun = pysat_fun
        # normalization needs the necessary layouts to work.
        self.verticalLayout_8 = verticalLayout
        # normalization_ needs a driver function main
        self.main()

    def main(self):
        # Load a in function
        self.pysat_fun.set_arg_list(self.pysat_fun.do_norm)
        # main needs to call the UI
        self.normalization_ui()

    def normalization_ui(self):
        self.normalization = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalization.setFont(font)
        self.normalization.setObjectName(_fromUtf8("normalization"))
        self.verticalLayout = QtGui.QVBoxLayout(self.normalization)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.choosedata_layout = QtGui.QHBoxLayout()
        self.choosedata_layout.setMargin(11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName(_fromUtf8("choosedata_layout"))
        self.regression_choosedata_label = QtGui.QLabel(self.normalization)
        self.regression_choosedata_label.setObjectName(_fromUtf8("regression_choosedata_label"))
        self.choosedata_layout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtGui.QComboBox(self.normalization)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
        self.choosedata_layout.addWidget(self.regression_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)
        self.all_ranges_layout = QtGui.QVBoxLayout()
        self.all_ranges_layout.setMargin(11)
        self.all_ranges_layout.setSpacing(6)
        self.all_ranges_layout.setObjectName(_fromUtf8("all_ranges_layout"))
        self.verticalLayout.addLayout(self.all_ranges_layout)
        self.min_max_horizontalLayout = QtGui.QHBoxLayout()
        self.min_max_horizontalLayout.setMargin(11)
        self.min_max_horizontalLayout.setSpacing(6)
        self.min_max_horizontalLayout.setObjectName(_fromUtf8("min_max_horizontalLayout"))
        self.add_ranges_button = QtGui.QPushButton(self.normalization)
        self.add_ranges_button.setObjectName(_fromUtf8("add_ranges_button"))
        self.min_max_horizontalLayout.addWidget(self.add_ranges_button)
        self.del_ranges_button = QtGui.QPushButton(self.normalization)
        self.del_ranges_button.setObjectName(_fromUtf8("add_ranges_button_2"))
        self.min_max_horizontalLayout.addWidget(self.del_ranges_button)
        self.verticalLayout.addLayout(self.min_max_horizontalLayout)
        self.verticalLayout_8.addWidget(self.normalization)

        self.normalization.setTitle(_translate("MainWindow", "Normalization", None))
        self.regression_choosedata_label.setText(_translate("MainWindow", "Choose data: ", None))
        self.regression_choosedata.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.add_ranges_button.setText(_translate("MainWindow", "Add Ranges", None))
        self.del_ranges_button.setText(_translate("MainWindow", "delete Ranges", None))

    def add_norm_value(self):
        pass


class min_max:
    def __init__(self):
        pass
