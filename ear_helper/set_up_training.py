from PyQt4 import QtCore, QtGui
from events import Events
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

class Ui_Form(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.prepared = 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(255, 100)
        Form.setFixedSize(255, 100)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 241, 31))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 241, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txt_quantity = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.txt_quantity.setMaxLength(2)
        self.txt_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_quantity.setObjectName(_fromUtf8("txt_quantity"))
        self.txt_quantity.setValidator(QtGui.QIntValidator(0, 99, self))
        self.txt_quantity.setText('0')
        self.txt_quantity.selectAll()
        self.horizontalLayout.addWidget(self.txt_quantity)
        self.btn_start = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.btn_start.clicked.connect(self.update_btn_play_chord_text)
        self.horizontalLayout.addWidget(self.btn_start)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def update_btn_play_chord_text(self):
        if self.txt_quantity.text() == '':
            self.prepared = 0
        else:
            self.prepared = (int)(self.txt_quantity.text())
        self.close()

    def get_prepared(self):
        return self.prepared

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Training settings", None))
        self.label.setText(_translate("Form", "How many times do you want to try:", None))
        self.btn_start.setText(_translate("Form", "Start", None))
