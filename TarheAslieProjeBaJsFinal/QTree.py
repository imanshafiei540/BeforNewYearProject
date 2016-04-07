from PyQt4 import QtGui
from PyQt4 import QtCore
import pickle
import os

dir_list = []

class Main(QtGui.QTreeView):

    def __init__(self,parent=None):
        QtGui.QTreeView.__init__(self)
        self.treeview = QtGui.QTreeView(self)
        self.treeview.resize(730, 280)
        self.treeview.model = QtGui.QFileSystemModel()
        self.treeview.model.setRootPath( QtCore.QDir.currentPath() )
        self.treeview.setModel(self.treeview.model)
        self.treeview.setColumnWidth(0, 200)
        self.treeview.clicked.connect(self.get_file_path)
        self.treeview.doubleClicked.connect(self.test)
        self.treeview.doubleClicked.connect(self.writeToHistory)
        self.filePath = None



    def test(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())
        self.fileName = self.treeview.model.fileName(indexItem)
        self.filePath = self.treeview.model.filePath(indexItem)
        if (os.path.isfile(self.filePath)):
            path = str('"' + self.filePath + '"')
            os.system(str(path))
        else:
            pass

    def get_file_path(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())
        self.fileName = self.treeview.model.fileName(indexItem)
        self.filePath = self.treeview.model.filePath(indexItem)


    def getFilePath(self):
        return self.filePath
    def getFileName(self):
        return self.fileName

    def writeToHistory(self):
        file = open('History.txt', 'a')
        file.write(self.getFilePath() + '\n')
        file.close()





if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    w=Main()
    w.show()
    sys.exit(app.exec_())
