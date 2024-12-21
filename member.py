class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.notifications = []
        self.borrowed_books = []
        self.reserved_books = []

    def notify(self, message):
        self.notifications.append(message)

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        self.notify(f"You have borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            self.notify(f"You have returned '{book.title}'.")
        else:
            self.notify(f"You do not have '{book.title}' borrowed.")

    def reserve_book(self, book):
        self.reserved_books.append(book)
        self.notify(f"You have reserved '{book.title}'.")

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Borrowed Books: {[book.title for book in self.borrowed_books]}")
        print(f"Reserved Books: {[book.title for book in self.reserved_books]}")
        print(f"Notifications: {self.notifications}")