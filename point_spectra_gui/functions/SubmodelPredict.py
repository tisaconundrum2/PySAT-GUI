from PyQt5 import QtWidgets
from pysat.regression import sm

from point_spectra_gui.ui.SubmodelPredict import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class subWidgets:
    def __init__(self, modelComboBox, minLabel, minSpinBox, maxLabel, maxSpinBox):
        self.modelComboBox = modelComboBox
        self.minLabel = minLabel
        self.minSpinBox = minSpinBox
        self.maxLabel = maxLabel
        self.maxSpinBox = maxSpinBox

    def setHidden(self, bool):
        self.modelComboBox.setHidden(bool)
        self.minLabel.setHidden(bool)
        self.minSpinBox.setHidden(bool)
        self.maxLabel.setHidden(bool)
        self.maxSpinBox.setHidden(bool)

    def getValues(self):
        return int(self.minSpinBox.text()), int(self.maxSpinBox.text())

    def setMaximum(self, int_):
        self.minSpinBox.setMaximum(int_)
        self.maxSpinBox.setMaximum(int_)

    def setValue(self, int_):
        self.minSpinBox.setValue(int_)
        self.maxSpinBox.setValue(int_)

    def spinBox(self, int_):
        if int_ == 0:
            return self.minSpinBox
        elif int_ == 1:
            return self.maxSpinBox
        else:
            return "Not a valid number"


class Ui_Form(Ui_Form, Basics):
    def __init__(self):
        super().__init__()
        self.subwidgets = []
        self.index = 1

    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.referenceModelComboBox, self.modelkeys)
        self.setComboBox(self.lowModelMaxSpinBox, self.modelkeys)
        self.setComboBox(self.highModelMaxSpinBox, self.modelkeys)
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setupWidgets()
        self.setHidden(self.subwidgets)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def setHidden(self, list):
        for i in range(0, len(list)):
            list[i].setHidden(True)

    def functions(self):
        ui_list = "do_submodel_predict"
        fun_list = "do_submodel_predict"
        modelranges = []
        submodel_names = []
        kws = {}

        try:
            datakey = self.chooseDataComboBox.currentText()
        except:
            datakey = None

        for i in self.submodel_gui_info:
            try:
                min_temp = i[1][0].value()
            except:
                min_temp = i[1][0]

            try:
                max_temp = i[1][1].value()
            except:
                max_temp = i[1][1]

            modelranges.append([min_temp, max_temp])
            submodel_names.append(i[0].currentText())

        try:
            trueval_data = self.chooseDataComboBox.currentText()
        except:
            trueval_data = None

        if trueval_data is not None:
            truevals = self.data[trueval_data].df[self.model_yvars[submodel_names[0]]]
            x_ref = []
        else:
            truevals = None

        # step through the submodel names and get the actual models and the x data
        x = []
        submodels = []
        for i in submodel_names:
            x.append(self.data[datakey].df[self.model_xvars[i]])
            submodels.append(self.models[i])
            if trueval_data is not None:
                x_ref.append(self.data[trueval_data].df[self.model_xvars[i]])

        # create the submodel object
        sm_obj = sm.sm(modelranges, submodels)

        # optimize blending if reference data is provided (otherwise, modelranges will be used as blending ranges)
        if truevals is not None:
            ref_predictions = sm_obj.predict(x_ref)
            ref_predictions_blended = sm_obj.do_blend(ref_predictions, truevals=truevals)

        # get predictions for each submodel separately
        predictions = sm_obj.predict(x)

        # blend the predictions together
        predictions_blended = sm_obj.do_blend(predictions)

        # save the individual and blended predictions
        for i, j in enumerate(predictions):
            self.data[datakey].df[('predict', submodel_names[i] + '-Predict')] = j
        self.data[datakey].df[('predict', 'Blended-Predict')] = predictions_blended
        pass

    def on_addRange_pushed(self):
        if self.index < len(self.subwidgets):
            self.subwidgets[self.index].setHidden(False)
            self.index += 1
        else:
            print("Cannot add more wavelengths")

    def on_deleteRange_pushed(self):
        if self.index > 1:
            self.index -= 1
            self.subwidgets[self.index].setHidden(True)
            self.subwidgets[self.index].setValue(0)
        else:
            print("Cannot delete any more wavelengths")

    def setupWidgets(self):
        self.subwidgets.append(
            subWidgets(self.modelComboBox, self.minLabel, self.minSpinBox, self.maxLabel, self.maxSpinBox))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_2, self.minLabel_2, self.minSpinBox_2, self.maxLabel_2, self.maxSpinBox_2))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_3, self.minLabel_3, self.minSpinBox_3, self.maxLabel_3, self.maxSpinBox_3))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_4, self.minLabel_4, self.minSpinBox_4, self.maxLabel_4, self.maxSpinBox_4))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_5, self.minLabel_5, self.minSpinBox_5, self.maxLabel_5, self.maxSpinBox_5))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_6, self.minLabel_6, self.minSpinBox_6, self.maxLabel_6, self.maxSpinBox_6))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_7, self.minLabel_7, self.minSpinBox_7, self.maxLabel_7, self.maxSpinBox_7))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_8, self.minLabel_8, self.minSpinBox_8, self.maxLabel_8, self.maxSpinBox_8))
        self.subwidgets.append(
            subWidgets(self.modelComboBox_9, self.minLabel_9, self.minSpinBox_9, self.maxLabel_9, self.maxSpinBox_9))
        self.subwidgets.append(subWidgets(self.modelComboBox_10, self.minLabel_10, self.minSpinBox_10, self.maxLabel_10,
                                          self.maxSpinBox_10))
        self.subwidgets.append(subWidgets(self.modelComboBox_11, self.minLabel_11, self.minSpinBox_11, self.maxLabel_11,
                                          self.maxSpinBox_11))
        self.subwidgets.append(subWidgets(self.modelComboBox_12, self.minLabel_12, self.minSpinBox_12, self.maxLabel_12,
                                          self.maxSpinBox_12))
        self.subwidgets.append(subWidgets(self.modelComboBox_13, self.minLabel_13, self.minSpinBox_13, self.maxLabel_13,
                                          self.maxSpinBox_13))
        self.subwidgets.append(subWidgets(self.modelComboBox_14, self.minLabel_14, self.minSpinBox_14, self.maxLabel_14,
                                          self.maxSpinBox_14))
        self.subwidgets.append(subWidgets(self.modelComboBox_15, self.minLabel_15, self.minSpinBox_15, self.maxLabel_15,
                                          self.maxSpinBox_15))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
