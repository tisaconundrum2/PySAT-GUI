import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SpinboxWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        # self.signalMapper = QSignalMapper(self)
        # self.signalMapper.mapped[str].connect(self.setspbMin)

        self.addSpinboxes(10)                                   # add an arbitrary number of spinboxes
        self.setLayout(self.layout)

    def addSpinboxes(self, n):
        spb = []
        self.layout.addWidget(QPushButton)

        for i in range(n):
            # objectname = 'spinbox_{}'.format(i)
            spinbox = QSpinBox()
            # spinbox.setObjectName(objectname)                 # to identify the spinbox later
            spinbox.setMaximum(1000)
            # spinbox.valueChanged.connect(self.signalMapper.map)
            # self.signalMapper.setMapping(spinbox, objectname) # sends the objectname with his mapped() signal
            spb.append(spinbox)                                 # added in edit
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