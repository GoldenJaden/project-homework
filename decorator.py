from book import Book

class BookDecorator(Book):
    def __init__(self, book):
        self._book = book

    def get_title(self):
        return self._book.title

    def get_author(self):
        return self._book.author

class Borrowable(BookDecorator):
    def __init__(self, book):
        super().__init__(book)
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False