import sys
from random import choice
from events import Events
events = Events(5, choice('abcdefg'))
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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            result = events.check_note('a')
        elif event.key() == QtCore.Qt.Key_B:
            result = events.check_note('b')
        elif event.key() == QtCore.Qt.Key_C:
            result = events.check_note('c')
        elif event.key() == QtCore.Qt.Key_D:
            result = events.check_note('d')
        elif event.key() == QtCore.Qt.Key_E:
            result = events.check_note('e')
        elif event.key() == QtCore.Qt.Key_F:
            result = events.check_note('f')
        elif event.key() == QtCore.Qt.Key_G:
            result = events.check_note('g')
        elif event.key() == QtCore.Qt.Key_Space:
            events.play_note(events.current_note)  # repete a nota

        if events.down_counter == 0: # acabou
             resultado = events.calculate_result()
             msgBox = QtGui.QMessageBox()
             msgBox.setText('You have scored %s%%' % str(resultado))
             msgBox.exec_()

#    def setupUi(self, Form):
#        Form.setObjectName(("Form"))
#        Form.resize(400, 300)
#        self.horizontalLayout = QtGui.QHBoxLayout(Form)
#        self.horizontalLayout.setObjectName(("horizontalLayout"))
#        self.verticalLayout = QtGui.QVBoxLayout()
#        self.verticalLayout.setObjectName(("verticalLayout"))
#        self.btnPlayChord = QtGui.QPushButton(Form)
#        self.btnPlayChord.setObjectName(("btnPlayChord"))
#        self.verticalLayout.addWidget(self.btnPlayChord)
#        self.horizontalLayout.addLayout(self.verticalLayout)
#        self.btnPlayChord.clicked.connect(self.play_current_note)

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
        self.btn_play_chord.clicked.connect(self.play_current_note)
        self.btn_shortcuts.clicked.connect(self.open_shortcuts)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_play_chord.setText(_translate("Form", "Play chord again (OR PRESS SPACE BAR)", None))
        self.btn_shortcuts.setText(_translate("Form", "Shorcuts", None))

    def play_current_note(self):
        events.play_note(events.current_note)

    def open_shortcuts(self):
        from frm_shortcuts import Ui_frm_shortcuts
        app = QtGui.QWidget(self)
        form = Ui_frm_shortcuts()
        form.setupUi(form)
        form.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = Ui_Form()
    Form.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
