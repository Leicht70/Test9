# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(1200, 800)
        font = QFont()
        font.setBold(False)
        frm_main.setFont(font)
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_offene_leistungen = QLabel(self.centralwidget)
        self.lb_offene_leistungen.setObjectName(u"lb_offene_leistungen")
        self.lb_offene_leistungen.setGeometry(QRect(0, 10, 1191, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.lb_offene_leistungen.setFont(font1)
        self.lb_offene_leistungen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_offene_rechnugen = QLabel(self.centralwidget)
        self.lb_offene_rechnugen.setObjectName(u"lb_offene_rechnugen")
        self.lb_offene_rechnugen.setGeometry(QRect(0, 360, 1191, 51))
        self.lb_offene_rechnugen.setFont(font1)
        self.lb_offene_rechnugen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tbl_offene_leistungen = QTableView(self.centralwidget)
        self.tbl_offene_leistungen.setObjectName(u"tbl_offene_leistungen")
        self.tbl_offene_leistungen.setGeometry(QRect(0, 50, 1191, 192))
        self.tbl_offene_rechnungen = QTableView(self.centralwidget)
        self.tbl_offene_rechnungen.setObjectName(u"tbl_offene_rechnungen")
        self.tbl_offene_rechnungen.setGeometry(QRect(0, 421, 1191, 271))
        self.bt_leistungen_erfassen = QPushButton(self.centralwidget)
        self.bt_leistungen_erfassen.setObjectName(u"bt_leistungen_erfassen")
        self.bt_leistungen_erfassen.setGeometry(QRect(60, 703, 161, 41))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.bt_leistungen_erfassen.setFont(font2)
        self.bt_rechnugen_erstellen = QPushButton(self.centralwidget)
        self.bt_rechnugen_erstellen.setObjectName(u"bt_rechnugen_erstellen")
        self.bt_rechnugen_erstellen.setGeometry(QRect(470, 700, 161, 41))
        self.bt_rechnugen_erstellen.setFont(font2)
        self.bt_zahlugen_erfassen = QPushButton(self.centralwidget)
        self.bt_zahlugen_erfassen.setObjectName(u"bt_zahlugen_erfassen")
        self.bt_zahlugen_erfassen.setGeometry(QRect(840, 700, 161, 41))
        self.bt_zahlugen_erfassen.setFont(font2)
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuQuit = QMenu(self.menubar)
        self.menuQuit.setObjectName(u"menuQuit")
        self.menuStammdaten = QMenu(self.menubar)
        self.menuStammdaten.setObjectName(u"menuStammdaten")
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        frm_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuStammdaten.menuAction())

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.lb_offene_leistungen.setText(QCoreApplication.translate("frm_main", u"Offene Leistung", None))
        self.lb_offene_rechnugen.setText(QCoreApplication.translate("frm_main", u"Offfene Rechnugen", None))
        self.bt_leistungen_erfassen.setText(QCoreApplication.translate("frm_main", u"Leistungen erfassen", None))
        self.bt_rechnugen_erstellen.setText(QCoreApplication.translate("frm_main", u"Rechnugen erstellen", None))
        self.bt_zahlugen_erfassen.setText(QCoreApplication.translate("frm_main", u"Zahlugen erfassen", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
        self.menuQuit.setTitle(QCoreApplication.translate("frm_main", u"Quit", None))
        self.menuStammdaten.setTitle(QCoreApplication.translate("frm_main", u"Stammdaten", None))
    # retranslateUi

