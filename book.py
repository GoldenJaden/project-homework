class Category:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author, isbn, publication_year, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.category = category
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify(f"The book '{self.title}' is now available.")

class EBook(Book):
    def __init__(self, title, author, isbn, publication_year, category):
        super().__init__(title, author, isbn, publication_year, category)
        self.format = "ebook"

class BookFactory:
    @staticmethod
    def create_book(book_type, title, author, isbn, publication_year, category):
        if book_type == "regular":
            return Book(title, author, isbn, publication_year, category)
        elif book_type == "ebook":
            return EBook(title, author, isbn, publication_year, category)
        # Add more types as needed