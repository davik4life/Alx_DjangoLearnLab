from django.shortcuts import render
from relationship_app.models import Book, Author, Librarian, Library
from django.views.generic import DetailView

# Create your views here.
# import using FBV Function Based View

# How I did it before

# def query_all_books(request, title):
#     books = Book.objects.all(name = title)
#     authors = Author.objects.all()
#     return render(request, 'books.html', {'books': books, 'authors': authors})

# Chat GPT's help and provided code

def list_books(request):
    books = Book.objects.all()

    context = {
        "books": books
    }

    return render(request, "relationship_app/list_books.html", context)


# def query_books_by_author(request, author_name):
#     books = Book.objects.filter(author__name=author_name)
#     authors = Author.objects.all()
#     return render(request, 'books.html', {'books': books, 'authors': authors})

# Using CBV Class based View

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

