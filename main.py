from PyQt5.QtWidgets import QDialog,QTextEdit
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QTextEdit,QLineEdit
from PySide6 import QtSql
from lxml.html.builder import SELECT
from twisted.python.formmethod import Password
from frm_test6 import Ui_frm_test6
from frm_kundenauswahl import Ui_frm_kundenauswahl
from frm_kunden import Ui_frm_kunden
#from PySide6 import Database
#import MySQLdb as mdb
import sys
import mariadb



class Frm_kunden(QMainWindow, Ui_frm_kunden):
    def __init__(self):
        super(Frm_kunden,self).__init__()
        self.setupUi(self)
        self.Speichern.clicked.connect(self.connectDB)



    def connectDB(self):
        try:

#            db = mariadb.connect('localhost', 'root', '13577', 'tb_kunde')
            db =mariadb.connect(
                host='localhost',
                user='root',
                password="13577",
                database='ku'

            )
            QMessageBox.about(self, 'Connection', 'Successfully Connected To DB')

            cursor = db.cursor()
            firma=self.te_Firma.text()

            insert_query = "INSERT INTO tb_kunde (tb_Firma) VALUES (?)"
            values = (firma ["tb_Firma"])
            cursor.execute(insert_query,values)
            db.commit()
            result =cursor.fetchone()
            if result:
                QMessageBox.information(self,"ist gespeichert")
            else:
                QMessageBox.information(self,"nicht geklabt")
            db.commit()


        except mariadb.Error as e:
            QMessageBox.about(self, 'connection', 'Not Connected')
            sys.exit(1)


class Frm_kundenauswahl(QMainWindow, Ui_frm_kundenauswahl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Frm_test6(QMainWindow, Ui_frm_test6 ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_Angebote.clicked.connect(self.Angebote)
        self.bt_Kunde.clicked.connect(self.Kunden)
        self.bt_Liferanten.clicked.connect(self.connectDB)


    def Kunden(self):
        frm_kunden.show()


    def Angebote(self):
        frm_kundenauswahl.show()

    def connectDB(self):
        try:
#            db = mariadb.connect('localhost', 'root', '13577', 'tb_kunde')
            db = mariadb.connect(
                host='localhost',
                user='root',
                password="13577",
                database='ku'
            )
            QMessageBox.about(self, 'Connection', 'Successfully Connected To DB')



        except mariadb.Error as e:
            QMessageBox.about(self, 'connection', 'Not Connected')
            sys.exit(1)




app = QApplication(sys.argv)
frm_main =Frm_test6()
frm_main.show()
frm_kundenauswahl =Frm_kundenauswahl()
frm_kunden=Frm_kunden()
app.exec()
