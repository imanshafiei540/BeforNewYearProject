# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from QTree import Main
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 471)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(208, 208, 208);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 10, 131, 48))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(590, 10, 131, 48))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 741, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeView = Main(self.verticalLayoutWidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_4.addWidget(self.treeView)
        self.commandLinkButton.raise_()
        self.commandLinkButton_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.treeView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setStyleSheet(_fromUtf8("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.toolBar.setIconSize(QtCore.QSize(90, 70))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iman/Downloads/settings1.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/settings_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings_2.setIcon(icon1)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionSearch = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/search_icon3.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon2)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionHome = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/home_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon3)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/save_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/cut_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon5)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/copy_icon2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/exit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSettings_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.hide)
        QtCore.QObject.connect(self.commandLinkButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.show)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.hide)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL(_fromUtf8("triggered()")), self.copy )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "HideMenu", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "ShowMenu", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))
        self.actionSettings.setToolTip(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setText(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setToolTip(_translate("MainWindow", "Settings", None))
        self.actionSearch.setText(_translate("MainWindow", "search", None))
        self.actionSearch.setToolTip(_translate("MainWindow", "Search", None))
        self.actionHome.setText(_translate("MainWindow", "home", None))
        self.actionHome.setToolTip(_translate("MainWindow", "Home", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionSave.setToolTip(_translate("MainWindow", "Save", None))
        self.actionCut.setText(_translate("MainWindow", "cut", None))
        self.actionCut.setToolTip(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "copy", None))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))

    def openMenu(self, position):

        menu = QMenu()

        menu.addAction(self.tr("cut"))
        menu.addAction(self.tr("copy"))
        menu.addAction(self.tr("paste"))
        menu.addAction(self.tr("delete"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))



    def copy(self):
        instance = self.treeView
        PATH = instance.getFilePath()
        file = open('DB.txt', "w")
        file.write(PATH)
        file.close()


import iman_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

