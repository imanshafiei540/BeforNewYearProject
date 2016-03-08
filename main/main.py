import login, sys

from  PyQt4 import QtCore, QtGui

class main(login.Ui_MainWindow, QtGui.QMainWindow, QtGui.QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def run():
    app = QtGui.QApplication([])
    isinstance = main()
    isinstance.show()
    app.exec_()

if __name__ == '__main__':
    run()


