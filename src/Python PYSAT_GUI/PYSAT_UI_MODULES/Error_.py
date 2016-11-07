from PyQt4.QtGui import QMessageBox

def error_print(message):
    print(message)
    try:
        """
        Warning Message Box
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    except:
        pass