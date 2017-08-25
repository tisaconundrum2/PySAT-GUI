import traceback

import numpy as np
# from plio import io_ccam_pds
import pandas as pd
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from pysat.fileio import io_ccam_pds
from pysat.plotting.plots import make_plot, pca_ica_plot
from pysat.regression import cv
from pysat.regression import regression
from pysat.regression import sm
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui_modules.Error_ import error_print
from point_spectra_gui.ui_modules.del_layout_ import *


class Module:
    nodeCount = 0

    def __init__(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore
        self.next = None
        self.UI_ID = Module.nodeCount
        Module.nodeCount += 1

    def setData(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore

    def getID(self):
        return self.UI_ID

    def getData(self):
        list = []
        list.append(self.getID())
        list.append(self.ui_list)
        list.append(self.fun_list)
        list.append(self.arg_list)
        list.append(self.kw_list)
        list.append(self.ui_restore)
        return list

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class listOfModules:
    def __init__(self):
        self.head = None
        self.curr_count = 0

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def push(self, ui_list, fun_list, arg_list, kw_list, ui_restore, UI_ID=None):
        if not self.amend(ui_list, fun_list, arg_list, kw_list, ui_restore,
                          UI_ID):  # if the UI_ID that we are playing with exists, amend it, otherwise make something new
            if len(self) == 0:
                # Create a new head
                temp = Module(ui_list, fun_list, arg_list, kw_list, ui_restore)  # self.head = None; temp = 0x085817F0
                temp.setNext(self.head)  # temp = 0x085817F0; temp.next = None
                self.head = temp  # self.head = 0x085817F0; self.head.next = None; temp = 0x085817F0; temp.next = None
                return temp.getID()
            else:
                # Append new data into .next
                temp = Module(ui_list, fun_list, arg_list, kw_list,
                              ui_restore)  # self.head = 0x085817F0; temp = 0x00568330
                current = self.head  # current = 0x085817F0; current.next = None; self.head = 0x085817F0; temp = 0x00568330
                while current.getNext() != None:  #
                    current = current.getNext()  #
                current.setNext(temp)  # current = 0x085817F0; current.next = 0x00568330;
                return temp.getID()
        return UI_ID

    def amend(self, ui_list, fun_list, arg_list, kw_list, ui_restore, UI_ID=None):
        current = self.head
        found = False
        while current is not None and not found and UI_ID is not None:
            if current.getID() == UI_ID:
                found = True
                current.setData(ui_list, fun_list, arg_list, kw_list, ui_restore)
            else:
                current = current.getNext()
        return found

    def pop(self):
        try:
            current = self.head
            self.head = self.head.getNext()
            return current.getData()
        except:
            pass

    def del_module(self):
        current = self.head
        if len(self) == 1:
            self.head = None
            return 1
        while current.getNext().getNext() is not None:
            current = current.getNext()
        current.setNext(None)
        return 1

    def pull(self):
        i = 0
        current = self.head
        while i < self.curr_count and current.getNext() is not None:
            current = current.getNext()
            i += 1
        self.curr_count += 1
        return current.getData()

    def isEmpty(self):
        return self.head == None

    def remove(self, UI_ID):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getID() == UI_ID:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def display(self):
        current = self.head
        while current is not None:
            for items in current.getData():
                print(items)
            current = current.getNext()