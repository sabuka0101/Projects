import json

from models import EBook, PrintedBook

FILE_PATH = "BookManager/books.json"


class BookManager:
    """Manages the list of books and saves it to the JSON file."""

    def __init__(self):
        self.__books = []
        self.load_books()

    def add_book(self, book):
        """Adds a book to the list and saves the file."""
        self.__books.append(book)
        self.save_books()
        print(f"Added new book: {book}")

    def show_books(self):
        """Prints every book. Each type prints its own way (polymorphism)."""
        if not self.__books:
            print("No books yet.")
            return
        for number, book in enumerate(self.__books, start=1):
            print(f"{number}. {book}")

    def search_by_title(self, title):
        """Prints every book whose title contains the given text (case-insensitive)."""
        found = False
        for book in self.__books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("No book found with that title.")

    def delete_book(self, title):
        """Deletes the book with exactly this title (case-insensitive) and saves the file."""
        for book in self.__books:
            if book.title.lower() == title.lower():
                self.__books.remove(book)
                self.save_books()
                print(f"Deleted: {book}")
                return
        print("No book found with that title.")

    def clear_library(self):
        """Removes all books and empties the JSON file."""
        self.__books.clear()
        self.save_books()
        print("Library cleared.")

    def save_books(self):
        """Writes all books to the JSON file (creates or overwrites it)."""
        data = [book.to_dict() for book in self.__books]
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_books(self):
        """Loads books from the JSON file, if it exists."""
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError as error:
            print(f"Could not load books: {error}")
            return

        for item in data:
            try:
                if item["type"] == "ebook":
                    book = EBook(
                        item["title"],
                        item["author"],
                        item["year"],
                        item["file_size_mb"],
                    )
                else:
                    book = PrintedBook(
                        item["title"], item["author"], item["year"], item["pages"]
                    )
                self.__books.append(book)
            except (KeyError, ValueError) as error:
                print(f"Skipped a broken book entry: {error}")
