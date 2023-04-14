# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_OrderForm(object):
    def setupUi(self, OrderForm):
        if not OrderForm.objectName():
            OrderForm.setObjectName(u"OrderForm")
        OrderForm.resize(584, 296)
        OrderForm.setMinimumSize(QSize(584, 296))
        OrderForm.setMaximumSize(QSize(584, 296))
        self.widget = QWidget(OrderForm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 581, 291))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.OrderBut = QPushButton(self.widget)
        self.OrderBut.setObjectName(u"OrderBut")

        self.verticalLayout.addWidget(self.OrderBut)


        self.retranslateUi(OrderForm)

        QMetaObject.connectSlotsByName(OrderForm)
    # setupUi

    def retranslateUi(self, OrderForm):
        OrderForm.setWindowTitle(QCoreApplication.translate("OrderForm", u"Order", None))
        self.OrderBut.setText(QCoreApplication.translate("OrderForm", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u044b", None))
    # retranslateUi

