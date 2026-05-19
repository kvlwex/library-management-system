from database import connect_db, get_books

def main():
    print("Система управления библиотекой")

    connection = connect_db()

    if connection:
        print("Подключение успешно")

        books = get_books()

        print("\nСписок книг:")

        for book in books:
            print(book)

        connection.close()

    else:
        print("Ошибка подключения")


if __name__ == "__main__":
    main()
