from django.shortcuts import render, redirect, get_object_or_404
# from relationship_app.models import Book, Author, Librarian, Library
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
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




def is_admin(user):
    return user.is_authenticated and user.profile.role == "Admin"


def is_librarian(user):
    return user.is_authenticated and user.profile.role == "Librarian"


def is_member(user):
    return user.is_authenticated and user.profile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Add Book View Create
@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")

        Book.objects.create(
            title=title,
            author_id=author_id
        )
        return redirect("/books/")

    return render(request, "relationship_app/add_book.html")

# Edit Book View (Update)
@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.save()
        return redirect("/books/")

    return render(
        request,
        "relationship_app/edit_book.html",
        {"book": book}
    )

# Delete Book view (Delete)
@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("/books/")

    return render(
        request,
        "relationship_app/delete_book.html",
        {"book": book}
    )
