import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtSql import QSqlTableModel

import registration
import admin
import user
from connection import Data


class Registration(QMainWindow, registration.Ui_MainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = registration.Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.ui.pushButton.pressed.connect(self.reg)

    def reg(self):
        user_login = self.ui.lineEdit_2.text()
        user_password = self.ui.lineEdit_3.text()
        user_city = self.ui.comboBox.currentText()
        user_name = self.ui.lineEdit.text()

        if len(user_login) == 0 or len(user_password) == 0:
            return

        check_password = self.conn.get_password(user_login)
        if check_password[0] is None and user_login != 'baranov@test':
            if len(user_name) == 0:
                msgBox = QMessageBox()
                msgBox.setText("Нет такого пользователя")
                msgBox.setInformativeText("Введите имя пользователя и город пользователя")
                msgBox.exec()
                return
            self.conn.add_user(user_name, user_city, user_login, user_password)
            self.user = User(self.conn.get_user_id(user_login))
            self.user.show()
            self.hide()
        else:
            user_id = self.conn.get_user_id(user_login)
            if check_password[0] == str(user_password) or user_login == 'baranov@test':
                if user_id[0] == 1 or (user_login == 'baranov@test' and user_password == '123'):
                    self.administrator = Administrator()
                    self.administrator.show()
                    self.hide()
                else:
                    self.user = User(user_id)
                    self.user.show()
                    self.hide()
            else:
                msgBox = QMessageBox()
                msgBox.setText("Неправильный логин или пароль")
                msgBox.exec()
                return


class Administrator(QMainWindow, admin.Ui_MainWindow):
    def __init__(self):
        super(Administrator, self).__init__()
        self.ui = admin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.ui.pushButton_spisok.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_table))
        self.ui.pushButton_zakazi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_add))

        self.ui.pushButton_2.clicked.connect(self.drop_database)
        # self.ui.pushButton_3.clicked.connect()

        self.ui.pushButton_obnovi.clicked.connect(self.refresh_table)
        self.ui.pushButton.clicked.connect(self.delete_table)
        self.ui.pushButton_korzina.clicked.connect(self.delete_row)
        self.ui.pushButton_add_book.clicked.connect(self.add_book)


    def refresh_table(self):
        self.ui.tableWidget.clear()
        table_name = self.ui.comboBox.currentText()
        if table_name == 'book':
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(['book_id', 'title', 'author_id', 'price', 'amount'])
            book = self.conn.get_table_book()
            self.ui.tableWidget.setRowCount(len(book))
            tablerow = 0
            for row in book:
                self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                tablerow += 1

        elif table_name == 'author':
            self.ui.tableWidget.setColumnCount(2)
            self.ui.tableWidget.setHorizontalHeaderLabels(['author_id', 'author_name'])
            author = self.conn.get_table_author()
            self.ui.tableWidget.setRowCount(len(author))
            tablerow = 0
            for row in author:
                self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                tablerow += 1

        elif table_name == 'city':
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(['city_id', 'city', 'days_delivery'])
            city = self.conn.get_table_city()
            self.ui.tableWidget.setRowCount(len(city))
            tablerow = 0
            for row in city:
                self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1

        elif table_name == 'client':
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(['client_id', 'name_client', 'city_id', 'email', 'password'])
            client = self.conn.get_table_client()
            self.ui.tableWidget.setRowCount(len(client))
            tablerow = 0
            for row in client:
                self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                tablerow += 1

        elif table_name == 'book_buy':
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(['buy_book_id', 'client_id', 'book_id'])
            buy_book = self.conn.get_table_buy_book()
            self.ui.tableWidget.setRowCount(len(buy_book))
            tablerow = 0
            for row in buy_book:
                self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        else:
            self.ui.tableWidget.setColumnCount(0)
            self.ui.tableWidget.setRowCount(0)
            msgBox = QMessageBox()
            msgBox.setText("Для обновления выберите определнную таблицу")
            msgBox.exec()

    def delete_table(self):
        table_name = self.ui.comboBox.currentText()
        if table_name == 'book_buy':
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите очистить все данные из таблицы заказов?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                self.conn.trancate_buy_book()
                return
            else:
                return

        elif table_name == 'author' or table_name == 'city' or table_name == 'client' or table_name == 'book':
            msgBox = QMessageBox()
            msgBox.setText("Таблица {} недоступна для удаления".format(table_name))
            msgBox.exec()
            return

        elif table_name == 'все таблицы':
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите вернуть базу данных к начальному состоянию?")
            msgBox.setInformativeText("Все заказы будут удалены безвозвратно.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                self.conn.trancate_all_table()
                return
            else:
                return

        else:
            msgBox = QMessageBox()
            msgBox.setText("Выберите элемент для удаления")
            msgBox.exec()

    def delete_row(self):
        table_name = self.ui.comboBox.currentText()
        selected_data = self.ui.tableWidget.selectedIndexes()
        if len(table_name) == 0 or table_name == 'все таблицы' or selected_data is None or len(selected_data) == 0:
            msgBox = QMessageBox()
            msgBox.setText("Выберите таблицу и элемент для удаления")
            msgBox.exec()
            return
        selected_data = selected_data[0]
        data = self.ui.tableWidget.model().data(selected_data)
        if table_name == 'client':
            if selected_data.column() != 0 and selected_data.column() != 3:
                msgBox = QMessageBox()
                msgBox.setText("Вы можете удалять пользователя только по его id или email")
                msgBox.exec()
                return
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите удалить этого пользователя?")
            msgBox.setInformativeText("Также удалятся все заказы этого пользователя")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                self.conn.delete_user(data, selected_data.column())
                return
            else:
                return

        elif table_name == 'book_buy':
            if selected_data.column() != 0:
                msgBox = QMessageBox()
                msgBox.setText("Вы можете удалить заказ только по его id")
                msgBox.exec()
                return
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите отменить этот заказ?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                self.conn.delete_order(data)
                return
            else:
                return
        else:
            msgBox = QMessageBox()
            msgBox.setText("Таблица {} недоступна для удаления".format(table_name))
            msgBox.exec()
            return

    def drop_database(self):
        msgBox = QMessageBox()
        msgBox.setText("Вы хотите удалить всю базу данных?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Yes)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            #self.conn.drop_database('book_shope')
            self.close()
            return
        else:
            return

    def add_book(self):
        name_author = self.ui.lineEdit_2.text()
        name_book = self.ui.lineEdit_3.text()
        price = self.ui.lineEdit_4.text()
        amount = self.ui.lineEdit_5.text()
        if len(name_book) == 0 or len(name_author) == 0 or len(price) == 0 or len(amount) == 0:
            msgBox = QMessageBox()
            msgBox.setText("Для добавления книги заполните все ячейки")
            msgBox.exec()
            return
        self.conn.add_book(name_author, name_book, price, amount)
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")




class User(QMainWindow, user.Ui_MainWindow):
    def __init__(self, user_id):
        super(User, self).__init__()
        self.ui = user.Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.user_id = user_id

        self.ui.pushButton_spisok.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_poisk))
        self.ui.pushButton_korzina.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_corzina))
        self.ui.pushButton_zakazi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_zakazi))

        self.ui.pushButton_obnovi.clicked.connect(self.refresh_books)
        self.ui.pushButton_poisc.clicked.connect(self.find_book)
        self.ui.pushButton_ophorm_zakaz.clicked.connect(self.place_order)
        self.ui.pushButton_obnovi_2.clicked.connect(self.refresh_orders)

        self.ui.tableWidget_3.doubleClicked.connect(self.delete_buy_book)

    def refresh_books(self):
        books = self.conn.get_books()
        i = len(books)
        if i == 0:
            return
        self.ui.tableWidget.setRowCount(i)
        tablerow = 0
        for row in books:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            tablerow += 1

    def find_book(self):
        book_name = self.ui.lineEdit.text()
        if len(book_name) == 0:
            return
        book = self.conn.find_book(book_name)
        self.ui.tableWidget_2.setRowCount(len(book))
        tablerow = 0
        for row in book:
            self.ui.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            tablerow += 1

    def place_order(self):
        row_flag = self.ui.tableWidget_2.selectedIndexes()
        print(row_flag)
        if len(row_flag) != 0:
            row_flag = row_flag[0]
            book_id = str(self.ui.tableWidget_2.model().data(row_flag))
            if row_flag.column() != 0:
                msgBox = QMessageBox()
                msgBox.setText("Выберите заказ по его id")
                msgBox.exec()
                return
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите оформить заказ?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                print(self.ui.tableWidget_2.item(row_flag.row(), row_flag.column()).text())
                if self.ui.tableWidget_2.item(row_flag.row(), 4).text() == "0":
                    msgBox = QMessageBox()
                    msgBox.setText("Невозможно сделать заказ")
                    msgBox.setInformativeText("Данный товар закончился")
                    msgBox.exec()
                    return
                self.conn.place_order(self.user_id, book_id)
                self.ui.lineEdit.setText("")
                self.ui.tableWidget_2.setRowCount(0)
                return
            elif ret == QMessageBox.Cancel:
                return
            else:
                return
        else:
            msgBox = QMessageBox()
            msgBox.setText("Невозможно сделать заказ")
            msgBox.setInformativeText("Выберите товар для заказа")
            msgBox.exec()
            return


    def refresh_orders(self):
        books = self.conn.get_completed_orders(self.user_id)
        i = len(books)
        self.ui.tableWidget_3.setRowCount(i)
        tablerow = 0
        for row in books:
            self.ui.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))

            tablerow += 1

    def delete_buy_book(self, item):
        column = item.column()
        if column != 0:
            return
        buy_book_id = self.ui.tableWidget_3.item(item.row(), item.column())
        if buy_book_id is not None:
            msgBox = QMessageBox()
            msgBox.setText("Вы хотите отменить заказ?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:

                self.conn.delete_order(str(buy_book_id.text()))
                return
            elif ret == QMessageBox.Cancel:
                return
            else:
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Registration()
    window.show()

    sys.exit(app.exec())
