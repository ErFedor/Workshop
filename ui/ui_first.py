# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_FirstForm(object):
    def setupUi(self, FirstForm):
        if not FirstForm.objectName():
            FirstForm.setObjectName(u"FirstForm")
        FirstForm.resize(279, 184)
        FirstForm.setMinimumSize(QSize(279, 184))
        FirstForm.setMaximumSize(QSize(279, 184))
        self.label = QLabel(FirstForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 21))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)
        self.layoutWidget = QWidget(FirstForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 41, 261, 138))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)

        self.nameprod_edit = QLineEdit(self.layoutWidget)
        self.nameprod_edit.setObjectName(u"nameprod_edit")

        self.gridLayout.addWidget(self.nameprod_edit, 1, 4, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)

        self.material_edit = QLineEdit(self.layoutWidget)
        self.material_edit.setObjectName(u"material_edit")

        self.gridLayout.addWidget(self.material_edit, 2, 2, 1, 3)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.weight_edit = QLineEdit(self.layoutWidget)
        self.weight_edit.setObjectName(u"weight_edit")

        self.gridLayout.addWidget(self.weight_edit, 3, 1, 1, 4)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 3)

        self.nextButton = QPushButton(self.layoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.gridLayout.addWidget(self.nextButton, 4, 3, 1, 2)


        self.retranslateUi(FirstForm)

        QMetaObject.connectSlotsByName(FirstForm)
    # setupUi

    def retranslateUi(self, FirstForm):
        FirstForm.setWindowTitle(QCoreApplication.translate("FirstForm", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0430\u043d\u043a\u0435\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("FirstForm", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0431 \u0438\u0437\u0434\u0435\u043b\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("FirstForm", u"\u0422\u0438\u043f \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("FirstForm", u"\u041c\u0435\u0442\u0430\u043b\u043b\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("FirstForm", u"\u0414\u0435\u0440\u0435\u0432\u044f\u043d\u043d\u043e\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u0435", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("FirstForm", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.label_3.setText(QCoreApplication.translate("FirstForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0437\u0434\u0435\u043b\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("FirstForm", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.label_5.setText(QCoreApplication.translate("FirstForm", u"\u0412\u0435\u0441", None))
        self.checkBox.setText(QCoreApplication.translate("FirstForm", u"\u041f\u043e\u0447\u0438\u043d\u043a\u0430", None))
        self.nextButton.setText(QCoreApplication.translate("FirstForm", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

