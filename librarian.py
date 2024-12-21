class Librarian:
    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name

    def add_book(self, library, book):
        library.add_book(book)

    def add_member(self, library, member):
        library.add_member(member)

    def add_librarian(self, library, librarian):
        library.add_librarian(librarian)