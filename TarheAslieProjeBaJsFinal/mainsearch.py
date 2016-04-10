# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainsearch.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_mainsearch(object):
    def setupUi(self, mainsearch):
        mainsearch.setObjectName(_fromUtf8("mainsearch"))
        mainsearch.resize(550, 475)
        mainsearch.setStyleSheet(_fromUtf8("font: 75 11pt \"Agency FB\";\n"
"background-color: rgb(1, 188, 255);"))
        self.centralwidget = QtGui.QWidget(mainsearch)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 531, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 491, 151))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 331, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 331, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 331, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 321, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 331, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 331, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalScrollBar = QtGui.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(490, 180, 16, 151))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        mainsearch.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainsearch)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainsearch.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainsearch)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(50, 45))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainsearch.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(mainsearch)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/exit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHome = QtGui.QAction(mainsearch)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/home_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon1)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(mainsearch)
        QtCore.QMetaObject.connectSlotsByName(mainsearch)

    def retranslateUi(self, mainsearch):
        mainsearch.setWindowTitle(_translate("mainsearch", "MainWindow", None))
        self.label.setText(_translate("mainsearch", "Part 1:", None))
        self.label_2.setText(_translate("mainsearch", "Part 2:", None))
        self.label_3.setText(_translate("mainsearch", "Part 3:", None))
        self.label_4.setText(_translate("mainsearch", "Result:", None))
        self.toolBar.setWindowTitle(_translate("mainsearch", "toolBar", None))
        self.actionExit.setText(_translate("mainsearch", "Exit", None))
        self.actionHome.setText(_translate("mainsearch", "Home", None))

import iman_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainsearch = QtGui.QMainWindow()
    ui = Ui_mainsearch()
    ui.setupUi(mainsearch)
    mainsearch.show()
    sys.exit(app.exec_())

