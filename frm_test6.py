# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_test6.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_frm_test6(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 746)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_Kunde = QPushButton(self.centralwidget)
        self.bt_Kunde.setObjectName(u"bt_Kunde")
        self.bt_Kunde.setGeometry(QRect(20, 30, 161, 71))
        font = QFont()
        font.setPointSize(20)
        self.bt_Kunde.setFont(font)
        self.bt_Liferanten = QPushButton(self.centralwidget)
        self.bt_Liferanten.setObjectName(u"bt_Liferanten")
        self.bt_Liferanten.setGeometry(QRect(200, 30, 161, 71))
        self.bt_Liferanten.setFont(font)
        self.bt_Artikel = QPushButton(self.centralwidget)
        self.bt_Artikel.setObjectName(u"bt_Artikel")
        self.bt_Artikel.setGeometry(QRect(370, 30, 161, 71))
        self.bt_Artikel.setFont(font)
        self.tab_Main = QTabWidget(self.centralwidget)
        self.tab_Main.setObjectName(u"tab_Main")
        self.tab_Main.setGeometry(QRect(10, 150, 1141, 501))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(False)
        self.tab_Main.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.bt_Angebote = QPushButton(self.tab)
        self.bt_Angebote.setObjectName(u"bt_Angebote")
        self.bt_Angebote.setGeometry(QRect(20, 40, 161, 71))
        self.bt_Angebote.setFont(font)
        self.bt_Aftrge = QPushButton(self.tab)
        self.bt_Aftrge.setObjectName(u"bt_Aftrge")
        self.bt_Aftrge.setGeometry(QRect(20, 130, 161, 71))
        self.bt_Aftrge.setFont(font)
        self.bt_Liferschein = QPushButton(self.tab)
        self.bt_Liferschein.setObjectName(u"bt_Liferschein")
        self.bt_Liferschein.setGeometry(QRect(20, 220, 161, 71))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        self.bt_Liferschein.setFont(font2)
        self.bt_Rechnugen = QPushButton(self.tab)
        self.bt_Rechnugen.setObjectName(u"bt_Rechnugen")
        self.bt_Rechnugen.setGeometry(QRect(20, 310, 161, 71))
        self.bt_Rechnugen.setFont(font2)
        self.tab_Main.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.bt_Buchaltung = QPushButton(self.tab_2)
        self.bt_Buchaltung.setObjectName(u"bt_Buchaltung")
        self.bt_Buchaltung.setGeometry(QRect(20, 30, 221, 71))
        self.bt_Buchaltung.setFont(font)
        self.bt_Beschtelugen = QPushButton(self.tab_2)
        self.bt_Beschtelugen.setObjectName(u"bt_Beschtelugen")
        self.bt_Beschtelugen.setGeometry(QRect(20, 120, 221, 71))
        self.bt_Beschtelugen.setFont(font)
        self.bt_Produktion = QPushButton(self.tab_2)
        self.bt_Produktion.setObjectName(u"bt_Produktion")
        self.bt_Produktion.setGeometry(QRect(20, 210, 221, 71))
        self.bt_Produktion.setFont(font)
        self.bt_Einkauf_4 = QPushButton(self.tab_2)
        self.bt_Einkauf_4.setObjectName(u"bt_Einkauf_4")
        self.bt_Einkauf_4.setGeometry(QRect(20, 320, 221, 71))
        self.bt_Einkauf_4.setFont(font2)
        self.tab_Main.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.bt_Lager = QPushButton(self.tab_3)
        self.bt_Lager.setObjectName(u"bt_Lager")
        self.bt_Lager.setGeometry(QRect(10, 20, 131, 71))
        self.bt_Lager.setFont(font)
        self.tab_Main.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.bt_Sonstiges = QPushButton(self.tab_4)
        self.bt_Sonstiges.setObjectName(u"bt_Sonstiges")
        self.bt_Sonstiges.setGeometry(QRect(20, 10, 161, 71))
        self.bt_Sonstiges.setFont(font)
        self.tab_Main.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_Main.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_Main.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tab_Main.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.tab_Main.raise_()
        self.bt_Kunde.raise_()
        self.bt_Liferanten.raise_()
        self.bt_Artikel.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 33))
        self.menuVerkauf = QMenu(self.menubar)
        self.menuVerkauf.setObjectName(u"menuVerkauf")
        self.menuEinkauf = QMenu(self.menubar)
        self.menuEinkauf.setObjectName(u"menuEinkauf")
        self.menuEinkauf.setFont(font)
        self.menuBuchhaltung = QMenu(self.menubar)
        self.menuBuchhaltung.setObjectName(u"menuBuchhaltung")
        self.menuZeiterfassung = QMenu(self.menubar)
        self.menuZeiterfassung.setObjectName(u"menuZeiterfassung")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuVerkauf.menuAction())
        self.menubar.addAction(self.menuEinkauf.menuAction())
        self.menubar.addAction(self.menuBuchhaltung.menuAction())
        self.menubar.addAction(self.menuZeiterfassung.menuAction())
        self.menuVerkauf.addSeparator()

        self.retranslateUi(MainWindow)

        self.tab_Main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_Kunde.setText(QCoreApplication.translate("MainWindow", u"Kunden", None))
        self.bt_Liferanten.setText(QCoreApplication.translate("MainWindow", u"Liferanten", None))
        self.bt_Artikel.setText(QCoreApplication.translate("MainWindow", u"Artikel", None))
        self.bt_Angebote.setText(QCoreApplication.translate("MainWindow", u"Angebote", None))
        self.bt_Aftrge.setText(QCoreApplication.translate("MainWindow", u"Aftr\u00e4ge", None))
        self.bt_Liferschein.setText(QCoreApplication.translate("MainWindow", u"Liferschein", None))
        self.bt_Rechnugen.setText(QCoreApplication.translate("MainWindow", u"Rechnugen", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Verkauf", None))
        self.bt_Buchaltung.setText(QCoreApplication.translate("MainWindow", u"Anfragen", None))
        self.bt_Beschtelugen.setText(QCoreApplication.translate("MainWindow", u"Beschtelugen", None))
        self.bt_Produktion.setText(QCoreApplication.translate("MainWindow", u"Wareneingag", None))
        self.bt_Einkauf_4.setText(QCoreApplication.translate("MainWindow", u"Eingangsrechnug", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Einkauf", None))
        self.bt_Lager.setText(QCoreApplication.translate("MainWindow", u"Lager", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Buchhaltung", None))
        self.bt_Sonstiges.setText(QCoreApplication.translate("MainWindow", u"Sonstiges", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Zeiterfassung", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Produktion", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Lager", None))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Sonstiges", None))
        self.menuVerkauf.setTitle(QCoreApplication.translate("MainWindow", u"Verkauf", None))
        self.menuEinkauf.setTitle(QCoreApplication.translate("MainWindow", u"Einkauf", None))
        self.menuBuchhaltung.setTitle(QCoreApplication.translate("MainWindow", u"Buchhaltung", None))
        self.menuZeiterfassung.setTitle(QCoreApplication.translate("MainWindow", u"Zeiterfassung", None))
    # retranslateUi

