import psycopg2
import os


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.conn_params = {
            "host": "localhost",
            "port": 5432,
            "database": "book_shop",
            "user": "postgres",
            "password": "postgres"
        }
        self.conn = psycopg2.connect(**self.conn_params)
        self.create_connection()

    def create_connection(self):
        # Параметры подключения к базе данных
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='book_shop'")
        exists = cursor.fetchone()
        if not exists:
            # Определяем путь к файлу user.sql
            file_path_user = os.path.join(os.path.dirname(__file__), "user.sql")
            file_path_createdb = os.path.join(os.path.dirname(__file__), "createdb.sql")
            file_path_admin = os.path.join(os.path.dirname(__file__), "admin.sql")
            # Открываем файл и выполняем запросы
            with open(file_path_createdb, "r") as f:
                cursor.execute(f.read())
                self.conn.commit()

            cursor.callproc('f_create_db', ['book_shop'])
            self.conn.commit()
            cursor.callproc('create_all_table', [])
            self.conn.commit()

            with open(file_path_user, "r") as f:
                cursor.execute(f.read())
                self.conn.commit()

            with open(file_path_admin, "r") as f:
                cursor.execute(f.read())
                self.conn.commit()

            # Закрываем соединение с базой данных
            cursor.close()
            self.conn.close()

            print("Файлы user.sql успешно выполнены")
        self.conn = psycopg2.connect(**self.conn_params)

    def get_password(self, user_login):
        cursor = self.conn.cursor()
        cursor.callproc('get_password', [user_login])
        result = cursor.fetchone()
        #result = cursor.execute("select * from get_password({param1})".format(param1=user_login))
        cursor.close()
        return result

    def add_user(self, user_name, user_city, user_login, user_password):
        cursor = self.conn.cursor()
        cursor.callproc('add_user', [user_name, user_city, user_login, user_password])
        self.conn.commit()
        cursor.close()

    def get_user_id(self, user_login):
        cursor = self.conn.cursor()
        cursor.callproc('get_user_id', [user_login])
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_books(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_books', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_book(self, book_name):
        cursor = self.conn.cursor()
        cursor.callproc('find_book', [book_name])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_completed_orders(self, user_id):
        cursor = self.conn.cursor()
        cursor.callproc('get_completed_order', [user_id])
        result = cursor.fetchall()
        cursor.close()
        return result

    def place_order(self, user_id, book_id):
        cursor = self.conn.cursor()
        cursor.callproc('add_buy_book', [user_id, book_id])
        result = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        return result

    def delete_order(self, order_id):
        cursor = self.conn.cursor()
        cursor.callproc('delete_buy_book', [order_id])
        self.conn.commit()
        cursor.close()

    def get_table_book(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_table_book', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_table_author(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_table_author', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_table_buy_book(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_table_buy_book', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_table_client(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_table_client', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_table_city(self):
        cursor = self.conn.cursor()
        cursor.callproc('get_table_city', [])
        result = cursor.fetchall()
        cursor.close()
        return result

    def trancate_buy_book(self):
        cursor = self.conn.cursor()
        cursor.callproc('trancate_buy_book', [])
        self.conn.commit()
        cursor.close()

    def trancate_all_table(self):
        cursor = self.conn.cursor()
        cursor.callproc('trancate_all_table', [])
        self.conn.commit()
        cursor.close()

    def delete_user(self, user_id, column):
        cursor = self.conn.cursor()
        if column == 3:
            user_id = self.get_user_id(user_id)
        cursor.callproc('delete_user', [user_id])
        self.conn.commit()

        cursor.callproc('delete_orders', [user_id])
        self.conn.commit()
        cursor.close()

    def add_book(self, name_author, name_book, price, amount):
        cursor = self.conn.cursor()
        cursor.callproc('get_author_id', [name_author])
        result = cursor.fetchone()
        print(name_author)
        if result[0] is None:
            cursor.callproc('add_new_author', [name_author])
            print(0)
            self.conn.commit()
        cursor.callproc('add_new_book', [name_author, name_book, price, amount])
        self.conn.commit()
        cursor.close()

    def drop_database(self, dbname):
        cursor = self.conn.cursor()
        cursor.callproc('f_drop_dbb', [dbname])
        self.conn.commit()
        cursor.close()



