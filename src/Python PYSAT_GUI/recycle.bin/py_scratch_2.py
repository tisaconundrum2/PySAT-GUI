import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QSpinBox
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QWidget


class SpinboxWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.addSpinboxes(10)
        self.setLayout(self.layout)

    def addSpinboxes(self, n):
        spb = []
        for i in range(n):
            spinbox = QSpinBox()
            spinbox.setMaximum(1000)
            spb.append(spinbox)
            self.layout.addWidget(spinbox)

        for i in range(n-1):
            spb[i].valueChanged.connect(spb[i + 1].setMinimum)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    widget = SpinboxWidget()
    widget.setWindowTitle('Spinbox Tester')
    widget.show()

sys.exit(app.exec_())