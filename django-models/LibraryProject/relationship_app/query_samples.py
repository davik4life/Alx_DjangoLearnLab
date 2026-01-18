"""
Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of 
the following of relationship:

Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
"""
# from django.template import Library

# # Query all books by a specific author
# def get_books_by_author(author_name):
#     author = Author.objects.get(name=author_name)
#     return Book.objects.filter(author=author)

# # List all books in a library
# def get_books_in_library(library_name):
#     library = Library.objects.get(name=library_name)
#     return library.books.all()

# # Retrieve the librarian for a library
# def get_librarian_for_library(library_name):
#     library = Library.objects.get(name=library_name)
#     return Librarian.objects.get(library=library)


import os
import django

# 1) Point Django to your settings module (adjust if your project name differs)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def seed_data():
    """
    Creates sample data so your queries return something.
    If you already have data, you can skip calling this.
    """
    george, _ = Author.objects.get_or_create(name="George Orwell")
    tolkien, _ = Author.objects.get_or_create(name="J.R.R. Tolkien")

    b1, _ = Book.objects.get_or_create(title="1984", author=george)
    b2, _ = Book.objects.get_or_create(title="Animal Farm", author=george)
    b3, _ = Book.objects.get_or_create(title="The Hobbit", author=tolkien)

    lib, _ = Library.objects.get_or_create(name="Central Library")
    lib.books.add(b1, b2, b3)

    Librarian.objects.get_or_create(name="Alice", library=lib)


def query_books_by_author(author_name: str):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # uses related_name="books"
    print(f"Books by {author.name}:")
    for book in books:
        print("-", book.title)


def query_books_in_library(library_name: str):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name}:")
    for book in books:
        print("-", book.title)


def query_librarian_for_library(library_name: str):
    """Retrieve the librarian for a library."""
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # uses related_name="librarian"
    print(f"Librarian for {library.name}: {librarian.name}")


if __name__ == "__main__":
    seed_data()

    query_books_by_author("George Orwell")
    print()

    query_books_in_library("Central Library")
    print()

    query_librarian_for_library("Central Library")
