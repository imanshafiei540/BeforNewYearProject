# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(240, 280)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(74, 140, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(74, 175, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.loginLine = QtGui.QLineEdit(self.centralwidget)
        self.loginLine.setGeometry(QtCore.QRect(64, 50, 113, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.loginLine.setFont(font)
        self.loginLine.setAutoFillBackground(False)
        self.loginLine.setInputMask(_fromUtf8(""))
        self.loginLine.setText(_fromUtf8(""))
        self.loginLine.setFrame(True)
        self.loginLine.setEchoMode(QtGui.QLineEdit.Normal)
        self.loginLine.setDragEnabled(False)
        self.loginLine.setPlaceholderText(_fromUtf8(""))
        self.loginLine.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.loginLine.setObjectName(_fromUtf8("loginLine"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(64, 100, 113, 22))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8(""))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 80, 53, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "ورود", None))
        self.pushButton_2.setText(_translate("MainWindow", "ثبت نام", None))
        self.label.setText(_translate("MainWindow", "شماره دانشجویی:", None))
        self.label_2.setText(_translate("MainWindow", "رمز ورود:", None))




