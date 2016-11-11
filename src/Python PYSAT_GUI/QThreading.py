import time

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class MyCustomWidget(QtGui.QWidget):
    def __init__(self, parent = None):                              # initialize the object
        super(MyCustomWidget, self).__init__(parent)                # super?
        layout = QtGui.QVBoxLayout(self)                            # set up the layout for things to sit in

        self.progressBar = QtGui.QProgressBar(self)                 # setting up progress bar
        self.progressBar.setRange(0,1)                              # this stops pulsing green
        layout.addWidget(self.progressBar)                          # we add the progressbar to the layout
        button = QtGui.QPushButton("Start", self)                   # set up the button
        layout.addWidget(button)                                    # add the button to the layout

        button.clicked.connect(self.onStart)                        # when the button is clicked, start onStart function
        self.myLongTask = TaskThread()                              # Instantiate myLongTask as a TaskThread object
        self.myLongTask.taskFinished.connect(self.onFinished)       # TaskThread.taskFinished variable returns a boolean and calls self.onFinished function

    def onStart(self):                                              # onStart function
        self.progressBar.setRange(0,0)                              # make the bar pulse green
        self.myLongTask.start()                                     # TaskThread.start()
                                                                    # This is multithreading thus run() == start()

    def onFinished(self):                                           # onFinished function
        self.progressBar.setRange(0,1)                              # stop the bar pulsing green
        self.progressBar.setValue(1)                                # displays 100% after process is finished.

class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()                              # taskFinished is pyqtSignal function call
    def run(self):                                                  # this function is called by using start() because it is multithreading
        SomeOtherFunction.runme(self)
        self.taskFinished.emit()                                    # QtCore.pyqtSignal.emit variable returns a boolean

class SomeOtherFunction(object):                                    # test object to see if we can call classes outside of the Thread
    def runme(self):                                                # test function
        time.sleep(5)                                               # timeout for 5 seconds



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyCustomWidget()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
