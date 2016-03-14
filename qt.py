class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.treeview = QTreeView(self)
        # Setting the treeview model
        self.treeview.setAlternatingRowColors(True)
