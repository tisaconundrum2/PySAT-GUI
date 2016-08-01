import sys
from PyQt4 import QtGui, QtCore

count = 1

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        centralwidget = QtGui.QWidget()
        self.add = QtGui.QPushButton("Add")
        self.add.clicked.connect(self.Add)
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.add, 0, 0)
        centralwidget.setLayout(self.grid)
        self.setCentralWidget(centralwidget)

        # ---------Window settings --------------------------------

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("")
        self.setWindowIcon(QtGui.QIcon(""))
        self.setStyleSheet("background-color:")
        self.show()

    def Add(self):
        global count
        b = QtGui.QPushButton(str(count), self)
        b.clicked.connect(self.Button)
        self.grid.addWidget(b, count, 0)
        count += 1

    def Button(self):
        sender = self.sender()
        print(sender.text())


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
