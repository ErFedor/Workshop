# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = "Erin Fedor"

import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore
from PySide6.QtCore import Qt

from ui.ui_order import Ui_OrderForm
from ui.ui_error import Ui_ErrForm

from db import DB_connecter
DB = DB_connecter('worker', 'worker')

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

class Error_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ErrForm()
        self.ui.setupUi(self)

class Order_Win(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_OrderForm()
        self.ui.setupUi(self)
        self.ui.OrderBut.clicked.connect(self.order_data)
        self.error = Error_Win()
        self.tableView = self.ui.tableView
        print(type(self.tableView))

    def order_data(self):
        self.data = DB.SelectOrder()
        self.model = TableModel(self.data)
        self.tableView.setModel(self.model)
        self.tableView.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Order_Win()
    window.show()

    sys.exit(app.exec())