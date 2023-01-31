# -*- coding: utf-8 -*-
__author__ = "Erin Fedor"

import pyodbc
class DB_connecter():
    def __init__(self):
        self.connection = pyodbc.connect(r'Driver={SQL Server}; '
                                    r'Server=FEDOR\FEDORSQL; '
                                    r'Database=Workshop; '
                                    r'Trusted_Connection=yes;', autocommit=True)
        self.cursor = self.connection.cursor()
        print("Подключен к SQLite")

    def SelectClient(self):
        self.cursor.execute(f' SELECT (ID_Client) FROM [Client]')
        for row in self.cursor.columns(table='Client'):
            print(row.column_name)
            for field in row:
                print(field)




    def InsertClient(self, data):
        self.cursor.execute(f"INSERT INTO [Client] "
                            f"(FirstName, Surname, Patronymic, PhoneNumber, Email) "
                            f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')")
        ID_Client = self.cursor.execute(f'SELECT * FROM  [Client] WHERE ID_Client = (SELECT MAX(ID_Client)  FROM [Client])')
        ID_Client = ID_Client.fetchone()
        ID_Client = ID_Client[0]
        # print(ID_Client)
        return(ID_Client)



    def InsertOrder(self, data):
        self.cursor.execute(f"INSERT INTO [Order] "
                            f"(ID_Product, ID_Worker, Comment, Date, Cost) "
                            f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')")

        ID_Order = self.cursor.execute(
            f'SELECT * FROM  [Order] WHERE ID_Order = (SELECT MAX(ID_Order)  FROM [Order])')
        ID_Order = ID_Order.fetchone()
        ID_Order = ID_Order[0]
        # print(ID_Product)
        return (ID_Order)

    def InsertProductType(self, data):
        self.cursor.execute(f"INSERT INTO [ProductType] "
                            f"(TypeProduct, NameProduct, Material, Weight, ID_Client, ServiceType) "
                            f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')")
        ID_Product = self.cursor.execute(
            f'SELECT * FROM  [ProductType] WHERE ID_Product = (SELECT MAX(ID_Product)  FROM [ProductType])')
        ID_Product = ID_Product.fetchone()
        ID_Product = ID_Product[0]
        # print(ID_Product)
        return (ID_Product)



if __name__ == "__main__":
    name = 'Ivan'
    surname = 'Ivanov'
    patr = 'Ivanovich'
    phone = '999999999'
    email = 'rrrr@ttt.yy'

    client_data = (name, surname, patr, phone, email)
    DB = DB_connecter()
    DB.InsertClient(client_data)
    # DB.InsertClient(client_data)
