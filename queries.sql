CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    publish_year INTEGER
);

INSERT INTO books(title, publish_year)
VALUES
('Война и мир', 1869),
('Преступление и наказание', 1866);

SELECT * FROM books;
