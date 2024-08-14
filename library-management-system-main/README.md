
# Library Management System

This project is a simplified library management system implemented using Python's Object-Oriented Programming (OOP) concepts. The system allows you to manage books and borrowers, handle book borrowing and returning, and search for books.

## Features

- **Book Management**
  - Add new books to the library database with details like title, author, ISBN, genre, and quantity.
  - Update existing book information (e.g., title, author, genre, quantity).
  - Remove books from the library database when they are no longer available.

- **Borrower Management**
  - Add new borrowers to the library system, including information like name, contact details, and membership ID.
  - Update borrower information when required (e.g., contact details).
  - Remove borrowers from the system if necessary.

- **Book Borrowing and Returning**
  - Allow borrowers to borrow books by linking the borrower's membership ID to the book details.
  - Record the due date for each borrowed book and handle overdue books.
  - Implement a mechanism for borrowers to return books, updating the database accordingly.

- **Book Search and Availability**
  - Provide a search feature that enables users to find books by title, author, or genre.
  - Show the availability status (number of copies available) for each book in the search results.



## Installation

1. Clone the repository:
   git clone https://github.com/your-username/library-management-system.git
   
Navigate to the project directory:
cd library-management-system

Run the Python script:
python library_management_system.py


Here is an example of how to use the library management system:

# Initialize the library
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
