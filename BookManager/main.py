"""Book management console application.

Lets the user add, view, search and delete books.
Books are saved to a JSON file, so they stay after the program closes.
"""

from manager import BookManager
from menu import add_book_from_input, show_menu

if __name__ == "__main__":
    manager = BookManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book_from_input(manager)

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = input("Search title: ")
            if title.strip():
                manager.search_by_title(title.strip())
            else:
                print("Error: Search text can't be empty")

        elif choice == "4":
            title = input("Title of the book to delete: ")
            manager.delete_book(title.strip())

        elif choice == "5":
            confirm = input("Delete ALL books? (y/n): ")
            if confirm.lower() == "y":
                manager.clear_library()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Please choose 1–6.")
