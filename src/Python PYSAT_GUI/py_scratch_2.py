import sys
from PyQt4 import QtGui, QtCore
from pysat_ui import *
count = 1

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI(self)

    def initUI(self, MainWindow):
        pysat_ui.mainframe(self, MainWindow)
        Main.normalization_setup(self)
        centralwidget = QtGui.QWidget()

        self.add = QtGui.QPushButton("Add")
        self.add.clicked.connect(self.Add)
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.add, 0, 0)
        centralwidget.setLayout(self.grid)
        self.setCentralWidget(centralwidget)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Test")
        self.setStyleSheet("background-color:")
        self.show()


    def Add(self):
        global count

        b = Main.normalization_values(self)
        c = Main.normalization_ok(self)

        self.grid.addWidget(b)
        self.grid.addWidget(c)

    def normalization_setup(self):
        self.Normalization = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Normalization.setFont(font)
        self.Normalization.setObjectName(("Normalization"))
        self.verticalLayout_27 = QtGui.QVBoxLayout(self.Normalization)
        self.verticalLayout_27.setMargin(11)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(("verticalLayout_27"))
        self.verticalLayout_26 = QtGui.QVBoxLayout()
        self.verticalLayout_26.setMargin(11)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(("verticalLayout_26"))
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setMargin(11)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(("verticalLayout_22"))
        self.verticalLayout_26.addLayout(self.verticalLayout_22)
        self.verticalLayout_27.addLayout(self.verticalLayout_26)
        self.verticalLayout_8.addWidget(self.Normalization)

    def normalization_values(self):
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setMargin(11)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(("horizontalLayout_24"))
        self.norm_label_8 = QtGui.QLabel(self.Normalization)
        self.norm_label_8.setObjectName(("norm_label_8"))
        self.horizontalLayout_24.addWidget(self.norm_label_8)
        self.norm_spinBox_16 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_16.setMaximum(1000)
        self.norm_spinBox_16.setObjectName(("norm_spinBox_16"))
        self.horizontalLayout_24.addWidget(self.norm_spinBox_16)
        self.norm_spinBox_8 = QtGui.QSpinBox(self.Normalization)
        self.norm_spinBox_8.setMaximum(1000)
        self.norm_spinBox_8.setObjectName(("norm_spinBox_8"))
        self.horizontalLayout_24.addWidget(self.norm_spinBox_8)
        self.verticalLayout_22.addLayout(self.horizontalLayout_24)
        self.norm_label_8.setText(("MainWindow", "Value 8", None))


    def normalization_ok(self):
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setMargin(11)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(("horizontalLayout_25"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem)
        self.NormValuebutton = QtGui.QPushButton(self.Normalization)
        self.NormValuebutton.setObjectName(("NormValuebutton"))
        self.horizontalLayout_25.addWidget(self.NormValuebutton)
        self.verticalLayout_22.addLayout(self.horizontalLayout_25)
        self.NormValuebutton.setText(("MainWindow", "Add Value", None))
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()