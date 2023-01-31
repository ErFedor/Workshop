# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_ErrForm(object):
    def setupUi(self, ErrForm):
        if not ErrForm.objectName():
            ErrForm.setObjectName(u"ErrForm")
        ErrForm.resize(227, 132)
        ErrForm.setMinimumSize(QSize(227, 132))
        ErrForm.setMaximumSize(QSize(227, 132))
        self.label = QLabel(ErrForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 101))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(ErrForm)

        QMetaObject.connectSlotsByName(ErrForm)
    # setupUi

    def retranslateUi(self, ErrForm):
        ErrForm.setWindowTitle(QCoreApplication.translate("ErrForm", u"\u041e\u0428\u0418\u0411\u041a\u0410!!!", None))
        self.label.setText(QCoreApplication.translate("ErrForm", u"\u041e\u0428\u0418\u0411\u041a\u0410!!!", None))
    # retranslateUi

