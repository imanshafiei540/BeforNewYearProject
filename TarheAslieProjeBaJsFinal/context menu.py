'''import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

data = [
    ("Alice", [
        ("Keys", []),
        ("Purse", [
            ("Cellphone", [])
            ])
        ]),
    ("Bob", [
        ("Wallet", [
            ("Credit card", []),
            ("Money", [])
            ])
        ])
    ]

class Window(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        self.model = QStandardItemModel()
        self.addItems(self.model, data)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Object")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def addItems(self, parent, elements):

        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    def openMenu(self, position):

        menu = QMenu()

        menu.addAction(self.tr("cut"))
        menu.addAction(self.tr("copy"))
        menu.addAction(self.tr("paste"))
        menu.addAction(self.tr("delete"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())'''

import sys
from PyQt4 import QtGui, QtCore

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.model = QtGui.QStandardItemModel()

        for k in range(0, 4):
            parentItem = self.model.invisibleRootItem()
            for i in range(0, 4):
                item = QtGui.QStandardItem(QtCore.QString("item %0 %1").arg(k).arg(i))
                parentItem.appendRow(item)
                parentItem = item

        self.view = QtGui.QTreeView()
        self.view.setModel(self.model)
        self.view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

        self.setCentralWidget(self.view)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()