"""Creation of main form."""
import sys
import json
import xml.etree.ElementTree as ET
from os import path
from events import Events
from PyQt4 import QtCore, QtGui
from result import Result
events = Events()

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
    """Main Form."""

    def keyPressEvent(self, event):
        """Process any key press in the form."""
        if event.key() == QtCore.Qt.Key_Space:
            events.play_note(events.current_note)  # repeat chord
        else:
            self.process_keypress(QtGui.QKeySequence(event.key()).toString())

        if events.down_counter == 0:  # finished training
            resultado = events.calculate_result()
            msgBox = QtGui.QMessageBox()
            msgBox.setText('You have scored %s%% \nLongest Streak: %s' %
                           (str(resultado), events.longest_streak))
            msgBox.setWindowTitle('Final result')
            msgBox.exec_()
            self.lbl_result.setText('')
            self.lbl_chord.setText('')
            self.btn_play_chord.setText(
                _translate("Form", "Set up training", None))
            result = Result(events.quantity, events.hits,
                            events.longest_streak)
            self.serialize(result)
        else:
            events.play_random_note()  # play next random note

    def process_keypress(self, chord):
        """Process only the keys A, B, C, D, E, F, G."""
        if chord in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            self.display_result(chord, events.check_note(chord))

    def serialize(self, object):
        """Serialize Result object into a json file."""
        json_result = json.dumps(object.__dict__, indent=4)
        caminho = path.dirname(path.abspath(__file__)) + '/results.json'
        file = open(caminho, 'a')
        file.write(json_result + '\n')
        file.close()

    def write_xml_estatistic(self, chord, right):
        """Write into xml file statistics of use."""
        tree = ET.parse(path.dirname(
            path.abspath(__file__)) + '/estatistic.xml')
        root = tree.getroot()
        for child in root:
            if child.attrib['name'] == chord:
                if right is True:
                    for acertos in child.iter('right_times'):
                        acerto = int(acertos.text)
                        acertos.text = str(acerto + 1)
                else:
                    for erros in child.iter('wrong_times'):
                        erro = int(erros.text)
                        erros.text = str(erro + 1)
        tree.write(path.dirname(path.abspath(__file__)) + '/estatistic.xml')

    def display_result(self, my_chord, chord_result):
        """Display result after user choose a chord."""
        self.lbl_result.setText(chord_result)
        self.lbl_chord.setText(my_chord)
        # compare
        if self.lbl_chord.text() == self.lbl_result.text():
            self.lbl_result.setStyleSheet('QLabel { color: green }')
            self.write_xml_estatistic(my_chord, True)
        else:
            self.lbl_result.setStyleSheet('QLabel { color: red }')
            self.write_xml_estatistic(my_chord, False)

    def setupUi(self, Form):
        """Set up the form UI."""
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
        self.lbl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lbl_result)

        self.btn_play_chord = QtGui.QPushButton(Form)
        self.btn_play_chord.setObjectName(_fromUtf8("btn_play_chord"))
        self.verticalLayout.addWidget(self.btn_play_chord)

        self.lbl_chord = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_chord.setFont(font)
        self.lbl_chord.setText(_fromUtf8(""))
        self.lbl_chord.setObjectName(_fromUtf8("lbl_chord"))
        self.lbl_chord.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lbl_chord)

        self.btn_shortcuts = QtGui.QPushButton(Form)
        self.btn_shortcuts.setObjectName(_fromUtf8("btn_shortcuts"))
        self.verticalLayout.addWidget(self.btn_shortcuts, QtCore.Qt.AlignRight)
        self.btn_play_chord.clicked.connect(self.play_current_note)
        self.btn_shortcuts.clicked.connect(self.open_shortcuts)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """Repaint UI."""
        Form.setWindowTitle(_translate("Form", "Ear Training", None))
        self.btn_play_chord.setText(
            _translate("Form", "Set up training", None))
        self.btn_shortcuts.setText(_translate("Form", "Shorcuts", None))

    def play_current_note(self):
        """Set up the training or play current chord."""
        if 'Set up' in self.btn_play_chord.text():
            from set_up_training import Ui_Form
            Dialog = Ui_Form()
            Dialog.exec_()
            if Dialog.get_prepared() != 0:
                print Dialog.get_prepared()
                self.btn_play_chord.setText("Play again")
                events.set_up_training(Dialog.get_prepared())
        else:
            events.play_note(events.current_note)

    def open_shortcuts(self):
        """Open Shorcuts Form."""
        from shortcuts import Ui_frm_shortcuts
        Dialog = Ui_frm_shortcuts()
        Dialog.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = Ui_Form()
    Form.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
