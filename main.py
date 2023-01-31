# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = "Erin Fedor"

import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6 import QtCore
from db import DB_connecter

from ui.ui_last import Ui_LastForm
from ui.ui_first import Ui_FirstForm
from ui.ui_error import Ui_ErrForm

DB = DB_connecter()

class Error_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ErrForm()
        self.ui.setupUi(self)

class Last_Win(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_LastForm()
        self.ui.setupUi(self)
        self.ui.final_button.clicked.connect(self.save_data)
        self.error = Error_Win()

    def save_data(self):
        self.name = self.ui.name_edit.text()
        self.surname = self.ui.surname_edit.text()
        self.patr = self.ui.patr_edit.text()
        self.phone = self.ui.phone_edit.text()
        self.email = self.ui.email_edit.text()
        self.comment = self.ui.com_edit.toPlainText()

        # ПРОВЕРКА НА НЕЗАПОЛНЕННОСТЬ ЯЧЕЕК
        if (self.name and self.surname and self.phone and self.email) != '':
            client_data = (self.name, self.surname, self.patr, self.phone, self.email)
            self.ID_Client = DB.InsertClient(client_data)
            # print(self.ID_Client)
            self.close()
            window.close()
        else:
            self.error.show()

        self.TypeProduct = window.TypeProduct
        self.NameProduct = window.NameProduct
        self.Material = window.Material
        self.Weight = window.Weight
        self.ServiceType = window.ServiceType

        if (self.TypeProduct and self.NameProduct and self.Material and self.ServiceType) != '':
            product_data = (self.TypeProduct, self.NameProduct, self.Material, self.Weight, self.ID_Client, self.ServiceType)
            self.ID_Product = DB.InsertProductType(product_data)
            # print(self.ID_Product)
        else:
            self.error.show()

        # ORDER
        self.ID_Worker = 2
        self.date = datetime.now()
        self.Cost = 2000

        if (self.ID_Product and self.ID_Worker and self.date and self.Cost) != '':
            order_data = (self.ID_Product, self.ID_Worker, self.comment, self.date, self.Cost)
            self.ID_Order = DB.InsertOrder(order_data)
            print(self.ID_Order)
        else:
            self.error.show()


        # КОНЕЦ ПРОГИ

class First_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FirstForm()
        self.ui.setupUi(self)
        self.lastwin = None
        self.ui.nextButton.clicked.connect(self.next_win)
        self.error = Error_Win()

    def next_win(self):
        if not self.lastwin:
            self.lastwin = Last_Win(self)
        self.lastwin.show()
        self.save_data()

    def save_data(self):
        self.TypeProduct = self.ui.comboBox.currentText()
        self.NameProduct = self.ui.nameprod_edit.text()
        self.Material = self.ui.material_edit.text()
        self.Weight = self.ui.weight_edit.text()
        self.ServiceType = self.ui.checkBox.isChecked()

        if self.Weight == '':
            self.Weight = 0


        # if (TypeProduct and NameProduct and Material and ServiceType) != '':
        #     product_data = (TypeProduct, NameProduct, Material, Weight, ID_Client, ServiceType)
        #     ID_Product = DB.InsertProductType(product_data)
        #     print(ID_Product)
        # else:
        #     self.error.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = First_Win()
    window.show()

    sys.exit(app.exec())