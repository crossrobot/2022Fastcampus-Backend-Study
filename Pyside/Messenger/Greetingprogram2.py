# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Greetingprogram2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_hi = QPushButton(self.centralwidget)
        self.btn_hi.setObjectName(u"btn_hi")
        self.btn_hi.setGeometry(QRect(350, 220, 75, 24))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(440, 160, 88, 20))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(280, 160, 88, 21))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(490, 280, 61, 20))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(370, 280, 73, 20))
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(250, 280, 73, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_hi.setText(QCoreApplication.translate("MainWindow", u" \uc778\uc0ac\ud558\uae30", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"radio2", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"radio1", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"chk3", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"chk2", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"chk1", None))
    # retranslateUi

