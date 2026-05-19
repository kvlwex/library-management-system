from database import connect_db


def test_connection():
    connection = connect_db()

    assert connection is not None

    print("Тест подключения успешно пройден")


test_connection()
