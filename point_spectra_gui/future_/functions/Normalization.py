from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.Normalization import Ui_Form


class normWidgets:
    def __init__(self, minimumWLabel, minimumWSpinBox, maximumWLabel, maximumWSpinBox):
        self.minimumWLabel = minimumWLabel
        self.minimumWSpinBox = minimumWSpinBox
        self.maximumWLabel = maximumWLabel
        self.maximumWSpinBox = maximumWSpinBox

    def setHidden(self, bool):
        self.minimumWLabel.setHidden(bool)
        self.minimumWSpinBox.setHidden(bool)
        self.maximumWLabel.setHidden(bool)
        self.maximumWSpinBox.setHidden(bool)

    def getValues(self):
        return (int(self.minimumWSpinBox.text()), int(self.maximumWSpinBox.text()))

    def clearValues(self):
        self.minimumWSpinBox.clear()
        self.maximumWSpinBox.clear()

    def setMaximum(self, int_):
        self.minimumWSpinBox.setMaximum(int_)
        self.maximumWSpinBox.setMaximum(int_)

    def spinBox(self, int_):
        if int_ == 0:
            return self.minimumWSpinBox
        elif int_ == 1:
            return self.maximumWSpinBox
        else:
            return "Not a valid number"


class Ui_Form(Ui_Form, Basics):
    def __init__(self):
        super().__init__()
        self.normwidgets = []
        self.all_boxes = []
        self.index = 1

    def setupUi(self, Form):
        self.__init__()
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setupWidgets()
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setListWidget(self.varToNormalizeListWidget, self.xvar_choices())
        self.setMaximum(9999999)
        self.clearValues()
        self.setHidden(self.normwidgets)
        self.qt.isGuiChanged(self.checkForNewMax)
        self.addRangePushButton.clicked.connect(self.on_addRange_pushed)
        self.deleteRangePushButton.clicked.connect(self.on_deleteRange_pushed)

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def setHidden(self, list):
        for i in range(1, len(list)):
            list[i].setHidden(True)

    def setMaximum(self, int_):
        for items in self.normwidgets:
            items.setMaximum(int_)

    def clearValues(self):
        for items in self.normwidgets:
            items.clearValues()

    def on_addRange_pushed(self):
        if self.index < len(self.normwidgets):
            self.normwidgets[self.index].setHidden(False)
            self.index += 1
        else:
            print("Cannot add more wavelengths")

    def on_deleteRange_pushed(self):
        if self.index > 1:
            self.index -= 1
            self.normwidgets[self.index].setHidden(True)
            self.normwidgets[self.index].clearValues()
        else:
            print("Cannot delete any more wavelengths")

    def setupWidgets(self):
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel, self.minimumWavelengthSpinBox,
                                            self.maximumWavelengthLabel, self.maximumWavelengthSpinBox))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_2, self.minimumWavelengthSpinBox_2,
                                            self.maximumWavelengthLabel_2, self.maximumWavelengthSpinBox_2))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_3, self.minimumWavelengthSpinBox_3,
                                            self.maximumWavelengthLabel_3, self.maximumWavelengthSpinBox_3))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_4, self.minimumWavelengthSpinBox_4,
                                            self.maximumWavelengthLabel_4, self.maximumWavelengthSpinBox_4))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_5, self.minimumWavelengthSpinBox_5,
                                            self.maximumWavelengthLabel_5, self.maximumWavelengthSpinBox_5))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_6, self.minimumWavelengthSpinBox_6,
                                            self.maximumWavelengthLabel_6, self.maximumWavelengthSpinBox_6))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_7, self.minimumWavelengthSpinBox_7,
                                            self.maximumWavelengthLabel_7, self.maximumWavelengthSpinBox_7))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_8, self.minimumWavelengthSpinBox_8,
                                            self.maximumWavelengthLabel_8, self.maximumWavelengthSpinBox_8))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_9, self.minimumWavelengthSpinBox_9,
                                            self.maximumWavelengthLabel_9, self.maximumWavelengthSpinBox_9))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_10, self.minimumWavelengthSpinBox_10,
                                            self.maximumWavelengthLabel_10, self.maximumWavelengthSpinBox_10))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_11, self.minimumWavelengthSpinBox_11,
                                            self.maximumWavelengthLabel_11, self.maximumWavelengthSpinBox_11))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_12, self.minimumWavelengthSpinBox_12,
                                            self.maximumWavelengthLabel_12, self.maximumWavelengthSpinBox_12))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_13, self.minimumWavelengthSpinBox_13,
                                            self.maximumWavelengthLabel_13, self.maximumWavelengthSpinBox_13))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_14, self.minimumWavelengthSpinBox_14,
                                            self.maximumWavelengthLabel_14, self.maximumWavelengthSpinBox_14))
        self.normwidgets.append(normWidgets(self.minimumWavelengthLabel_15, self.minimumWavelengthSpinBox_15,
                                            self.maximumWavelengthLabel_15, self.maximumWavelengthSpinBox_15))
        for i in range(len(self.normwidgets)):
            for j in range(0, 2):
                self.all_boxes.append(self.normwidgets[i].spinBox(j))

    def checkForNewMax(self):
        for i in range(len(self.all_boxes) - 1):
            self.all_boxes[i].valueChanged.connect(self.all_boxes[i + 1].setMinimum)

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].df.columns.levels[
                    0].values
            except:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices

    def function(self):
        ranges = []
        for i in range(self.index):
            ranges.append(self.normwidgets[i].getValues())
        datakey = self.chooseDataComboBox.currentText()
        try:
            col_var, filter_ = self.varToNormalizeListView.selectedItems().text()
        except:
            col_var = 'wvl'
        print("{}".format(ranges))
        try:
            print(self.data[datakey].df.columns.levels[0])
            self.data[datakey].norm(ranges, col_var=col_var)
            print(self.data[datakey].df.columns.levels[0])
            print("Normalization has been applied to the ranges: " + str(ranges))
        except Exception as e:
            print("There was a problem: ", e)
