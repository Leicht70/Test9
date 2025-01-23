# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_kunden.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_frm_kunden(object):
    def setupUi(self, frm_Kunden):
        if not frm_Kunden.objectName():
            frm_Kunden.setObjectName(u"frm_Kunden")
        frm_Kunden.resize(905, 722)
        font = QFont()
        font.setPointSize(15)
        frm_Kunden.setFont(font)
        self.tabWidget = QTabWidget(frm_Kunden)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 160, 557, 494))
        font1 = QFont()
        font1.setPointSize(13)
        self.tabWidget.setFont(font1)
        self.tab_Kontakt = QWidget()
        self.tab_Kontakt.setObjectName(u"tab_Kontakt")
        self.verticalLayout = QVBoxLayout(self.tab_Kontakt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_Firma = QLabel(self.tab_Kontakt)
        self.lb_Firma.setObjectName(u"lb_Firma")

        self.horizontalLayout_6.addWidget(self.lb_Firma)

        self.te_Firma = QTextEdit(self.tab_Kontakt)
        self.te_Firma.setObjectName(u"te_Firma")

        self.horizontalLayout_6.addWidget(self.te_Firma)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_Strasse = QLabel(self.tab_Kontakt)
        self.lb_Strasse.setObjectName(u"lb_Strasse")

        self.horizontalLayout_5.addWidget(self.lb_Strasse)

        self.le_Strasse = QLineEdit(self.tab_Kontakt)
        self.le_Strasse.setObjectName(u"le_Strasse")

        self.horizontalLayout_5.addWidget(self.le_Strasse)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_Adresse = QLabel(self.tab_Kontakt)
        self.lb_Adresse.setObjectName(u"lb_Adresse")

        self.horizontalLayout_4.addWidget(self.lb_Adresse)

        self.land = QSpinBox(self.tab_Kontakt)
        self.land.setObjectName(u"land")

        self.horizontalLayout_4.addWidget(self.land)

        self.le_PLZ = QLineEdit(self.tab_Kontakt)
        self.le_PLZ.setObjectName(u"le_PLZ")

        self.horizontalLayout_4.addWidget(self.le_PLZ)

        self.le_ort = QLineEdit(self.tab_Kontakt)
        self.le_ort.setObjectName(u"le_ort")

        self.horizontalLayout_4.addWidget(self.le_ort)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab_Kontakt)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.le_telefon = QLineEdit(self.tab_Kontakt)
        self.le_telefon.setObjectName(u"le_telefon")

        self.horizontalLayout_3.addWidget(self.le_telefon)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tab_Kontakt)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.le_mail = QLineEdit(self.tab_Kontakt)
        self.le_mail.setObjectName(u"le_mail")

        self.horizontalLayout_2.addWidget(self.le_mail)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.tab_Kontakt)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.le_Internet = QLineEdit(self.tab_Kontakt)
        self.le_Internet.setObjectName(u"le_Internet")

        self.horizontalLayout.addWidget(self.le_Internet)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Speichern = QPushButton(self.tab_Kontakt)
        self.Speichern.setObjectName(u"Speichern")


        self.verticalLayout.addWidget(self.Speichern)

        self.label_5 = QLabel(self.tab_Kontakt)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.tabWidget.addTab(self.tab_Kontakt, "")
        self.tab_Sonstiges = QWidget()
        self.tab_Sonstiges.setObjectName(u"tab_Sonstiges")
        self.tabWidget.addTab(self.tab_Sonstiges, "")
        self.tab_Internes = QWidget()
        self.tab_Internes.setObjectName(u"tab_Internes")
        self.tabWidget.addTab(self.tab_Internes, "")
        self.tab_Artikel = QWidget()
        self.tab_Artikel.setObjectName(u"tab_Artikel")
        self.tabWidget.addTab(self.tab_Artikel, "")
        self.widget = QWidget(frm_Kunden)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(220, 50, 290, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.retranslateUi(frm_Kunden)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_Kunden)
    # setupUi

    def retranslateUi(self, frm_Kunden):
        frm_Kunden.setWindowTitle(QCoreApplication.translate("frm_Kunden", u"Kunden", None))
        self.lb_Firma.setText(QCoreApplication.translate("frm_Kunden", u"Firma", None))
        self.lb_Strasse.setText(QCoreApplication.translate("frm_Kunden", u"Strasse", None))
        self.lb_Adresse.setText(QCoreApplication.translate("frm_Kunden", u"Land/PLZ/Ort", None))
        self.label_2.setText(QCoreApplication.translate("frm_Kunden", u"Telefon", None))
        self.label_3.setText(QCoreApplication.translate("frm_Kunden", u"E-Mail", None))
        self.label_4.setText(QCoreApplication.translate("frm_Kunden", u"Internet", None))
        self.Speichern.setText(QCoreApplication.translate("frm_Kunden", u"Speichern", None))
        self.label_5.setText(QCoreApplication.translate("frm_Kunden", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Kontakt), QCoreApplication.translate("frm_Kunden", u"Kontakt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Sonstiges), QCoreApplication.translate("frm_Kunden", u"Sonstiges", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Internes), QCoreApplication.translate("frm_Kunden", u"Internes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Artikel), QCoreApplication.translate("frm_Kunden", u"Artiekel", None))
        self.label.setText(QCoreApplication.translate("frm_Kunden", u"Kunden Nr.", None))
    # retranslateUi

