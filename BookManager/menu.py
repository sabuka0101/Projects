from models import EBook, PrintedBook


def show_menu():
    """Prints the main menu."""
    print("\n1. Add book")
    print("2. Show books")
    print("3. Search by title")
    print("4. Delete book")
    print("5. Clear library")
    print("6. Exit")


def add_book_from_input(manager):
    """Asks the user for book details, creates the right book type and adds it."""
    print("1. E-book")
    print("2. Printed book")
    book_type = input("Choose book type: ")
    if book_type not in ("1", "2"):
        print("Error: Please choose 1 or 2")
        return

    title = input("Title: ")
    author = input("Author: ")

    try:
        year = int(input("Year: "))
    except ValueError:
        print("Error: Year must be a whole number")
        return

    try:
        if book_type == "1":
            size = float(input("File size (MB): "))
            book = EBook(title, author, year, size)
        else:
            pages = int(input("Pages: "))
            book = PrintedBook(title, author, year, pages)
        manager.add_book(book)
    except ValueError as error:
        print(f"Error: {error}")
