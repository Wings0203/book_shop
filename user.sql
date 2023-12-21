
CREATE OR REPLACE FUNCTION get_table_for_user()
RETURNS TABLE(book_id INT, title VARCHAR, name_author VARCHAR, price DECIMAL, amount INT)
AS $$
BEGIN
RETURN QUERY
SELECT b.book_id, b.title, a.name_author, b.price, b.amount
FROM book b
JOIN author a ON b.author_id = a.author_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_password(login VARCHAR)
RETURNS varchar
AS $$
BEGIN
RETURN (SELECT client_password FROM client WHERE email=login);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_user(
	user_name VARCHAR,
	user_city VARCHAR,
	user_login VARCHAR,
	user_password VARCHAR
	)
RETURNS void
AS $$
BEGIN
INSERT INTO client (name_client, city_id, email, client_password)
VALUES
(user_name,
(SELECT city_id FROM city WHERE name_city = user_city),
user_login,
user_password);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_user_id(user_login VARCHAR)
RETURNS INTEGER
AS $$
BEGIN
RETURN
(SELECT client_id
FROM client
WHERE email = user_login);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION find_book(book_name VARCHAR)
RETURNS TABLE(book_id INT, title VARCHAR, name_author VARCHAR, price DECIMAL, amount INT)
AS $$
BEGIN
IF NOT EXISTS (
        SELECT 1
        FROM pg_indexes
        WHERE tablename = 'book' AND indexname = 'book_title_index'
    ) THEN
        CREATE INDEX book_title_index ON book(title);
    END IF;
RETURN QUERY
SELECT b.book_id, b.title, a.name_author, b.price, b.amount
FROM book b
JOIN author a ON b.author_id = a.author_id
WHERE b.title = book_name;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_completed_order(user_id INT)
RETURNS TABLE(buy_book_id INT, 
        title VARCHAR, 
        name_author VARCHAR, 
        name_city VARCHAR, 
        days_delivery INT, 
        price DECIMAL)
AS $$
BEGIN
RETURN QUERY
SELECT buy_book.buy_book_id, b.title, a.name_author, city.name_city, city.days_delivery, b.price
FROM book b
JOIN buy_book ON b.book_id = buy_book.book_id
JOIN author a ON b.author_id = a.author_id
JOIN client ON buy_book.client_id = client.client_id
JOIN city ON city.city_id = client.city_id
WHERE client.client_id = user_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_buy_book(
	user_id INTEGER,
	book_id INTEGER
	)
RETURNS void
AS $$
BEGIN
INSERT INTO buy_book(client_id, book_id)
VALUES
(user_id, book_id);
END;
$$ LANGUAGE plpgsql;


