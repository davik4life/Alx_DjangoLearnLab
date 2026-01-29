from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    