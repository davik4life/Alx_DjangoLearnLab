from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.

    Covers:
    - CRUD operations
    - Filtering, searching, ordering
    - Authentication & permissions
    """

    def setUp(self):
        """
        Set up test data and users.
        Runs before every test.
        """

        # Create user for authenticated requests
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create books
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Arrow of God",
            publication_year=1964,
            author=self.author
        )

        # URLs
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"



    def test_list_books(self):
        """
        Ensure anyone can retrieve list of books.
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Ensure a single book can be retrieved by ID.
        """
        url = f"/api/books/{self.book1.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book_requires_authentication(self):
        """
        Unauthenticated users should not be able to create books.
        """
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id,
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_create_book_authenticated(self):
        """
        Authenticated users can create a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id,
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)


    def test_update_book(self):
        """
        Authenticated users can update a book.
        """
        self.client.login(username="testuser", password="testpassword")

        url = f"/api/books/{self.book1.id}/update/"
        data = {"title": "Things Fall Apart (Updated)"}

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_delete_book(self):
        """
        Authenticated users can delete a book.
        """
        self.client.login(username="testuser", password="testpassword")

        url = f"/api/books/{self.book1.id}/delete/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(
            self.list_url + "?publication_year=1958"
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_search_books_by_title(self):
        """
        Test search functionality.
        """
        response = self.client.get(self.list_url + "?search=Arrow")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Arrow of God")

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(
            self.list_url + "?ordering=-publication_year"
        )

        self.assertEqual(response.data[0]["title"], "Arrow of God")
