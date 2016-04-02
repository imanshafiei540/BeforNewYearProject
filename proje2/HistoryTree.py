import sys
from PyQt4 import QtGui,QtCore

class Myview(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self)
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath('C:\Myfolder')
        self.view = QtGui.QTreeView()
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)

    def getModel(self):
        return self.model
    def getView(self):
        return self.view



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myview = Myview()
    myview.show()
    sys.exit(app.exec_())