from datetime import datetime, timedelta

class Book:
    """Class to represent a Book in the library."""
    def __init__(self, title, author, ISBN, genre, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.quantity = quantity

class Borrower:
    """Class to represent a Borrower in the library system."""
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id

class Library:
    """Class to manage the library system, including books and borrowers."""
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}

    def add_book(self, title, author, ISBN, genre, quantity):
        """Add a new book to the library."""
        if ISBN in self.books:
            print("Book with this ISBN already exists.")
        else:
            self.books[ISBN] = Book(title, author, ISBN, genre, quantity)
            print(f"Book '{title}' added to the library.")

    def update_book(self, ISBN, title=None, author=None, genre=None, quantity=None):
        """Update the details of an existing book."""
        if ISBN not in self.books:
            print("Book with this ISBN does not exist.")
        else:
            book = self.books[ISBN]
            if title:
                book.title = title
            if author:
                book.author = author
            if genre:
                book.genre = genre
            if quantity is not None:  # Quantity can be 0, so we check against None
                book.quantity = quantity
            print(f"Book with ISBN {ISBN} has been updated.")

    def remove_book(self, ISBN):
        """Remove a book from the library."""
        if ISBN in self.books:
            del self.books[ISBN]
            print(f"Book with ISBN {ISBN} has been removed from the library.")
        else:
            print("Book with this ISBN does not exist.")

    def add_borrower(self, name, contact_details, membership_id):
        """Add a new borrower to the library system."""
        if membership_id in self.borrowers:
            print("Borrower with this membership ID already exists.")
        else:
            self.borrowers[membership_id] = Borrower(name, contact_details, membership_id)
            print(f"Borrower '{name}' added to the system.")

    def update_borrower(self, membership_id, name=None, contact_details=None):
        """Update the details of an existing borrower."""
        if membership_id not in self.borrowers:
            print("Borrower with this membership ID does not exist.")
        else:
            borrower = self.borrowers[membership_id]
            if name:
                borrower.name = name
            if contact_details:
                borrower.contact_details = contact_details
            print(f"Borrower with membership ID {membership_id} has been updated.")

    def remove_borrower(self, membership_id):
        """Remove a borrower from the system."""
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(f"Borrower with membership ID {membership_id} has been removed from the system.")
        else:
            print("Borrower with this membership ID does not exist.")

    def borrow_book(self, membership_id, ISBN, borrow_days=14):
        """Allow a borrower to borrow a book."""
        if membership_id not in self.borrowers:
            print("Borrower with this membership ID does not exist.")
            return

        if ISBN not in self.books:
            print("Book with this ISBN does not exist.")
            return

        book = self.books[ISBN]
        if book.quantity <= 0:
            print(f"No copies of '{book.title}' are available for borrowing.")
            return
        # Record the borrowing transaction
        due_date = datetime.now() + timedelta(days=borrow_days)
        self.borrowed_books[(membership_id, ISBN)] = {
            'due_date': due_date,
            'returned': False
        }
        book.quantity -= 1
        print(f"Borrower '{self.borrowers[membership_id].name}' borrowed '{book.title}' due on {due_date.strftime('%Y-%m-%d')}.")

    def return_book(self, membership_id, ISBN):
        """Allow a borrower to return a book."""
        if (membership_id, ISBN) not in self.borrowed_books:
            print("This borrowing transaction does not exist.")
            return

        if self.borrowed_books[(membership_id, ISBN)]['returned']:
            print("This book has already been returned.")
            return

        # Update the borrowing record and library inventory
        self.borrowed_books[(membership_id, ISBN)]['returned'] = True
        self.books[ISBN].quantity += 1
        print(f"Borrower '{self.borrowers[membership_id].name}' returned '{self.books[ISBN].title}'.")

    def check_overdue_books(self):
        """Check for any overdue books."""
        today = datetime.now()
        for (membership_id, ISBN), details in self.borrowed_books.items():
            if not details['returned'] and details['due_date'] < today:
                print(f"Book '{self.books[ISBN].title}' borrowed by '{self.borrowers[membership_id].name}' is overdue.")

    def search_books(self, query, search_by='title'):
        """Search for books by title, author, or genre."""
        results = []
        for book in self.books.values():
            if search_by == 'title' and query.lower() in book.title.lower():
                results.append(book)
            elif search_by == 'author' and query.lower() in book.author.lower():
                results.append(book)
            elif search_by == 'genre' and query.lower() in book.genre.lower():
                results.append(book)
        return results

    def display_search_results(self, query, search_by='title'):
        """Display search results with availability status."""
        results = self.search_books(query, search_by)
        if not results:
            print("No books found matching the query.")
        else:
            for book in results:
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available Copies: {book.quantity}")

# Sample usage
library = Library()

# Adding books
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890", "Fiction", 5)
library.add_book("1984", "George Orwell", "1234567891", "Dystopian", 10)
library.add_book("To Kill a Mockingbird", "Harper Lee", "1234567892", "Classic", 7)

# Adding borrowers
library.add_borrower("John Doe", "john.doe@example.com", "MEM001")
library.add_borrower("Jane Smith", "jane.smith@example.com", "MEM002")

# Borrowing books
library.borrow_book("MEM001", "1234567890")
library.borrow_book("MEM002", "1234567891")

# Returning a book
library.return_book("MEM001", "1234567890")

# Checking overdue books
library.check_overdue_books()

# Searching for books
print("Search by Title '1984':")
library.display_search_results("1984", search_by='title')

print("\nSearch by Author 'George Orwell':")
library.display_search_results("George Orwell", search_by='author')

print("\nSearch by Genre 'Fiction':")
library.display_search_results("Fiction", search_by='genre')

# Print the current state of the library and borrower databases, and borrowed books
print("\nLibrary Database:")
for ISBN, book in library.books.items():
    print(f"{ISBN}: {book.title}, {book.author}, {book.genre}, {book.quantity} copies available")

print("\nBorrower Database:")
for membership_id, borrower in library.borrowers.items():
    print(f"{membership_id}: {borrower.name}, {borrower.contact_details}")

print("\nBorrowed Books:")
for (membership_id, ISBN), details in library.borrowed_books.items():
    status = "returned" if details['returned'] else f"due on {details['due_date'].strftime('%Y-%m-%d')}"
    print(f"{membership_id} borrowed {ISBN} ({library.books[ISBN].title}) - {status}")
