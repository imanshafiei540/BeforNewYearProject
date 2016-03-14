from PyQt4 import QtGui
from PyQt4 import QtCore
import os
class Main(QtGui.QTreeView):

  def __init__(self,parent):

    QtGui.QTreeView.__init__(self)

    self.treeview = QtGui.QTreeView(self)
    self.treeview.model = QtGui.QFileSystemModel()
    self.treeview.model.setRootPath( QtCore.QDir.currentPath() )
    self.treeview.setModel(self.treeview.model)
    self.treeview.setColumnWidth(0, 200)
    self.treeview.clicked.connect(self.test)




  @QtCore.pyqtSlot("QItemSelection, QItemSelection")
  def test2(self, selected, deselected):
      print("hello!")
      print(selected)
      print(deselected)

  @QtCore.pyqtSlot("QItemSelection, QItemSelection")
  def test(self, index):
      indexItem = self.treeview.model.index(index.row(), 0, index.parent())

      # path or filename selected
      fileName = self.treeview.model.fileName(indexItem)
      # full path/filename selected
      filePath = self.treeview.model.filePath(indexItem)

      print(fileName)
      print(filePath)
      print(os.path.isfile(filePath))
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Main(None)
    w.show()
    sys.exit(app.exec_())
