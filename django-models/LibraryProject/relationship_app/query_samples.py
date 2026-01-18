"""
Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of 
the following of relationship:

Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
"""
from django.template import Library


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)