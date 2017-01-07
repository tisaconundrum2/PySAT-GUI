import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import inspect

# this is the restore class
# use guisave to save the current layout/module
# use guirestore to restore the module.


class restore_:
    def __init__(self, ui, settings):
        self.settings = settings
        self.ui = ui

    def guisave(self):
        for name, obj in inspect.getmembers(self.ui):
            # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
            if isinstance(obj, QComboBox):
                index = obj.currentIndex()  # get current region from combobox
                # text   = obj.itemText(index)   # get the text for new selected index
                name = obj.objectName()

                value = (self.settings.value(name))

                if value == "":
                    continue

                index = obj.findText(value)  # get the corresponding index for specified string in combobox

                if index == -1:  # add to list if not found
                    obj.insertItems(0, [value])
                    index = obj.findText(value)
                    obj.setCurrentIndex(index)
                else:
                    obj.setCurrentIndex(index)  # preselect a combobox value by index

            if isinstance(obj, QLineEdit):
                name = obj.objectName()
                value = obj.text()
                self.settings.setValue(name, value)  # save ui values, so they can be restored next time

            if isinstance(obj, QCheckBox):
                name = obj.objectName()
                state = obj.checkState()
                self.settings.setValue(name, state)

            if isinstance(obj, QRadioButton):
                name = obj.objectName()
                value = obj.isChecked()  # get stored value from registry
                self.settings.setValue(name, value)

            if isinstance(obj, QSlider):
                name = obj.objectName()
                value = obj.value()  # get stored value from registry
                self.settings.setValue(name, value)

            if isinstance(obj, QSpinBox):
                name = obj.objectName()
                value = obj.value()  # get stored value from registry
                self.settings.setValue(name, value)

    def guirestore(self):
        for name, obj in inspect.getmembers(self.ui):
            if isinstance(obj, QComboBox):
                index = obj.currentIndex()  # get current region from combobox
                # text   = obj.itemText(index)   # get the text for new selected index
                name = obj.objectName()

                value = self.settings.value(name)

                if value == "":
                    continue

                index = obj.findText(value)  # get the corresponding index for specified string in combobox

                if index == -1:  # add to list if not found
                    obj.insertItems(0, [value])
                    index = obj.findText(value)
                    obj.setCurrentIndex(index)
                else:
                    obj.setCurrentIndex(index)  # preselect a combobox value by index

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
