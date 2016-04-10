# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
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

class Ui_signupwindow(object):
    def setupUi(self, signupwindow):
        signupwindow.setObjectName(_fromUtf8("signupwindow"))
        signupwindow.resize(208, 291)
        signupwindow.setStyleSheet(_fromUtf8("font: 11pt \"Agency FB\";\n"
"background-color: rgb(0, 170, 255);"))
        self.centralwidget = QtGui.QWidget(signupwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(20, 190, 171, 28))
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(22, 140, 161, 22))
        self.password.setObjectName(_fromUtf8("password"))
        self.email = QtGui.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(22, 90, 161, 22))
        self.email.setObjectName(_fromUtf8("email"))
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(22, 40, 161, 22))
        self.username.setObjectName(_fromUtf8("username"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label.setStyleSheet(_fromUtf8("font: 75 11pt \"Agency FB\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 161, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        signupwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(signupwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 208, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        signupwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(signupwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        signupwindow.setStatusBar(self.statusbar)

        self.retranslateUi(signupwindow)
        QtCore.QMetaObject.connectSlotsByName(signupwindow)
        QtCore.QObject.connect(self.signUpButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushInfo)

    def retranslateUi(self, signupwindow):
        signupwindow.setWindowTitle(_translate("signupwindow", "MainWindow", None))
        self.signUpButton.setText(_translate("signupwindow", "Sign Up", None))
        self.label.setText(_translate("signupwindow", "Username:", None))
        self.label_2.setText(_translate("signupwindow", "Email:", None))
        self.label_3.setText(_translate("signupwindow", "Password:", None))

    def pushInfo(self):
        file = open('passdict.txt', 'r')
        info = file.readlines()
        info = eval(info[0])
        print self.username.text()
        info[str(self.username.text())] =str(self.password.text())
        print info, type(info)
        file.close()
        file = open('passdict.txt', 'w')
        file.write(str(info))
        file.close()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    signupwindow = QtGui.QMainWindow()
    ui = Ui_signupwindow()
    ui.setupUi(signupwindow)
    signupwindow.show()
    sys.exit(app.exec_())

