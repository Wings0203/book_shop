CREATE EXTENSION IF NOT EXISTS dblink;

CREATE OR REPLACE FUNCTION f_create_db(dbname text)
  RETURNS void AS
$func$
BEGIN
IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
   RAISE NOTICE 'Database already exists';
ELSE
   PERFORM dblink_exec('dbname=' || current_database()
                     , 'CREATE DATABASE ' || quote_ident(dbname));
END IF;

END
$func$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION f_drop_db(dbname text)
RETURNS VOID
AS $$
BEGIN
IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
   RAISE NOTICE 'Database not exists';
ELSE
   PERFORM dblink_exec('dbname=' || current_database(), 'DROP DATABASE ' || quote_ident(dbname));
END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION create_all_table()
RETURNS INTEGER
AS $$
BEGIN
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'author') THEN
CREATE TABLE author (
author_id SERIAL PRIMARY KEY,
name_author VARCHAR(50)
);
INSERT INTO author(name_author)
VALUES ('Булгаков М.А.'),
('Достоевский Ф.М.'),
('Есенин С.А.'),
('Пастернак Б.Л.'),
('Лермонтов М.Ю.');
END IF;

IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'book') THEN
CREATE TABLE book(
book_id SERIAL PRIMARY KEY,
title VARCHAR(50),
author_id INT NOT NULL,
price DECIMAL(8,2) CONSTRAINT positive_price CHECK (price > 0),
amount INT CONSTRAINT positive_amount CHECK (amount >= 0),
FOREIGN KEY (author_id) REFERENCES author (author_id) ON DELETE CASCADE
);
INSERT INTO book (title, author_id, price, amount)
VALUES ('Мастер и Маргарита', 1, 670.99, 3),
('Белая гвардия', 1, 540.50, 5),
('Идиот', 2, 460.00, 10),
('Братья Карамазовы', 2, 799.01, 2),
('Игрок', 2, 480.50, 10),
('Стихотворения и поэмы', 3, 650.00, 15),
('Черный человек', 3, 570.20, 6),
('Лирика', 4, 518.99, 2);
END IF;

IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'city') THEN
CREATE TABLE city(
city_id SERIAL primary key,
name_city varchar(30),
days_delivery int CONSTRAINT positive_days_delivery CHECK (days_delivery > 0)
);
INSERT INTO city(name_city, days_delivery)
 VALUES ('Москва', 5),
('Санкт-Петербург', 3),
('Владивосток', 12),
('Нижний Новгород', 1),
('Казань', 3),
('Омск', 8),
('Екатеринбург', 7),
('Самара', 5),
('Новосибирск', 10),
('Красноярск', 6),
('Челябинск', 4);
END IF;

IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'client') THEN
CREATE TABLE client(
client_id SERIAL primary key,
name_client varchar(50),
city_id INT NOT NULL,
email varchar(30),
client_password varchar(20),
FOREIGN KEY (city_id) REFERENCES city (city_id) ON DELETE CASCADE
);
INSERT INTO client(name_client, city_id, email, client_password)
VALUES ('Баранов Павел', 3, 'baranov@test', '123'),
('Абрамова Катя', 1, 'abramova@test', '456'),
('Семенонов Иван', 2, 'semenov@test', '789'),
('Яковлева Галина', 1, 'yakovleva@test', 'abc');
END IF;

IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'buy_book') THEN
CREATE TABLE buy_book(
buy_book_id SERIAL PRIMARY KEY,
client_id INT NOT NULL,
book_id INT NOT NULL,
FOREIGN KEY (client_id) REFERENCES client (client_id) ON DELETE CASCADE,
FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE
);
INSERT INTO buy_book(client_id, book_id)
VALUES
(2, 1),
(2, 2),
(3, 3),
(4, 1);
END IF;
RETURN 0;
END;
$$ LANGUAGE plpgsql;
