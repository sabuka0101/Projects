# Book Manager

A console application for managing a list of books, written in Python using
object-oriented programming. Books are saved to a JSON file, so they are still
there after the program closes.

## Features

- Add e-books and printed books
- View all books
- Search books by title (case-insensitive, partial match)
- Delete a book by its title
- Clear the whole library
- Input validation with clear error messages
- Books are saved to and loaded from `books.json` automatically

## Project structure

| File | Purpose |
|---|---|
| `main.py` | starts the program and runs the menu |
| `menu.py` | the menu and asking the user for book details |
| `manager.py` | `BookManager`: adds, shows, searches, deletes, saves and loads books |
| `models.py` | `Book`, `EBook` and `PrintedBook` classes |

## OOP principles used

- **Encapsulation:** book data is stored in private attributes and accessed through
  properties. The setters validate every value (no empty titles, years between 0
  and the current year, positive page counts and file sizes).
- **Inheritance:** `EBook` and `PrintedBook` inherit from `Book` and reuse its
  validation with `super()`.
- **Polymorphism:** each book type has its own `__str__` and `to_dict`, so the
  same code prints and saves every type in its own way.

## How to run

No extra libraries are needed, only Python 3.

Run it from the main folder of this repository (the one that contains
`BookManager`), not from inside `BookManager`:

```bash
python BookManager/main.py
```

## Example

```
1. Add book
2. Show books
3. Search by title
4. Delete book
5. Clear library
6. Exit
Choose an option: 1
1. E-book
2. Printed book
Choose book type: 2
Title: 1984
Author: George Orwell
Year: 1949
Pages: 328
Added new book: [Printed] 1984 — George Orwell (1949), 328 pages

Choose an option: 1
1. E-book
2. Printed book
Choose book type: 1
Title: Harry Potter
Author: J.K. Rowling
Year: 1997
File size (MB): 2.5
Added new book: [E-Book] Harry Potter — J.K. Rowling (1997), 2.5 MB

Choose an option: 2
1. [Printed] 1984 — George Orwell (1949), 328 pages
2. [E-Book] Harry Potter — J.K. Rowling (1997), 2.5 MB

Choose an option: 3
Search title: harry
[E-Book] Harry Potter — J.K. Rowling (1997), 2.5 MB

Choose an option: 1
1. E-book
2. Printed book
Choose book type: 2
Title: Test
Author: Someone
Year: 3000
Pages: 100
Error: Year must be between 0 and 2026

Choose an option: 4
Title of the book to delete: 1984
Deleted: [Printed] 1984 — George Orwell (1949), 328 pages

Choose an option: 6
Goodbye!
```
