# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/play.ui'
#
# Created: Thu Feb 25 17:08:08 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Form(QtGui.QWidget):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(391, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_result = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_result.setFont(font)
        self.lbl_result.setText(_fromUtf8(""))
        self.lbl_result.setObjectName(_fromUtf8("lbl_result"))
        self.verticalLayout.addWidget(self.lbl_result, QtCore.Qt.AlignHCenter)
        self.btn_play_chord = QtGui.QPushButton(Form)
        self.btn_play_chord.setObjectName(_fromUtf8("btn_play_chord"))
        self.verticalLayout.addWidget(self.btn_play_chord)
        self.lbl_chord = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_chord.setFont(font)
        self.lbl_chord.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_chord.setText(_fromUtf8(""))
        self.lbl_chord.setObjectName(_fromUtf8("lbl_chord"))
        self.verticalLayout.addWidget(self.lbl_chord, QtCore.Qt.AlignHCenter)
        self.btn_shortcuts = QtGui.QPushButton(Form)
        self.btn_shortcuts.setObjectName(_fromUtf8("btn_shortcuts"))
        self.verticalLayout.addWidget(self.btn_shortcuts, QtCore.Qt.AlignRight)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_play_chord.setText(_translate("Form", "Play chord again (OR PRESS SPACE BAR)", None))
        self.btn_shortcuts.setText(_translate("Form", "Shorcuts", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = Ui_Form()
    Form.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
