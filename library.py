class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.members = []
            cls._instance.librarians = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def add_librarian(self, librarian):
        self.librarians.append(librarian)

    def search_books(self, title=None, author=None, category=None):
        results = []
        for book in self.books:
            if (title and title in book.title) or (author and author in book.author) or (category and category in book.category.name):
                results.append(book)
        return results

    def search_members(self, name=None, email=None):
        results = []
        for member in self.members:
            if (name and name in member.name) or (email and email in member.email):
                results.append(member)
        return results