# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QModelIndex, Qt
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QModelIndex, Qt
import sys

from db import DB_connecter
DB = DB_connecter()

class OrderTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=[[]], parent=None):
        super().__init__(parent)
        self.data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ['ID_Order', 'Comment', 'Date', 'Cost']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]


    def columnCount(self, parent=None):
        # print(len(self.data[0]))
        return len(self.data[0])

    def rowCount(self, parent=None):
        # print(len(self.data))
        return len(self.data)

    def data(self, index: QModelIndex, role: int):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data[row][col])

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ['ID_Order', 'Comment', 'Date', 'Cost']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    data = DB.SelectOrder()
    print(data)
    model = TableModel(data)

    view = QtWidgets.QTableView()
    view.setModel(model)

    view.show()

    sys.exit(app.exec())