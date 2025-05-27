import json
import os

# File to store the library
LIBRARY_FILE = "library.txt"

# Library data structure (list of book dictionaries)
library = []

# Load library from file
def load_library():
    global library
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []

# Save library to file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: ").strip())
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()

    keyword = input("Enter the search term: ").strip().lower()
    matches = []

    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("📚 Matching Books:")
        display_books(matches)
    else:
        print("❌ No matching books found.")

# Display all books
def display_books(books=None):
    if books is None:
        books = library

    if not books:
        print("📭 Your library is empty.")
        return

    for i, book in enumerate(books, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_stats():
    total = len(library)
    if total == 0:
        print("📊 No books in the library.")
        return

    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total) * 100
    print(f"📚 Total books: {total}")
    print(f"📖 Percentage read: {percentage:.1f}%")

# Menu system
def menu():
    load_library()
    while True:
        print("\n📘 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("📁 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
