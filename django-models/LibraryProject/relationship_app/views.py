from django.shortcuts import render, redirect
# from relationship_app.models import Book, Author, Librarian, Library
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# import using FBV Function Based View

# How I did it before

# def query_all_books(request, title):
#     books = Book.objects.all(name = title)
#     authors = Author.objects.all()
#     return render(request, 'books.html', {'books': books, 'authors': authors})

# Chat GPT's help and provided code
@login_required
def list_books(request):
    books = Book.objects.all()

    context = {
        "books": books
    }

    return render(request, "relationship_app/list_books.html", context)


# Views for register
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Views for login

def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Views for logout

def logout(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/logout.html", {"form": form})



# def query_books_by_author(request, author_name):
#     books = Book.objects.filter(author__name=author_name)
#     authors = Author.objects.all()
#     return render(request, 'books.html', {'books': books, 'authors': authors})

# Using CBV Class based View

@LoginRequiredMixin
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LoginView(DetailView):
    model = Library
    template_name = "relationship_app/login.html"
    context_object_name = "library"

class LogoutView(DetailView):
    model = Library
    template_name = "relationship_app/logout.html"
    context_object_name = "library"

class RegisterView(DetailView):
    model = Library
    template_name = "relationship_app/register.html"
    context_object_name = "library"