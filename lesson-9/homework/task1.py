class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f'"{self.title}" by {self.author}'

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.max_books = 3

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= self.max_books:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.max_books} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __str__(self):
        borrowed = ', '.join([book.title for book in self.borrowed_books]) or 'No books borrowed'
        return f"Member: {self.name}, Borrowed Books: {borrowed}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def add_member(self, member: Member):
        self.members.append(member)
        print(f"Added member: {member.name}")

    def borrow_book(self, member_name: str, book_title: str):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        member.borrow_book(book)
        print(f"{member_name} borrowed {book_title}.")

    def return_book(self, member_name: str, book_title: str):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if book and member:
            member.return_book(book)
            print(f"{member_name} returned {book_title}.")

    def list_books(self):
        for book in self.books:
            status = 'Borrowed' if book.is_borrowed else 'Available'
            print(f"{book} - {status}")

# Test scenarios
if __name__ == '__main__':
    library = Library()
    # Adding books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    
    # Adding members
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    # Borrowing books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Bob", "The Great Gatsby")
        library.borrow_book("Alice", "1984")  # Should raise BookAlreadyBorrowedException
    except Exception as e:
        print(e)

    # Listing books
    library.list_books()

    # Returning a book
    library.return_book("Alice", "1984")
    library.list_books()

    # Exception handling
    try:
        library.borrow_book("Alice", "Nonexistent Book")  # Should raise BookNotFoundException
    except Exception as e:
        print(e)

    # Test member limit
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "The Great Gatsby")
    except Exception as e:
        print(e)
