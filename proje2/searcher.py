import PyQt4, sys
from PyQt4 import QtGui, QtCore


class searchclass(QtGui.QWidget):


    def main(self):

        self.text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        'what do you want to be for sure?(separate with space): ')

        if ok:

            pass



