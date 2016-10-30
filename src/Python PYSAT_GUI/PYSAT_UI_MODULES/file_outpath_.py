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


def file_outpath(pysat_fun, verticalLayout_8):
    file_out_path = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    file_out_path.setFont(font)
    file_out_path.setObjectName(_fromUtf8("file_out_path"))
    horizontalLayout = QtGui.QHBoxLayout(file_out_path)
    horizontalLayout.setMargin(11)
    horizontalLayout.setSpacing(6)
    horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    file_out_path_label = QtGui.QLabel(file_out_path)
    file_out_path_label.setObjectName(_fromUtf8("file_out_path_label"))
    horizontalLayout.addWidget(file_out_path_label)
    file_out_path_line_edit = QtGui.QLineEdit(file_out_path)
    file_out_path_line_edit.setReadOnly(True)
    file_out_path_line_edit.setObjectName(_fromUtf8("file_out_path_line_edit"))
    horizontalLayout.addWidget(file_out_path_line_edit)
    file_out_path_button = QtGui.QToolButton(file_out_path)
    file_out_path_button.setObjectName(_fromUtf8("file_out_path_button"))
    horizontalLayout.addWidget(file_out_path_button)
    verticalLayout_8.addWidget(file_out_path)

    file_out_path.setTitle(_translate("MainWindow", "Ouput Folder", None))
    file_out_path_label.setText(_translate("MainWindow", "Folder Name", None))
    file_out_path_line_edit.setText(_translate("MainWindow", "*/", None))
    file_out_path_button.setText(_translate("MainWindow", "...", None))

    try:
        file_out_path_button.clicked.connect(lambda: on_outPutLocationButton_clicked(pysat_fun, file_out_path_line_edit))
    except:
        pass

        #### Opening Files

def on_outPutLocationButton_clicked(pysat_fun, lineEdit):
    filename = QtGui.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
    lineEdit.setText(filename)
    pysat_fun.set_file_outpath(filename)
    if lineEdit.text() == "":
        lineEdit.setText("*/*")

        #### Ok Button Clicked
