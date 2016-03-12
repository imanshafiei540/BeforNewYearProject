from PyQt4 import QtGui
from PyQt4 import QtCore

class Main(QtGui.QTreeView):

<<<<<<< HEAD
  def __init__(self,parent=None):

    QtGui.QTreeView.__init__(self)
    model = QtGui.QFileSystemModel()
    model.setRootPath( QtCore.QDir.currentPath() )
    self.setModel(model)
    QtCore.QObject.connect(self.selectionModel(), QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'), self.test)

  @QtCore.pyqtSlot("QItemSelection, QItemSelection")
  def test(self, selected, deselected):
      print("hello!")
      print(selected)
      print(deselected)
=======
    def __init__(self,parent):

        QtGui.QTreeView.__init__(self)
        self.treeview = QtGui.QTreeView(self)

        self.treeview.model = QtGui.QFileSystemModel()
        self.treeview.model.setRootPath( QtCore.QDir.currentPath() )
        self.treeview.setModel(self.treeview.model)
        self.treeview.setColumnWidth(0, 200)
        self.treeview.clicked.connect(self.test)
    @QtCore.pyqtSlot("QItemSelection, QItemSelection")
    def test(self,index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())

        # path or filename selected
        fileName = self.treeview.model.fileName(indexItem)
        # full path/filename selected
        filePath = self.treeview.model.filePath(indexItem)

        print(fileName)
        print(filePath)


>>>>>>> 06e63293eeca0fe108f54fab5f453e251f08fe19

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Main(None)
    w.show()
    sys.exit(app.exec_())
