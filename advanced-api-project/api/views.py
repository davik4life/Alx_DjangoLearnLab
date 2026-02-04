from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"
from django_filter.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
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
        SearchFilter,
        OrderingFilter,
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

