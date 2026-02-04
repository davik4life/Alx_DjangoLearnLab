from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Enhanced List View:
    - Filtering
    - Searching
    - Ordering

    Filtering:
    - title
    - publication_year
    - author (by ID)

    Searching:
    - title
    - author name

    Ordering:
    - title
    - publication_year
    """

    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Exlicitly declare backends (optional since we set global defaults)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering (Exact matches)
    filterset_fields = {
        "title": ["exact", "icontains"],
        "publication_years": ["exact", "gte", "lte"],
        "author": ["exact"],
    }

    # Search (text-based)
    search_fields = [
        "title",
        "author__name",
    ]

    # Ordering
    ordering_fields = [
        "title",
        "publication_year",
    ]

    # Default ordering
    ordering = ["title"]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Public: Retrieve a single book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<id>/update/
    Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/
    Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

