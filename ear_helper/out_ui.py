# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/player.ui'
#
# Created: Wed Feb 24 16:29:16 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(QtGui.QWidget):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog
    self.ui.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnPlay = QtGui.QPushButton(Form)
        self.btnPlay.setObjectName(_fromUtf8("btnPlay"))
        self.verticalLayout.addWidget(self.btnPlay)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Nothing ", None))
        self.btnPlay.setText(_translate("Form", "Play chord", None))
        self.btnPlay.clicked.connect(self.play_note)


    def play_note():
        notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
        mixer.init()
        mixer.music.load(notes_folder.format(note='a'))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
