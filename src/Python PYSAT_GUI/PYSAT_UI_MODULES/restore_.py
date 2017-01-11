import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import inspect

class restore_:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def guisave(self):
        for name, obj in inspect.getmembers(self.ui):

            print(obj, name)
            if isinstance(obj, QComboBox):
                index = obj.currentIndex()
                name = obj.objectName()
                value = self.settings.vale(name)

                if value == "":
                    continue

                index = obj.findText(value)

                if index == -1:
                    obj.insertItems(0, [value])
                    index = obj.findText(value)
                    obj.setCurrentIndex(index)
                else:
                    obj.setCurrentIndex(index)

            if isinstance(obj, QLineEdit):
                name = obj.objectName()
                value = obj.text()
                # self.settings.setValue(name, state)
                print(value)

            if isinstance(obj, QCheckBox):
                name = obj.objectName()
                state = obj.checkState()
                # self.settings.setValue(name, state)
                print(state)

            if isinstance(obj, QRadioButton):
                name = obj.objectName()
                value = obj.isChecked()  # get stored value from registry
                # self.settings.setValue(name, value)
                print(value)

            if isinstance(obj, QSlider):
                name = obj.objectName()
                value = obj.value()  # get stored value from registry
                # self.settings.setValue(name, value)
                print(value)

            if isinstance(obj, QSpinBox):
                name = obj.objectName()
                value = obj.value()  # get stored value from registry
                # self.settings.setValue(name, value)
                print(value)

    def guirestore(self):
        for name, obj in inspect.getmembers(self.ui):

            if isinstance(obj, QComboBox):
                index = obj.currentIndex()
                name = obj.objectName()
                value = self.settings.value(name)

                if value == "":
                    continue

                index = obj.findText(value)

                if index == -1:
                    obj.insertItems(0, [value])
                    index = obj.findText(value)
                    obj.setCurrentIndex(index)
                else:
                    obj.setCurrentIndex(index)

            if isinstance(obj, QLineEdit):
                name = obj.objectName()
                value = self.settings.value(name)  # get stored value from registry
                obj.setText(value)  # restore lineEditFile

            if isinstance(obj, QCheckBox):
                name = obj.objectName()
                value = self.settings.value(name)  # get stored value from registry
                if value != None:
                    obj.setChecked(value)  # restore checkbox

            if isinstance(obj, QRadioButton):
                name = obj.objectName()
                value = self.settings.value(name)  # get stored value from registry
                if value != None:
                    obj.setChecked(value)

            if isinstance(obj, QSlider):
                name = obj.objectName()
                value = self.settings.value(name)  # get stored value from registry
                if value != None:
                    obj.setValue(int(value))  # restore value from registry

            if isinstance(obj, QSpinBox):
                name = obj.objectName()
                value = self.settings.value(name)  # get stored value from registry
                if value != None:
                    obj.setValue(int(value))  # restore value from registry
