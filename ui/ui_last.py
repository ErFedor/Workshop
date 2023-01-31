# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'last.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_LastForm(object):
    def setupUi(self, LastForm):
        if not LastForm.objectName():
            LastForm.setObjectName(u"LastForm")
        LastForm.resize(275, 426)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LastForm.sizePolicy().hasHeightForWidth())
        LastForm.setSizePolicy(sizePolicy)
        LastForm.setMinimumSize(QSize(0, 0))
        LastForm.setMaximumSize(QSize(333, 500))
        self.widget = QWidget(LastForm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 258, 419))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.name_edit = QLineEdit(self.widget)
        self.name_edit.setObjectName(u"name_edit")

        self.gridLayout.addWidget(self.name_edit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.surname_edit = QLineEdit(self.widget)
        self.surname_edit.setObjectName(u"surname_edit")

        self.gridLayout.addWidget(self.surname_edit, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.patr_edit = QLineEdit(self.widget)
        self.patr_edit.setObjectName(u"patr_edit")

        self.gridLayout.addWidget(self.patr_edit, 3, 2, 1, 1)

        self.phone_label = QLabel(self.widget)
        self.phone_label.setObjectName(u"phone_label")

        self.gridLayout.addWidget(self.phone_label, 4, 0, 1, 1)

        self.phone_edit = QLineEdit(self.widget)
        self.phone_edit.setObjectName(u"phone_edit")

        self.gridLayout.addWidget(self.phone_edit, 4, 1, 1, 2)

        self.email_label = QLabel(self.widget)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 5, 0, 1, 1)

        self.email_edit = QLineEdit(self.widget)
        self.email_edit.setObjectName(u"email_edit")

        self.gridLayout.addWidget(self.email_edit, 5, 1, 1, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 3)

        self.com_edit = QTextEdit(self.widget)
        self.com_edit.setObjectName(u"com_edit")

        self.gridLayout.addWidget(self.com_edit, 7, 0, 1, 3)

        self.final_button = QPushButton(self.widget)
        self.final_button.setObjectName(u"final_button")

        self.gridLayout.addWidget(self.final_button, 8, 0, 1, 1)


        self.retranslateUi(LastForm)

        QMetaObject.connectSlotsByName(LastForm)
    # setupUi

    def retranslateUi(self, LastForm):
        LastForm.setWindowTitle(QCoreApplication.translate("LastForm", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_5.setText(QCoreApplication.translate("LastForm", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043f\u043e\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("LastForm", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("LastForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("LastForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e(\u0415\u0441\u043b\u0438 \u0438\u043c\u0435\u0435\u0442\u0441\u044f)", None))
        self.phone_label.setText(QCoreApplication.translate("LastForm", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.email_label.setText(QCoreApplication.translate("LastForm", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("LastForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 (\u041d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)", None))
        self.final_button.setText(QCoreApplication.translate("LastForm", u"\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi

