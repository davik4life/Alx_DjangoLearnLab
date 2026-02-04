from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model.

    Purpose:
    - Stores information about an author.
    - An Author can have many books (one-to-many relationship).

    Fields:
    - name: stores the author's name as a string.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model.

    Purpose:
    - Stores information about a book.
    - Each Book belongs to exactly one Author (many-to-one).

    Fields:
    - title: the book title.
    - publication_year: the year the book was published.
    - author: foreign key linking to Author.

    Relationship:
    - This foreign key creates a one-to-many relationship:
        One Author -> Many Books
    - `related_name="books"` enables reverse lookup:
        author.books.all()
    """
    title = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = "books")

    def __str__(self) -> str:
        return f"{self.title}, ({self.publication_year})"

