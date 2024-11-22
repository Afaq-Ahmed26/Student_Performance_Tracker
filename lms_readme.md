Library Management System
Overview
The Library Management System is a Python-based project that allows a community library to manage its books and users efficiently. It supports features like adding books and users, searching for books, borrowing and returning books, and viewing user details.

Features
Manage Books

Add new books to the library.
View all books with their details.
Search for books by title, author, or genre.
Manage Users

Add new users to the system.
View user details, including borrowed books.
Borrow and Return Books

Allow users to borrow available books.
Return borrowed books to the library.
Class Interaction

Use intuitive commands to manage the library and interact with users.
How to Use
1. Start the Program
Run the program in a Python environment:
Choose an option by entering the corresponding number.

3. Functionalities
View All Books
Displays a list of all books in the library, showing:
Book ID
Title
Author
Status (Available/Checked Out)

Search for a Book

Search by:

Title
Author
Genre
Displays matching results.

Borrow a Book

Input your User ID and the Book ID to borrow.
The book's status will be updated to "Checked Out."

Return a Book

Input your User ID and the Book ID to return.
The book's status will be updated to "Available."

View All Users

Displays user details, including:
Borrowed books (if any).

Dependencies

Python 3.x is required to run this program.

Customization

Add or remove books by modifying the add_book function calls.
Add or remove users by modifying the add_user function calls.
Update functionality by editing respective functions like borrow_book or search_books.

Usage Notes

Ensure all inputs are valid:
Book IDs and User IDs must exist in the system.
Scores must be between 0 and 100.

Future Enhancements

Implement a database for persistent storage.
Add an admin panel for managing users and books.
Include a graphical user interface (GUI).

Acknowledgments
This project was created as part of a learning exercise for building Python-based management systems.
