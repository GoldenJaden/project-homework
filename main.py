from library import Library
from book import BookFactory, Category
from member import Member
from decorator import Borrowable
from librarian import Librarian

library = Library()

fiction = Category("Fiction")
non_fiction = Category("Non-Fiction")

book1 = BookFactory.create_book("regular", "1984", "George Orwell", "1234567890", 1949, fiction)
book2 = BookFactory.create_book("ebook", "Brave New World", "Aldous Huxley", "0987654321", 1932, fiction)

library.add_book(book1)
library.add_book(book2)

member1 = Member(1, "Alice", "alice@example.com")
member2 = Member(2, "Bob", "bob@example.com")

library.add_member(member1)
library.add_member(member2)

librarian = Librarian(1, "Charles")

library.add_librarian(librarian)

book1.add_observer(member1)
book2.add_observer(member2)

book1.notify_observers()
book2.notify_observers()

borrowable_book = Borrowable(book1)
borrowable_book.borrow()

member1.borrow_book(book1)
member2.borrow_book(book2)

member1.reserve_book(book2)

print(member1.notifications)
print(member2.notifications)

member1.display_info()
member2.display_info()

search_results = library.search_books(title="1984")
print(f"Search Results: {[book.title for book in search_results]}")