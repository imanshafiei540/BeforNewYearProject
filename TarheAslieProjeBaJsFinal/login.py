# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import socket, json, sys, os
global data
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(231, 236)
        LoginWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        LoginWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 255);\n"
"font: 75 12pt \"Agency FB\";"))
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 140, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(40, 40, 151, 22))
        self.username.setObjectName(_fromUtf8("lineEdit"))
        self.password= QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(40, 100, 151, 22))
        self.password.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.sendInfo)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow", None))
        self.pushButton.setText(_translate("LoginWindow", "LOGIN", None))
        self.label.setText(_translate("LoginWindow", "Username:", None))
        self.label_2.setText(_translate("LoginWindow", "Password : ", None))
    def sendInfo(self):
        print self.username.text()
        print self.password
        print len(self.username.text())
        print self.username.text() == 'iman'
        userpass = open('userpass.txt', 'w')
        userpass.write(self.username.text()+'\n'+self.password.text())
        userpass.close()

        userpass = open('userpass.txt', 'r')
        UP = userpass.readlines()
        print UP
        UP[0] = UP[0].replace('\n', '')



        file = open('database.txt', 'w')

        lenght = network.recv(15)
        network.send('True')
        network.send(UP[0])
        network.send(UP[1])

        permission = network.recv(8)
        print permission
        print lenght
        if permission == 'accepted':
            for i in range(int(lenght)/20000 + 1):

                ln = network.recv(20000)
                file.write(ln)
                print ln
            file.close()


            permission = 1


            if permission:
                print 'hi'
                file = open('database.txt', 'r')
                data = file.readlines()
                print data
                print type(data[0])

                data = eval(data[0])

                window = Window()
                window.show()

            network.close



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

        indexes = self.treeView.selectedIndexes()
        if len(indexes) > 0:

            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1

        menu = QMenu()
        if level == 0:
            menu.addAction(self.tr("Edit person"))
        elif level == 1:
            menu.addAction(self.tr("Edit object/container"))
        elif level == 2:
            menu.addAction(self.tr("Edit object"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))



if __name__ == "__main__":
    import sys
    network = socket.socket()
    host = socket.gethostname()
    port = 5003
    network.connect((host, port))
    app = QtGui.QApplication(sys.argv)
    LoginWindow = QtGui.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()

    sys.exit(app.exec_())

