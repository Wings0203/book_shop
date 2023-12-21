# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(140, 170, 501, 341))
        self.groupBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 100, 71, 21))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgb(178, 186, 255)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 20, 201, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:rgb(178, 186, 255)")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 160, 71, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color:rgb(178, 186, 255)")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 190, 71, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color:rgb(178, 186, 255)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 130, 71, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color:rgb(178, 186, 255)")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 100, 241, 21))
        self.lineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 160, 241, 21))
        self.lineEdit_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 190, 241, 21))
        self.lineEdit_3.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 260, 151, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"\n"
"background-color:rgb(255, 0, 255);\n"
"")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 130, 241, 21))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 50, 621, 71))
        font3 = QFont()
        font3.setPointSize(17)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color:rgb(163, 97, 255)")
        self.label_6.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Personal diary", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041c\u042f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0425\u041e\u0414 \u0412 \u0410\u041a\u041a\u0410\u0423\u041d\u0422", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u041e\u0413\u0418\u041d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0410\u0420\u041e\u041b\u042c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041e\u0420\u041e\u0414", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0437\u0430\u043d\u044c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u043c\u0441\u043a", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0435\u0440\u0433", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0434\u0438\u0432\u043e\u0441\u0442\u043e\u043a", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u0430\u0440\u0430", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043b\u044f\u0431\u0438\u043d\u0441\u043a", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0420\u041e \u041f\u041e\u0416\u0410\u041b\u041e\u0412\u0410\u0422\u042c \u0412 BOOK_SHOP", None))
    # retranslateUi

