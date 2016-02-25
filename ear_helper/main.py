import sys
from random import choice
from events import Events
events = Events(5, choice('abcdefg'))
from PyQt4 import QtCore, QtGui

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

    def setupUi(self, Form):
        Form.setObjectName(("Form"))
        Form.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.btnPlayChord = QtGui.QPushButton(Form)
        self.btnPlayChord.setObjectName(("btnPlayChord"))
        self.verticalLayout.addWidget(self.btnPlayChord)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.btnPlayChord.clicked.connect(self.play_current_note)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def play_current_note(self):
        events.play_note(events.current_note)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = Ui_Form()
    Form.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
