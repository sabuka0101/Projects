from datetime import datetime


class Book:
    """Base class for every book: title, author and publication year."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def title(self):
        """Returns the book's title."""
        return self.__title

    @title.setter
    def title(self, value):
        """Sets the title. It can't be empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title can't be empty")
        self.__title = value.strip()

    @property
    def author(self):
        """Returns the book's author."""
        return self.__author

    @author.setter
    def author(self, value):
        """Sets the author. It can't be empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author can't be empty")
        self.__author = value.strip()

    @property
    def year(self):
        """Returns the publication year."""
        return self.__year

    @year.setter
    def year(self, value):
        """Sets the year. It must be a whole number between 0 and the current year."""
        if not isinstance(value, int):
            raise ValueError("Year must be a number")
        if not 0 <= value <= datetime.now().year:
            raise ValueError(f"Year must be between 0 and {datetime.now().year}")
        self.__year = value

    def to_dict(self):
        """Returns the shared book data as a dictionary, for saving to JSON."""
        return {"title": self.title, "author": self.author, "year": self.year}

    def __str__(self):
        """Returns a readable description of the book."""
        return f"{self.title} — {self.author} ({self.year})"


class EBook(Book):
    """An electronic book. Adds a file size in megabytes."""

    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    @property
    def file_size_mb(self):
        """Returns the file size in MB."""
        return self.__file_size_mb

    @file_size_mb.setter
    def file_size_mb(self, value):
        """Sets the file size. It must be a positive number."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("File size must be a positive number")
        self.__file_size_mb = value

    def to_dict(self):
        """Adds the book type and file size to the parent's dictionary."""
        data = super().to_dict()
        data["type"] = "ebook"
        data["file_size_mb"] = self.file_size_mb
        return data

    def __str__(self):
        """Overrides the parent's __str__ (polymorphism)."""
        return f"[E-Book] {self.title} — {self.author} ({self.year}), {self.file_size_mb} MB"


class PrintedBook(Book):
    """A printed book. Adds the number of pages."""

    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    @property
    def pages(self):
        """Returns the number of pages."""
        return self.__pages

    @pages.setter
    def pages(self, value):
        """Sets the number of pages. It must be a positive whole number."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive whole number")
        self.__pages = value

    def to_dict(self):
        """Adds the book type and page count to the parent's dictionary."""
        data = super().to_dict()
        data["type"] = "printed"
        data["pages"] = self.pages
        return data

    def __str__(self):
        """Overrides the parent's __str__ (polymorphism)."""
        return (
            f"[Printed] {self.title} — {self.author} ({self.year}), {self.pages} pages"
        )
