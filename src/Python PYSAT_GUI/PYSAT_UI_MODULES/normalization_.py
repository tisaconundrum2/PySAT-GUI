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
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8
        self.data = [None] * 24
        self.num = 0
        self.main()

    def main(self):
        # append function to pysat
        # self.pysat_fun.fun_list.append(self.pysat_fun.set_file_outpath)
        self.normalization_ui()
        try:
            pass
            # parameters here
        except Exception as e:
            error_print(e)

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
        self.normalization_choosedata_hlayout = QtGui.QHBoxLayout()
        self.normalization_choosedata_hlayout.setMargin(11)
        self.normalization_choosedata_hlayout.setSpacing(6)
        self.normalization_choosedata_hlayout.setObjectName(_fromUtf8("normalization_choosedata_hlayout"))
        self.regression_choosedata_label = QtGui.QLabel(self.normalization)
        self.regression_choosedata_label.setObjectName(_fromUtf8("regression_choosedata_label"))
        self.normalization_choosedata_hlayout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtGui.QComboBox(self.normalization)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
        self.normalization_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.normalization_choosedata_hlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.normalization_choosedata_hlayout)
        self.add_ranges_button_hlayout = QtGui.QHBoxLayout()
        self.add_ranges_button_hlayout.setMargin(11)
        self.add_ranges_button_hlayout.setSpacing(6)
        self.add_ranges_button_hlayout.setObjectName(_fromUtf8("add_ranges_button_hlayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.add_ranges_button_hlayout.addItem(spacerItem1)
        self.add_ranges_button = QtGui.QPushButton(self.normalization)
        self.add_ranges_button.setObjectName(_fromUtf8("add_ranges_button"))
        self.add_ranges_button_hlayout.addWidget(self.add_ranges_button)
        self.verticalLayout.addLayout(self.add_ranges_button_hlayout)
        self.verticalLayout_8.addWidget(self.normalization)

        self.normalization.setTitle(_translate("MainWindow", "Normalization", None))
        self.regression_choosedata_label.setText(_translate("MainWindow", "Choose data: ", None))
        self.regression_choosedata.setItemText(0, _translate("MainWindow", "Choose Data", None))
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data", None))
        self.add_ranges_button.setText(_translate("MainWindow", "Add Ranges", None))
        self.add_ranges_button.clicked.connect(lambda: self.add_range_clicked(self.num))
        self.num = self.num + 1

    def add_range_clicked(self, num):
        self.data[num] = min_max(self.pysat_fun, self.normalization, self.verticalLayout, 0)


class min_max:
    def __init__(self, pysat_fun, normalization, verticalLayout, row_number):
        self.pysat_fun = pysat_fun
        self.normalization = normalization
        self.verticalLayout = verticalLayout
        self.row_number = row_number
        self.small_tuple = (None, None)
        self.min_max()

    def min_max(self):
        self.min_max_horizontalLayout = QtGui.QHBoxLayout()
        self.min_max_horizontalLayout.setMargin(11)
        self.min_max_horizontalLayout.setSpacing(6)
        self.min_max_horizontalLayout.setObjectName(_fromUtf8("min_max_horizontalLayout"))
        self.min_label = QtGui.QLabel(self.normalization)
        self.min_label.setObjectName(_fromUtf8("min_label"))
        self.min_max_horizontalLayout.addWidget(self.min_label)
        self.min_lineEdit = QtGui.QLineEdit(self.normalization)
        self.min_lineEdit.setObjectName(_fromUtf8("min_lineEdit"))
        self.min_max_horizontalLayout.addWidget(self.min_lineEdit)
        self.max_label = QtGui.QLabel(self.normalization)
        self.max_label.setObjectName(_fromUtf8("max_label"))
        self.min_max_horizontalLayout.addWidget(self.max_label)
        self.max_lineEdit = QtGui.QLineEdit(self.normalization)
        self.max_lineEdit.setObjectName(_fromUtf8("max_lineEdit"))
        self.min_max_horizontalLayout.addWidget(self.max_lineEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.min_max_horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.min_max_horizontalLayout)
        self.min_label.setText(_translate("MainWindow", "Min", None))
        self.max_label.setText(_translate("MainWindow", "Max", None))
        self.min_lineEdit.editingFinished.connect(lambda: self.set_list(self.min_lineEdit, self.max_lineEdit))
        self.max_lineEdit.editingFinished.connect(lambda: self.set_list(self.min_lineEdit, self.max_lineEdit))

    def set_list(self, min, max):
        if min.text() == '' and max.text() == '':
            error_print("Please fill in all boxes")
        else:
            try:
                min = int(min.text())
                max = int(max.text())
                self.small_tuple = (min, max)
                print(self.small_tuple)

            except:
                pass

    def add_to_pysat(self):
        self.pysat_fun.set_arg_list()
