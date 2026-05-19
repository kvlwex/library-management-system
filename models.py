
class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year


class Reader:
    def __init__(self, full_name, phone):
        self.full_name = full_name
        self.phone = phone


class Loan:
    def __init__(self, book_id, reader_id):
        self.book_id = book_id
        self.reader_id = reader_id
