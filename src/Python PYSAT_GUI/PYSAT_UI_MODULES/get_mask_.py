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

def get_mask(pysat_fun, verticalLayout_8):
    get_mask = QtGui.QGroupBox()
    font = QtGui.QFont()
    font.setPointSize(10)
    get_mask.setFont(font)
    get_mask.setObjectName(_fromUtf8("get_mask"))
    horizontalLayout = QtGui.QHBoxLayout(get_mask)
    horizontalLayout.setMargin(11)
    horizontalLayout.setSpacing(6)
    horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    get_mask_label = QtGui.QLabel(get_mask)
    get_mask_label.setObjectName(_fromUtf8("get_mask_label"))
    horizontalLayout.addWidget(get_mask_label)
    get_mask_line_edit = QtGui.QLineEdit(get_mask)
    get_mask_line_edit.setReadOnly(True)
    get_mask_line_edit.setObjectName(_fromUtf8("get_mask_line_edit"))
    horizontalLayout.addWidget(get_mask_line_edit)
    get_mask_button = QtGui.QToolButton(get_mask)
    get_mask_button.setObjectName(_fromUtf8("get_mask_button"))
    horizontalLayout.addWidget(get_mask_button)
    verticalLayout_8.addWidget(get_mask)

    get_mask.setTitle(_translate("MainWindow", "Mask File", None))
    get_mask_label.setText(_translate("MainWindow", "File Name", None))
    get_mask_line_edit.setText(_translate("MainWindow", "*.csv", None))
    get_mask_button.setText(_translate("MainWindow", "...", None))
    try:
        get_mask_button.clicked.connect(
            lambda: on_getDataButton_clicked(pysat_fun, get_mask_line_edit, "Known"))
    except:
        pass

def on_getDataButton_clicked(pysat_fun, lineEdit, key):
    filename = QtGui.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
    lineEdit.setText(filename)
    if lineEdit.text() == "":
        lineEdit.setText("*.csv")
    pysat_fun.do_mask(key, filename)
