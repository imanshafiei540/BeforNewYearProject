import PyQt4, sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):


    def main(self):

        self.text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        'Rename Here : ')

        if ok:

            pass



