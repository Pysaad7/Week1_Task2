import json
import os

# File to store data
DATA_FILE = "library.json"

# Load books from JSON File
def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save books to JSON file
def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Function to Add Books
def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))

    for book in books:
        if book["Book ID"] == book_id:
            print(" Book ID already exists!")
            return

    books.append({
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Quantity": quantity,
        "Max Quantity": quantity  
    })
    save_books(books)
    print(" Book added successfully!")

# function to View all books
def view_books(books):
    if not books:
        print(" No books available!")
    else:
        print("\n--- Available Books ---")
        for book in books:
            print(f'ID: {book["Book ID"]}, Title: {book["Title"]}, Author: {book["Author"]}, Quantity: {book["Quantity"]}/{book["Max Quantity"]}')
        print("-----------------------")

# Function to Borrow book
def borrow_book(books):
    book_id = input("Enter Book ID to borrow: ")
    for book in books:
        if book["Book ID"] == book_id:
            if book["Quantity"] > 0:
                book["Quantity"] -= 1
                save_books(books)
                print(f' You borrowed "{book["Title"]}"')
            else:
                print(" Book not available (out of stock).")
            return
    print(" Book ID not found!")

# Function to Return book
def return_book(books):
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["Book ID"] == book_id:
            if book["Quantity"] < book["Max Quantity"]:
                book["Quantity"] += 1
                save_books(books)
                print(f' You returned "{book["Title"]}"')
            else:
                print(" All copies already in library. You can't return more!")
            return
    print(" Book ID not found!")

            # Main menu
def main():
    books = load_books()
    
    while True:
        print("\n===== Mini Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main()
