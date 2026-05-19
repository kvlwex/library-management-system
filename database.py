import psycopg2


def connect_db():
    try:
        connection = psycopg2.connect(
            database="library_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

        return connection

    except Exception as error:
        print("Ошибка:", error)
        return None


def get_books():
    connection = connect_db()

    cursor = connection.cursor()

    query = "SELECT * FROM books"

    cursor.execute(query)

    books = cursor.fetchall()

    connection.close()

    return books
