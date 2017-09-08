from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.Normalization import Ui_Form


class normWidgets:
    def __init__(self, minimumWavelengthLabel, minimumWavelengthSpinBox, maximumWavelengthLabel,
                 maximumWavelengthSpinBox):
        self.minimumWavelengthLabel = minimumWavelengthLabel
        self.minimumWavelengthSpinBox = minimumWavelengthSpinBox
        self.maximumWavelengthLabel = maximumWavelengthLabel
        self.maximumWavelengthSpinBox = maximumWavelengthSpinBox

    def setHidden(self, bool):
        self.minimumWavelengthLabel.setHidden(bool)
        self.minimumWavelengthSpinBox.setHidden(bool)
        self.maximumWavelengthLabel.setHidden(bool)
        self.maximumWavelengthSpinBox.setHidden(bool)

    def setMinMax(self):
        pass

    def getValues(self):
        return [self.minimumWavelengthSpinBox.text(), self.maximumWavelengthSpinBox.text()]


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setupWidgets()
        self.setHidden(self.normwidgets)
        self.addRangePushButton.clicked.connect()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def setHidden(self, list):
        for i in range(1, len(list)):
            list[i].setHidden(True)

    def setupWidgets(self):
        self.normwidgets = []
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