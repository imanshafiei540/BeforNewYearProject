# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SEARCH.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 611, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.openfile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.openfile.setObjectName(_fromUtf8("openfile"))
        self.verticalLayout.addWidget(self.openfile)
        self.selected_path = QtGui.QLineEdit(self.centralwidget)
        self.selected_path.setGeometry(QtCore.QRect(10, 290, 611, 31))
        self.selected_path.setObjectName(_fromUtf8("selected_path"))
        self.searchbox = QtGui.QLineEdit(self.centralwidget)
        self.searchbox.setGeometry(QtCore.QRect(10, 30, 341, 51))
        self.searchbox.setObjectName(_fromUtf8("searchbox"))
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(530, 30, 93, 51))
        self.search.setObjectName(_fromUtf8("search"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 291, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 381, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.results = QtGui.QTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(10, 120, 611, 131))
        self.results.setText(_fromUtf8(""))
        self.results.setObjectName(_fromUtf8("results"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(100, 65))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionHome = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/home_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/exit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSetting = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/BeforNewYearProject/settings_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon2)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSetting)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.searcher)
        QtCore.QObject.connect(self.openfile, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.openpath)
        QtCore.QObject.connect(self.actionHome, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.update)
        QtCore.QObject.connect(self.actionSetting, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.update)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.openfile.setText(_translate("MainWindow", "Open the file", None))
        self.search.setText(_translate("MainWindow", "search", None))
        self.label.setText(_translate("MainWindow", "Enter the file name that you want to search :", None))
        self.label_2.setText(_translate("MainWindow", "Suggestions : ", None))
        self.label_3.setText(_translate("MainWindow", "Copy the path from suggestions box and paste here :", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionHome.setText(_translate("MainWindow", "Home", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSetting.setText(_translate("MainWindow", "setting", None))

    def searcher(self):
        keyword=str(self.searchbox.text())
        import os
        import re
        print keyword
        os.system("c:")
        os.system("cd/")
        a=os.popen("dir "+ keyword+ " /s /p").read()
        print "dir"+ keyword+ " /s /p"
        print "a:"
        #print a
        print type(a)
        b=a.rsplit()
        print a.find("Directory of")
        print b
        c = [i for i, item in enumerate(b) if re.search('[A-Z]:\\\\', item)]
        print "c"
        paths=[b[i] for i in c]
        print paths
        if paths!=[]:
            lastresult=str(paths)[1:-1].replace(",","\\"+str(self.searchbox.text())+"\n").replace("\\\\","\\").replace("'","") +"\\"+str(self.searchbox.text())
            self.results.setText(lastresult)

    def openpath(self):
        path=str(self.selected_path.text())
        filename=str(self.searchbox.text())
        os.system(path)
        print path
import iman_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

