# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from PyQt4 import QtCore, QtGui
from search import Search
import os


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(762, 499)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(208, 208, 208);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 10, 131, 48))
        self.commandLinkButton.setStyleSheet(_fromUtf8("font: 16pt \"Agency FB\";"))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(590, 10, 131, 48))
        self.commandLinkButton_2.setStyleSheet(_fromUtf8("font: 15pt \"Agency FB\";"))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 741, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeView = Main(self.verticalLayoutWidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_4.addWidget(self.treeView)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 10, 331, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(self.verticalLayoutWidget_2)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)

        self.webView.load(QUrl('hello.html'))
        #self.webView.load(QUrl('main.html'))


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setStyleSheet(_fromUtf8("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.toolBar.setIconSize(QtCore.QSize(51, 55))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 762, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/settings_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        self.actionSettings_2.setIcon(icon)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionSearch = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/search_icon3.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon1)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionHome = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/home_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon2)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/save_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/cut_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/copy_icon2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/exit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/paste.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon7)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/delete.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon8)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionNewfolder = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/folder.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewfolder.setIcon(icon9)
        self.actionNewfolder.setObjectName(_fromUtf8("actionNewfolder"))
        self.actionHistory = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/history.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon10)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionRename = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/rename.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon11)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewfolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSettings_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.hide)
        QtCore.QObject.connect(self.commandLinkButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.show)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.hide)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.copy)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.paste)
        QtCore.QObject.connect(self.actionCut, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.cut)
        QtCore.QObject.connect(self.actionDelete, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.delete)
        QtCore.QObject.connect(self.actionNewfolder, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.newFolder)
        QtCore.QObject.connect(self.actionSearch, QtCore.SIGNAL(_fromUtf8("triggered()")), self.openSearch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "HideMenu", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "ShowMenu", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
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
        self.actionPaste.setText(_translate("MainWindow", "paste", None))
        self.actionDelete.setText(_translate("MainWindow", "delete", None))
        self.actionNewfolder.setText(_translate("MainWindow", "newfolder", None))
        self.actionHistory.setText(_translate("MainWindow", "history", None))
        self.actionRename.setText(_translate("MainWindow", "rename", None))




    def copyScript(self):
        self.webView.load(QUrl('copy.html'))
        print 1
    def cutScript(self):
        self.webView.load(QUrl('cut.html'))
    def pasteScript(self):
        self.webView.load(QUrl('paste.html'))





    def copy(self):
        print "copy"
        instance = self.treeView
        PATH = instance.getFilePath()
        file = open('DB.txt', "w")
        file.write(PATH)
        NAME = instance.getFileName()
        file.write("\n")
        file.write(NAME)
        file.write("\n")
        file.write("0")
        file.close()
        self.copyScript()


    def cut(self):
        print "cut"
        instance = self.treeView
        PATH = instance.getFilePath()
        file = open('DB.txt', "w")
        file.write(PATH)
        NAME = instance.getFileName()
        file.write("\n")
        file.write(NAME)
        file.write("\n")
        file.write("1")
        file.close()
        self.cutScript()

    def paste(self):
        print "paste"
        instance = self.treeView
        lastPATH = instance.getFilePath()
        file=open('DB.txt',"r")
        try:
            firstPATH=file.readline().strip()
            NAME=file.readline().strip()
            mode=file.readline()
            firstPATH=firstPATH.replace("/",'\\')
            lastPATH=str(lastPATH).replace("/",'\\')
            print firstPATH
            print NAME
            if(int(mode)==0):
                print "copy"
                if (os.path.isfile(str(firstPATH))):
                    print "file"
                    os.system("copy "+str(firstPATH)+" "+str(lastPATH))
                    print "copy "+str(firstPATH)+" "+str(lastPATH)
                else:
                    print "foldere"
                    os.system("md "+str(lastPATH)+'\\'+str(NAME))
                    print "md "+str(lastPATH)+'\\'+str(NAME)
                    os.system("copy "+str(firstPATH)+" "+str(lastPATH)+"\\"+str(NAME))
                    print "copy "+str(firstPATH)+" "+str(lastPATH)+"\\"+str(NAME)
                file.close()
            elif(int(mode)==1):
                print "cut"
                os.system("move "+str(firstPATH)+" "+str(lastPATH))
                print "move "+str(firstPATH)+" "+str(lastPATH)
                file.close()
        except:
            print "exception"

        self.pasteScript()

    def delete(self):
        instance =  self.treeView
        PATH = instance.getFilePath()
        new_path = str(PATH).replace('/', "\\")
        if (os.path.isfile(str(new_path))):

            if ' ' in str(new_path):

                os.system("DEL /F /Q /A " + '"' + str(new_path) + '"')

            else:

                os.system("DEL /F /Q /A " + str(new_path) )

        else:
            os.system('RD /S /Q ' + '"' + str(PATH) + '"')

    def newFolder(self):
        instance = self.treeView
        PATH = instance.getFilePath()
        PATH = instance.getFilePath()
        new_path = str(PATH).replace('/', "\\")
        if (os.path.isfile((str(new_path)))):
            print "khodet khari"
        else:

            os.system("md " +'"' + str(new_path) + "\New folder" + '"' )

    def openSearch(self):
        MainWindow = QtGui.QMainWindow()
        ui = Search()
        ui.setupUi(MainWindow)
        MainWindow.show()
        Error      #put the error to stay in window :) :D :P


from PyQt4 import QtWebKit
from QTree import Main
import iman_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

