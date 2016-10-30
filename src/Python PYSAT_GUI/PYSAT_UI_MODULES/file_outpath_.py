from PyQt4 import QtCore, QtGui

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


class file_outpath_:
    def __init__(self, pysat_fun, verticalLayout_8):
        self.pysat_fun = pysat_fun
        self.verticalLayout_8 = verticalLayout_8


    def file_outpath(self):
        self.file_out_path = QtGui.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_out_path.setFont(font)
        self.file_out_path.setObjectName(_fromUtf8("file_out_path"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.file_out_path)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.file_out_path_label = QtGui.QLabel(self.file_out_path)
        self.file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtGui.QLineEdit(self.file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtGui.QToolButton(self.file_out_path)
        self.file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
        self.horizontalLayout.addWidget(self.file_out_path_button)
        self.verticalLayout_8.addWidget(self.file_out_path)

        self.file_out_path.setTitle(_translate("MainWindow", "Ouput Folder", None))
        self.file_out_path_label.setText(_translate("MainWindow", "Folder Name", None))
        self.file_out_path_line_edit.setText(_translate("MainWindow", "*/", None))
        self.file_out_path_button.setText(_translate("MainWindow", "...", None))

        try:
            self.file_out_path_button.clicked.connect(lambda: file_outpath_.on_outPutLocationButton_clicked(self, self.file_out_path_line_edit))
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
