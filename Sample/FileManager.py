#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(600, 600)
        self.setWindowTitle('FoVi Sorter')
        exit = QtGui.QAction('show', self)
        exit.setShortcut('Ctrl+R')
        exit.setStatusTip('close the program')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        settings = QtGui.QAction('Settings', self)
        settings.setStatusTip('rename')

        self.statusBar()
        menubar = self.menuBar()
        file = menubar.addMenu('file')
        file.addAction(exit)
        options = menubar.addMenu('option')
        options.addAction(settings)

        self.mainWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.optionsWidget = QtGui.QWidget(self)

        files_list = QtGui.QListWidget()
        select_path_label = QtGui.QLabel("target directory")
        dest_path_edit = QtGui.QLineEdit()
        select_path = QtGui.QPushButton("fehrest")
        description_label = QtGui.QLabel("be har dalil bara aks va ya film gerefte shod.")
        description_edit = QtGui.QLineEdit()
        start = QtGui.QPushButton("copy and start to rename")

        self.fileBrowserWidget = QtGui.QWidget(self)

        self.dirmodel = QtGui.QFileSystemModel()
        # Don't show files, just folders
        self.dirmodel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)

        self.folder_view = QtGui.QTreeView(parent=self);
        self.folder_view.setModel(self.dirmodel)
        self.folder_view.clicked[QtCore.QModelIndex].connect(self.clicked)
        # Don't show columns for size, file type, and last modified
        self.folder_view.setHeaderHidden(True)
        self.folder_view.hideColumn(1)
        self.folder_view.hideColumn(2)
        self.folder_view.hideColumn(3)


        self.selectionModel = self.folder_view.selectionModel()

        self.filemodel = QtGui.QFileSystemModel()
        # Don't show folders, just files
        self.filemodel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)

        self.file_view = QtGui.QListView(parent=self);
        self.file_view.setModel(self.filemodel)


        group_input = QtGui.QGroupBox()
        grid_input = QtGui.QGridLayout()

        splitter_filebrowser = QtGui.QSplitter()
        splitter_filebrowser.addWidget(self.folder_view)
        splitter_filebrowser.addWidget(self.file_view)
        splitter_filebrowser.setStretchFactor(0,2)
        splitter_filebrowser.setStretchFactor(1,4)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(splitter_filebrowser)
        self.fileBrowserWidget.setLayout(hbox)

        grid_input.addWidget(select_path_label, 0, 0)
        grid_input.addWidget(dest_path_edit, 1, 0)
        grid_input.addWidget(select_path, 1, 1)
        grid_input.addWidget(description_label, 2, 0)
        grid_input.addWidget(description_edit, 3, 0)
        grid_input.addWidget(start, 3, 1)
        group_input.setLayout(grid_input)

        vbox_options = QtGui.QVBoxLayout(self.optionsWidget)
        vbox_options.addWidget(files_list)
        vbox_options.addWidget(group_input)
        self.optionsWidget.setLayout(vbox_options)

        splitter_filelist = QtGui.QSplitter()
        splitter_filelist.setOrientation(QtCore.Qt.Vertical)
        splitter_filelist.addWidget(self.fileBrowserWidget)
        splitter_filelist.addWidget(self.optionsWidget)
        vbox_main = QtGui.QVBoxLayout(self.mainWidget)
        vbox_main.addWidget(splitter_filelist)
        vbox_main.setContentsMargins(0,0,0,0)
        #self.setLayout(vbox_main)

    def set_path(self):
        self.dirmodel.setRootPath("")

    def clicked(self, index):

        index = self.selectionModel.currentIndex()
        dir_path = self.dirmodel.filePath(index)
        self.filemodel.setRootPath(dir_path)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
main.set_path()

sys.exit(app.exec_())