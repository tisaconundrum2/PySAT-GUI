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
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.min = 0
        self.max = 0
        self.main()

    def main(self):
        # driver function, calls UI and set's up connections
        # add function list calls here
        self.pysat_fun.set_fun_list(self.pysat_fun.do_norm)
        self.normalization_ui()
        try:
            self.add_ranges_button.clicked.connect(lambda: self.add_ranges())
            self.del_ranges_button.clicked.connect(lambda: self.del_ranges())
        except:
            pass

    def normalization_ui(self):
        # add all UI code here
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            error_print('No Data has been loaded')
            datachoices = ['No data has been loaded!']
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
        self.regression_choosedata = make_combobox(datachoices)
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
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.add_ranges_button.setText(_translate("MainWindow", "Add Range", None))
        self.del_ranges_button.setText(_translate("MainWindow", "Delete All Ranges", None))

    def set_min(self):
        # get the box range min from the specific class of focus
        pass

    def set_max(self):
        # get the box range max from the specific class of focus
        pass

    def add_ranges(self):
        # TODO make boxes appear
        add_ranges.add_boxes(self)

    def del_ranges(self):
        # make boxes disappear
        del_ranges.del_boxes(self)


class add_ranges(normalization_):
    def __init__(self, pysat_fun, verticalLayout_8):
        super().__init__(pysat_fun, verticalLayout_8)
        self.min = 0
        self.max = 0

    def get_min(self):
        # return an int
        self.min = self.min_lineEdit.text()
        return self.min

    def get_max(self):
        # return an int
        self.max = self.max_lineEdit.text()
        return self.max

    def add_boxes(self):
        # TODO create UI boxes
        self.ranges_layout = QtGui.QHBoxLayout()
        self.ranges_layout.setMargin(11)
        self.ranges_layout.setSpacing(6)
        self.ranges_layout.setObjectName(_fromUtf8("ranges_layout"))
        self.min_label = QtGui.QLabel(self.normalization)
        self.min_label.setObjectName(_fromUtf8("min_label"))
        self.ranges_layout.addWidget(self.min_label)
        self.min_lineEdit = QtGui.QLineEdit(self.normalization)
        self.min_lineEdit.setObjectName(_fromUtf8("min_lineEdit"))
        self.ranges_layout.addWidget(self.min_lineEdit)
        self.max_label = QtGui.QLabel(self.normalization)
        self.max_label.setObjectName(_fromUtf8("max_label"))
        self.ranges_layout.addWidget(self.max_label)
        self.max_lineEdit = QtGui.QLineEdit(self.normalization)
        self.max_lineEdit.setObjectName(_fromUtf8("max_lineEdit"))
        self.ranges_layout.addWidget(self.max_lineEdit)
        self.all_ranges_layout.addLayout(self.ranges_layout)
        self.min_label.setText(_translate("MainWindow", "Min", None))
        self.max_label.setText(_translate("MainWindow", "Max", None))


class del_ranges(normalization_):
    def __init__(self):
        self.del_boxes()

    def del_boxes(self):
        # TODO use deletLater to delete the entire widget
        try:
            self.all_ranges_layout.deleteLater()
        except:
            pass
        self.all_ranges_layout = QtGui.QVBoxLayout()


def make_combobox(choices):
    combo = QtGui.QComboBox()
    for i, choice in enumerate(choices):
        combo.addItem(_fromUtf8(""))
        combo.setItemText(i, _translate('', choice, None))
    return combo
