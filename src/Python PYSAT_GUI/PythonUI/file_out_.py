from PyQt4 import QtCore, QtGui
from pysat_function import pysat_func

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


class file_outpath_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()


    def file_outpath(self, MainWindow):
        self.outputFolder = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputFolder.setFont(font)
        self.outputFolder.setObjectName(_fromUtf8("outputFolder"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.outputFolder)
        self.verticalLayout_22.setMargin(11)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setMargin(11)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setMargin(11)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.label_9 = QtGui.QLabel(self.outputFolder)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_25.addWidget(self.label_9)
        self.horizontalLayout_13.addLayout(self.verticalLayout_25)
        self.verticalLayout_28 = QtGui.QVBoxLayout()
        self.verticalLayout_28.setMargin(11)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(_fromUtf8("verticalLayout_28"))
        self.lineEdit_10 = QtGui.QLineEdit(self.outputFolder)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.verticalLayout_28.addWidget(self.lineEdit_10)
        self.horizontalLayout_13.addLayout(self.verticalLayout_28)
        self.verticalLayout_29 = QtGui.QVBoxLayout()
        self.verticalLayout_29.setMargin(11)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.fullDataBaseButton_4 = QtGui.QToolButton(self.outputFolder)
        self.fullDataBaseButton_4.setObjectName(_fromUtf8("fullDataBaseButton_4"))
        self.verticalLayout_29.addWidget(self.fullDataBaseButton_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_29)
        self.verticalLayout_22.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addWidget(self.outputFolder)
        self.outputFolder.raise_()
        self.outputFolder.setTitle(_translate("MainWindow", "Output", None))
        self.label_9.setText(_translate("MainWindow", "Output Folder", None))
        self.lineEdit_10.setText(_translate("MainWindow", "*.*", None))
        self.fullDataBaseButton_4.setText(_translate("MainWindow", "...", None))
        try:
            self.fullDataBaseButton_4.clicked.connect(lambda: file_outpath_.on_outPutLocationButton_clicked(self, self.lineEdit_10))
        except:
            pass

            #### Opening Files

    def on_outPutLocationButton_clicked(self, lineEdit):
        filename = QtGui.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        lineEdit.setText(filename)
        self.pysat_fun.set_file_outpath(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*/*")

            #### Ok Button Clicked
