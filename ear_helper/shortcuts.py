# -*- coding: utf-8 -*-
"""Docstring."""
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


class Ui_frm_shortcuts(QtGui.QDialog):
    """Shortcuts form."""

    def __init__(self, parent=None):
        """Constructor."""
        super(Ui_frm_shortcuts, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, frm_shortcuts):
        """Set up the form UI."""
        frm_shortcuts.setObjectName(_fromUtf8("frm_shortcuts"))
        frm_shortcuts.resize(420, 145)
        frm_shortcuts.setFixedSize(420, 145)
        frm_shortcuts.setToolTip(_fromUtf8(""))
        frm_shortcuts.setAutoFillBackground(False)
        self.gridLayout_2 = QtGui.QGridLayout(frm_shortcuts)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_16 = QtGui.QLabel(frm_shortcuts)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 134, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        self.label_16.setPalette(palette)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 3, 0, 1, 1)
        self.btn_mi = QtGui.QPushButton(frm_shortcuts)
        self.btn_mi.setObjectName(_fromUtf8("btn_mi"))
        self.btn_mi.setToolTip(_fromUtf8("Push to play note"))
        self.btn_mi.clicked.connect(lambda: events.play_note('e'))
        self.gridLayout_5.addWidget(self.btn_mi, 0, 0, 1, 1)
        self.btn_fa = QtGui.QPushButton(frm_shortcuts)
        self.btn_fa.setObjectName(_fromUtf8("btn_fa"))
        self.btn_fa.setToolTip(_fromUtf8("Push to play note"))
        self.btn_fa.clicked.connect(lambda: events.play_note('f'))
        self.gridLayout_5.addWidget(self.btn_fa, 1, 0, 1, 1)
        self.btn_sol = QtGui.QPushButton(frm_shortcuts)
        self.btn_sol.setObjectName(_fromUtf8("btn_sol"))
        self.btn_sol.clicked.connect(lambda: events.play_note('g'))
        self.btn_sol.setToolTip(_fromUtf8("Push to play note"))
        self.gridLayout_5.addWidget(self.btn_sol, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 4, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_9 = QtGui.QLabel(frm_shortcuts)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(frm_shortcuts)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtGui.QLabel(frm_shortcuts)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(frm_shortcuts)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 3, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btn_la = QtGui.QPushButton(frm_shortcuts)
        self.btn_la.setToolTip(_fromUtf8("Push to play note"))
        self.btn_la.setObjectName(_fromUtf8("btn_la"))
        self.btn_la.clicked.connect(lambda: events.play_note('a'))
        self.gridLayout_3.addWidget(self.btn_la, 0, 0, 1, 1)
        self.btn_si = QtGui.QPushButton(frm_shortcuts)
        self.btn_si.setObjectName(_fromUtf8("btn_si"))
        self.btn_si.setToolTip(_fromUtf8("Push to play note"))
        self.btn_si.clicked.connect(lambda: events.play_note('b'))
        self.gridLayout_3.addWidget(self.btn_si, 1, 0, 1, 1)
        self.btn_do = QtGui.QPushButton(frm_shortcuts)
        self.btn_do.setObjectName(_fromUtf8("btn_do"))
        self.btn_do.setToolTip(_fromUtf8("Push to play note"))
        self.btn_do.clicked.connect(lambda: events.play_note('c'))
        self.gridLayout_3.addWidget(self.btn_do, 2, 0, 1, 1)
        self.btn_re = QtGui.QPushButton(frm_shortcuts)
        self.btn_re.setObjectName(_fromUtf8("btn_re"))
        self.btn_re.setToolTip(_fromUtf8("Push to play note"))
        self.btn_re.clicked.connect(lambda: events.play_note('d'))
        self.gridLayout_3.addWidget(self.btn_re, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(frm_shortcuts)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(frm_shortcuts)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(frm_shortcuts)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(frm_shortcuts)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(
            40, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)

        self.retranslateUi(frm_shortcuts)
        QtCore.QMetaObject.connectSlotsByName(frm_shortcuts)

    def retranslateUi(self, frm_shortcuts):
        """Reapaint UI."""
        frm_shortcuts.setWindowTitle(_translate(
            "frm_shortcuts", "Keyboard Shortcuts", None))
        self.label_16.setText(_translate("frm_shortcuts", "PLAY AGAIN", None))
        self.btn_mi.setText(_translate("frm_shortcuts", "MI", None))
        self.btn_fa.setText(_translate("frm_shortcuts", "FA", None))
        self.btn_sol.setText(_translate("frm_shortcuts", "SOL", None))
        self.label_9.setText(_translate("frm_shortcuts", "E", None))
        self.label_10.setText(_translate("frm_shortcuts", "F", None))
        self.label_11.setText(_translate("frm_shortcuts", "G", None))
        self.label_15.setText(_translate("frm_shortcuts", "SPACE", None))
        self.btn_la.setText(_translate("frm_shortcuts", "LA", None))
        self.btn_si.setText(_translate("frm_shortcuts", "SI", None))
        self.btn_do.setText(_translate("frm_shortcuts", "DO", None))
        self.btn_re.setText(_translate("frm_shortcuts", "RE", None))
        self.label.setText(_translate("frm_shortcuts", "A", None))
        self.label_3.setText(_translate("frm_shortcuts", "C", None))
        self.label_2.setText(_translate("frm_shortcuts", "B", None))
        self.label_4.setText(_translate("frm_shortcuts", "D", None))
