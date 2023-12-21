CREATE OR REPLACE FUNCTION add_new_book(author_b VARCHAR,
										name_book VARCHAR,
										price_book DECIMAL,
										amount_book INT)
RETURNS void
AS $$
BEGIN
INSERT INTO book(title, author_id, price, amount)
VALUES
(name_book,
(SELECT author.author_id FROM author WHERE author.name_author = author_b),
price_book,
amount_book);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_new_author(author_b VARCHAR)
RETURNS void
AS $$
BEGIN
INSERT INTO author(name_author)
VALUES (author_b);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_author_id(author_name varchar)
RETURNS INTEGER
AS $$
BEGIN
RETURN (SELECT author_id FROM author WHERE name_author = author_name);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_table_book()
RETURNS TABLE(book_id int, title varchar, author_id int, price decimal, amount int)
AS $$
BEGIN
RETURN QUERY
SELECT * FROM book;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_table_author()
RETURNS TABLE(author_id int, name_author varchar)
AS $$
BEGIN
RETURN QUERY
SELECT * FROM author;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_table_buy_book()
RETURNS TABLE(buy_book_id int, client_id int, book_id int)
AS $$
BEGIN
RETURN QUERY
SELECT * FROM buy_book;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_table_client()
RETURNS TABLE(client_id int, name_client varchar, city_id int, email varchar, client_password varchar)
AS $$
BEGIN
RETURN QUERY
SELECT * FROM client;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_table_city()
RETURNS TABLE(city_id int, name_city varchar, days_delivery int)
AS $$
BEGIN
RETURN QUERY
SELECT * FROM city;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_buy_book(id_buy_book int)
RETURNS void
AS $$
BEGIN
DELETE FROM buy_book WHERE  buy_book_id = id_buy_book;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION trancate_all_table()
RETURNS void
AS $$
BEGIN
TRUNCATE TABLE author CASCADE;
TRUNCATE TABLE city CASCADE;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION drop_all_table()
RETURNS void
AS $$
BEGIN
DROP TABLE book CASCADE;
DROP TABLE city CASCADE;
DROP TABLE author CASCADE;
DROP TABLE client CASCADE;
DROP TABLE buy_book CASCADE;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION delete_user(user_id int)
RETURNS void
AS $$
BEGIN
DELETE FROM client
WHERE client_id = user_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_user(user_email varchar)
RETURNS void
AS $$
BEGIN
DELETE FROM client
WHERE email = user_email;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_book(name_book varchar)
RETURNS void
AS $$
BEGIN
DELETE FROM book
WHERE title = name_book;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_city(city_name varchar)
RETURNS void
AS $$
BEGIN
DELETE FROM city
WHERE name_city = city_name;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_author(author_name varchar)
RETURNS void
AS $$
BEGIN
DELETE FROM author
WHERE name_author = author_name;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION trancate_buy_book()
RETURNS void
AS $$
BEGIN
TRUNCATE TABLE buy_book;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION update_book_amount()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    UPDATE book
    SET amount = amount - 1
    WHERE book_id = NEW.book_id;
  ELSIF TG_OP = 'DELETE' THEN
    UPDATE book
    SET amount = amount + 1
    WHERE book_id = OLD.book_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER update_book_amount_trigger
AFTER INSERT OR DELETE ON buy_book
FOR EACH ROW
EXECUTE FUNCTION update_book_amount();


CREATE OR REPLACE FUNCTION delete_orders(user_id int)
RETURNS void
AS $$
BEGIN
DELETE FROM buy_book WHERE  client_id = user_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fill_all_table()
RETURNS void
AS $$
BEGIN
INSERT INTO author(name_author)
VALUES ('Булгаков М.А.'),
('Достоевский Ф.М.'),
('Есенин С.А.'),
('Пастернак Б.Л.'),
('Лермонтов М.Ю.');

INSERT INTO book (title, author_id, price, amount)
VALUES ('Мастер и Маргарита', (select author_id from author where name_author = 'Булгаков М.А.'), 670.99, 3),
('Белая гвардия', (select author_id from author where name_author = 'Булгаков М.А.'), 540.50, 5),
('Идиот', (select author_id from author where name_author = 'Достоевский Ф.М.'), 460.00, 10),
('Братья Карамазовы', (select author_id from author where name_author = 'Достоевский Ф.М.'), 799.01, 2),
('Игрок', (select author_id from author where name_author = 'Достоевский Ф.М.'), 480.50, 10),
('Стихотворения и поэмы', (select author_id from author where name_author = 'Есенин С.А.'), 650.00, 15),
('Черный человек', (select author_id from author where name_author = 'Есенин С.А.'), 570.20, 6),
('Лирика', (select author_id from author where name_author = 'Пастернак Б.Л.'), 518.99, 2);

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

INSERT INTO client(name_client, city_id, email, client_password)
VALUES ('Баранов Павел', (select city_id from city where name_city = 'Владивосток'), 'baranov@test', '123'),
('Абрамова Катя', (select city_id from city where name_city = 'Москва'), 'abramova@test', '456'),
('Семенонов Иван', (select city_id from city where name_city = 'Санкт-Петербург'), 'semenov@test', '789'),
('Яковлева Галина', (select city_id from city where name_city = 'Москва'), 'yakovleva@test', 'abc');

END;
$$ LANGUAGE plpgsql;