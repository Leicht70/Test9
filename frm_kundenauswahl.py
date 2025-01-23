# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_kundenauswahl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_frm_kundenauswahl(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 391, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bt_ok = QPushButton(Form)
        self.bt_ok.setObjectName(u"bt_ok")
        self.bt_ok.setGeometry(QRect(10, 260, 75, 24))
        self.frm_kundenauswahl = QTableView(Form)
        self.frm_kundenauswahl.setObjectName(u"frm_kundenauswahl")
        self.frm_kundenauswahl.setGeometry(QRect(0, 40, 391, 211))
        self.bt_Abbruch = QPushButton(Form)
        self.bt_Abbruch.setObjectName(u"bt_Abbruch")
        self.bt_Abbruch.setGeometry(QRect(290, 260, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Bitte Kunden Auswehlen", None))
        self.bt_ok.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.bt_Abbruch.setText(QCoreApplication.translate("Form", u"Abbruch", None))
    # retranslateUi

