# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = "Erin Fedor"

import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6 import QtCore
from PySide6.QtCore import Qt
from db import DB_connecter

from ui.ui_last import Ui_LastForm
from ui.ui_first import Ui_FirstForm
from ui.ui_error import Ui_ErrForm
from ui.ui_order import Ui_OrderForm

DB = DB_connecter('client', 'client')

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        print(self._data)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ['ID_Order', 'Comment', 'Date', 'Cost']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class Order_Win(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_OrderForm()
        self.ui.setupUi(self)
        self.ui.OrderBut.clicked.connect(self.order_data)
        self.error = Error_Win()
        self.tableView = self.ui.tableView
        print(type(self.tableView))


    def order_data(self):
        print('ORDER')
        self.ID_Product = window2.ID_Product
        self.data = DB.SelectCurrentOrder(self.ID_Product)
        self.model = TableModel(self.data)
        self.tableView.setModel(self.model)
        self.tableView.show()

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
        if (self.name and self.surname and self.phone) != '':
            client_data = (self.name, self.surname, self.patr, self.phone, self.email)
            self.ID_Client = DB.InsertClient(client_data)
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
            window3.show()
        else:
            self.error.show()

        # КОНЕЦ ПРОГИ

class First_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_FirstForm()
        self.ui.setupUi(self)
        self.ui.nextButton.clicked.connect(self.next_win)
        self.error = Error_Win()

    def next_win(self):
        window2.show()
        self.save_data()

    def save_data(self):
        self.TypeProduct = self.ui.comboBox.currentText()
        self.NameProduct = self.ui.nameprod_edit.text()
        self.Material = self.ui.material_edit.text()
        self.Weight = self.ui.weight_edit.text()
        self.ServiceType = self.ui.checkBox.isChecked()
        if self.Weight == '':
            self.Weight = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = First_Win()
    window2 = Last_Win()
    window3 = Order_Win()
    window.show()

    sys.exit(app.exec())