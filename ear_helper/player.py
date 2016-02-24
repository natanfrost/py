# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/play.ui'
#
# Created: Wed Feb 24 17:17:56 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pygame
from pygame import mixer, display, event
from os import path

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnPlayChord = QtGui.QPushButton(Form)
        self.btnPlayChord.setObjectName(_fromUtf8("btnPlayChord"))
        self.verticalLayout.addWidget(self.btnPlayChord)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnPlayChord.setText(_translate("Form", "Play chord", None))
        self.btnPlayChord.clicked.connect(self.play_note)

    def play_note(self):
        notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
        mixer.init()
        mixer.music.load(notes_folder.format(note='a'))
        mixer.music.play()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
