from rest_framework import serializers
from datetime import date
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model instances.

    - Purpose:
      Convert Book objects <-> JSON (and validate incoming data).

    - Requirements covered:
      1) Serialize ALL fields of the Book model.
      2) Custom validation: publication_year must not be in the future.
    """
    class Meta:
        model = Book
        field = "__all__"

        def validate_publication_year(self, value: int) -> int:
            """
            Field-level validation for 'publication_year'.

            Ensures the book's publication year is not greater than the current year.
            """
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError(f"Publication Year cannot be in the Future. (Max_Allowed: {current_year}.)")
            return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model instances.

    Includes:
    - 'name' field from Author.
    - Nested books list via BookSerializer, based on the Author->Book relationship.

    Relationship explanation:
    - In Book model, `author = ForeignKey(Author, related_name="books", ...)`
    - That related_name="books" creates a reverse relation:
        author.books.all()
    - We expose that relation in this serializer as a nested list using BookSerializer.

    Note:
    - `read_only=True` means books are returned when reading an Author,
      but you won't create/update Books through AuthorSerializer in this version.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        field = ["id", "name", "books"]