import PyQt4, sys
from PyQt4 import QtGui, QtCore


class searchclass(QtGui.QWidget):


    def part1(self):

        self.text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        'Excisting Item: ')

        if ok:

            pass

    def part2(self):

        self.text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        'Not Exiisting Item: ')

        if ok:

            pass

    def part3(self):

        self.text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        'Two That You Want It or Sure: ')

        if ok:

            pass



