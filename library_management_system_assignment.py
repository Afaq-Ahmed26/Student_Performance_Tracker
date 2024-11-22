# Library Management System

# Lists to store books and users
books = []
users = []

# Function to add a new book to the library
def add_book(book_id, title, author, genre, status="Available"):
    # Create a book dictionary with details and add it to the books list
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "genre": genre,
        "status": status
    }
    books.append(book)

# Function to add a new user to the library system
def add_user(user_id, name):
    # Create a user dictionary with details and add it to the users list
    user = {
        "id": user_id,
        "name": name,
        "borrowed_books": []
    }
    users.append(user)

# Function to show all books in the library
def view_all_books():
    print("\nAll Books:")
    for book in books:
        # Display book info like ID, title, author, and availability
        status = book["status"]
        print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({status})')
    print("-" * 40)

# Function to search for books by title, author, or genre
def search_books(criteria, search_term):
    print(f'\nSearch Results for "{search_term}" by {criteria.capitalize()}:')
    # Find books that match the search term
    found_books = [book for book in books if book[criteria].lower() == search_term.lower()]
    if found_books:
        for book in found_books:
            status = book["status"]
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({status})')
    else:
        print("No books found.")
    print("-" * 40)

# Function to let a user borrow a book
def borrow_book(user_id, book_id):
    # Find the user and the book by their IDs
    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)
    if user and book:
        # Check if the book is available
        if book["status"] == "Available":
            book["status"] = "Checked Out"  # Change the book's status
            user["borrowed_books"].append(book_id)  # Add book to user's borrowed list
            print(f'You have borrowed "{book["title"]}".')
        else:
            print(f'Sorry, the book "{book["title"]}" is currently checked out.')
    else:
        print("Invalid user ID or book ID.")
    print("-" * 40)

# Function to let a user return a book
def return_book(user_id, book_id):
    # Find the user and the book by their IDs
    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)
    if user and book:
        # Check if the user actually borrowed the book
        if book_id in user["borrowed_books"]:
            book["status"] = "Available"  # Change the book's status back
            user["borrowed_books"].remove(book_id)  # Remove book from user's list
            print(f'You have returned "{book["title"]}".')
        else:
            print("This book was not borrowed by you.")
    else:
        print("Invalid user ID or book ID.")
    print("-" * 40)

# Function to show all users in the system
def view_all_users():
    print("\nAll Users:")
    for user in users:
        # Display user info like ID and name
        print(f'User ID: {user["id"]}, Name: {user["name"]}')
        if user["borrowed_books"]:
            print("  Borrowed Books:")
            # Show the books each user has borrowed
            for book_id in user["borrowed_books"]:
                book = next((b for b in books if b["id"] == book_id), None)
                if book:
                    print(f'    - "{book["title"]}" by {book["author"]}')
        else:
            print("  No borrowed books.")
    print("-" * 40)

# Main menu function for interacting with the system
def main_menu():
    # This loop keeps showing the menu until the user exits
    while True:
        print("\nWelcome to the Community Library System!")
        print("-" * 40)
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-6): ")
        
        # Perform the action based on user's choice
        if choice == "1":
            view_all_books()
        elif choice == "2":
            criteria = input("Search by (title, author, genre): ").lower()
            search_term = input("Enter search term: ")
            search_books(criteria, search_term)
        elif choice == "3":
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to borrow: "))
            borrow_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to return: "))
            return_book(user_id, book_id)
        elif choice == "5":
            view_all_users()
        elif choice == "6":
            print("Thank you for using the Community Library System!")
            break  # Exit the loop to end the program
        else:
            print("Invalid choice. Please try again.")
        print("-" * 40)

# Adding some books and users to get started
add_book(1, "Islamiat for Class 10", "Punjab Textbook Board", "Education")
add_book(2, "Pakistan Studies Class 10", "Punjab Textbook Board", "Education")
add_book(3, "Mathematics for Class 9", "Punjab Textbook Board", "Education")
add_user(1, "Afaq")
add_user(2, "Ahmed")

# Start the library system
main_menu()
