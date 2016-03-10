from PyQt4 import QtGui
from PyQt4 import QtCore

class Main(QtGui.QTreeView):

  def __init__(self,parent):

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

  def change_color(self, color):
      template_css = """
QTreeView {
    alternate-background-color: #ffffff;
    background: #e8f4fc;
    color:black;
}
"""
      css = template_css % color
      self.setStyleSheet(css) 

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())