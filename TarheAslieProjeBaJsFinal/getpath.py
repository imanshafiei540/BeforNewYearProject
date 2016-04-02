from PyQt4 import QtGui
from PyQt4 import QtCore

# ---------------------------------------------------------------------
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.resize(600,400)
        self.setWindowTitle("Treeview Example")

        self.treeview = QtGui.QTreeView(self)

        self.treeview.model = QtGui.QFileSystemModel()
        self.treeview.model.setRootPath( QtCore.QDir.currentPath() )
        self.treeview.setModel(self.treeview.model)
        self.treeview.setColumnWidth(0, 200)

        self.setCentralWidget(self.treeview)

        self.treeview.clicked.connect(self.on_treeview_clicked)

# ---------------------------------------------------------------------

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())

        # path or filename selected
        fileName = self.treeview.model.fileName(indexItem)
        # full path/filename selected
        filePath = self.treeview.model.filePath(indexItem)

        print(fileName)
        print(filePath)

# ---------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())