# -*- coding: utf-8 -*-
__author__ = "Erin Fedor"

import pyodbc
class DB_connecter():
    def __init__(self, username, password):
        self.connection = pyodbc.connect(r'Driver={SQL Server}; '
                                         r'Server=FEDOR\FEDORSQL; '
                                         r'Database=Workshop; '
                                         r'UID='+username+'; PWD='+password)
        self.cursor = self.connection.cursor()


    def SelectOrder(self):
        self.cursor.execute(f' SELECT ID_Order, Comment, Date, Cost '
                            f'FROM [Order]')
        self.dataOrder = self.cursor.fetchall()
        for i in range(len(self.dataOrder)):
            self.dataOrder[i][3] = str(self.dataOrder[i][3])
        return(self.dataOrder)

    def SelectCurrentOrder(self, ID_Product):
        self.cursor.execute(f' SELECT ID_Order, Comment, Date, Cost '
                            f'FROM [Order] '
                            f'WHERE ID_Product = {ID_Product}')
        self.data = self.cursor.fetchall()
        for i in range(len(self.data)):
            self.data[i][3] = str(self.data[i][3])
        return(self.data)


    def InsertClient(self, data):
        IsClientExists = self.cursor.execute(f" SELECT ID_Client FROM [Client]  "
                                             f"WHERE FirstName = '{data[0]}' "
                                             f"AND Surname = '{data[1]}' "
                                             f"AND Patronymic = '{data[2]}' ")
        IsClientExists = IsClientExists.fetchone()
        if IsClientExists != None:
            IsClientExists = IsClientExists[0]
            print(IsClientExists)
            return(IsClientExists)
        else:
            self.cursor.execute(f"INSERT INTO [Client] "
                                f"(FirstName, Surname, Patronymic, PhoneNumber, Email) "
                                f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')")

            ID_Client = self.cursor.execute(f'SELECT * FROM  [Client] '
                                            f'WHERE ID_Client = (SELECT MAX(ID_Client)  '
                                            f'FROM [Client])')
            ID_Client = ID_Client.fetchone()
            ID_Client = ID_Client[0]
            print(ID_Client)
            return(ID_Client)

    def InsertOrder(self, data):
        self.cursor.execute(f"INSERT INTO [Order] "
                            f"(ID_Product, ID_Worker, Comment, Date, Cost) "
                            f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')")

        ID_Order = self.cursor.execute(
            f'SELECT * FROM  [Order] '
            f'WHERE ID_Order = (SELECT MAX(ID_Order)  '
            f'FROM [Order])')
        ID_Order = ID_Order.fetchone()
        ID_Order = ID_Order[0]
        return (ID_Order)

    def InsertProductType(self, data):
        self.cursor.execute(f"INSERT INTO [ProductType] "
                            f"(TypeProduct, NameProduct, Material, Weight, ID_Client, ServiceType) "
                            f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')")
        ID_Product = self.cursor.execute(
            f'SELECT * FROM  [ProductType] '
            f'WHERE ID_Product = (SELECT MAX(ID_Product)  '
            f'FROM [ProductType])')
        ID_Product = ID_Product.fetchone()
        ID_Product = ID_Product[0]
        return (ID_Product)


if __name__ == "__main__":
    # name = 'Олег'
    # surname = 'Иванов'
    # patr = 'Иванович'
    # phone = '999999999'
    # email = 'rrrr@ttt.yy'
    #
    # client_data = (name, surname, patr, phone, email)
    # ID_Product = 2004
    DB = DB_connecter('client', 'client')
    # DB.SelectCurrentOrder(ID_Product)
    DB.SelectOrder()
