# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 42))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_menu = QPushButton(self.frame_2)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setGeometry(QRect(40, 10, 141, 41))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_menu.setFont(font)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 10, 271, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color:rgb(170, 170, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(0, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(170, 170, 255)\n"
"}\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_spisok = QPushButton(self.frame_4)
        self.pushButton_spisok.setObjectName(u"pushButton_spisok")
        self.pushButton_spisok.setGeometry(QRect(30, 50, 141, 41))
        self.pushButton_spisok.setMinimumSize(QSize(0, 40))
        self.pushButton_korzina = QPushButton(self.frame_4)
        self.pushButton_korzina.setObjectName(u"pushButton_korzina")
        self.pushButton_korzina.setGeometry(QRect(30, 120, 141, 41))
        self.pushButton_korzina.setMinimumSize(QSize(0, 40))
        self.pushButton_zakazi = QPushButton(self.frame_4)
        self.pushButton_zakazi.setObjectName(u"pushButton_zakazi")
        self.pushButton_zakazi.setGeometry(QRect(30, 190, 141, 41))
        self.pushButton_zakazi.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_poisk = QWidget()
        self.page_poisk.setObjectName(u"page_poisk")
        self.tableWidget = QTableWidget(self.page_poisk)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 80, 501, 341))
        self.tableWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.label = QLabel(self.page_poisk)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 141, 41))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_obnovi = QPushButton(self.page_poisk)
        self.pushButton_obnovi.setObjectName(u"pushButton_obnovi")
        self.pushButton_obnovi.setGeometry(QRect(410, 440, 111, 31))
        font3 = QFont()
        font3.setBold(True)
        self.pushButton_obnovi.setFont(font3)
        self.stackedWidget.addWidget(self.page_poisk)
        self.page_corzina = QWidget()
        self.page_corzina.setObjectName(u"page_corzina")
        self.label_2 = QLabel(self.page_corzina)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 171, 31))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.page_corzina)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 70, 221, 31))
        self.lineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.pushButton_poisc = QPushButton(self.page_corzina)
        self.pushButton_poisc.setObjectName(u"pushButton_poisc")
        self.pushButton_poisc.setGeometry(QRect(430, 70, 91, 31))
        self.pushButton_ophorm_zakaz = QPushButton(self.page_corzina)
        self.pushButton_ophorm_zakaz.setObjectName(u"pushButton_ophorm_zakaz")
        self.pushButton_ophorm_zakaz.setGeometry(QRect(390, 390, 131, 51))
        self.tableWidget_2 = QTableWidget(self.page_corzina)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 120, 501, 231))
        self.label_5 = QLabel(self.page_corzina)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 10, 151, 31))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_corzina)
        self.page_zakazi = QWidget()
        self.page_zakazi.setObjectName(u"page_zakazi")
        self.tableWidget_3 = QTableWidget(self.page_zakazi)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 120, 501, 281))
        self.label_3 = QLabel(self.page_zakazi)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 30, 271, 51))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_obnovi_2 = QPushButton(self.page_zakazi)
        self.pushButton_obnovi_2.setObjectName(u"pushButton_obnovi_2")
        self.pushButton_obnovi_2.setGeometry(QRect(390, 420, 111, 31))
        self.pushButton_obnovi_2.setFont(font3)
        self.stackedWidget.addWidget(self.page_zakazi)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_menu.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u041d\u042e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041a\u041a\u0410\u0423\u041d\u0422 \u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u0422\u0415\u041b\u042f", None))
        self.pushButton_spisok.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043d\u0438\u0433", None))
        self.pushButton_korzina.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.pushButton_zakazi.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"author_id", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"amount", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041f\u0418\u0421\u041e\u041a \u041a\u041d\u0418\u0413", None))
        self.pushButton_obnovi.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415 \u041a\u041d\u0418\u0413\u0418:", None))
        self.pushButton_poisc.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a", None))
        self.pushButton_ophorm_zakaz.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0424\u041e\u0420\u041c\u0418\u0422\u042c \u0417\u0410\u041a\u0410\u0417", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"title", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"author_id", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"price", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"amount", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u0420\u0417\u0418\u041d\u0410", None))
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"title", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"author", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"name_city", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"days_delivery", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"price", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0424\u041e\u0420\u041c\u041b\u0415\u041d\u041d\u042b\u0415 \u0417\u0410\u041a\u0410\u0417\u042b", None))
        self.pushButton_obnovi_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
    # retranslateUi

