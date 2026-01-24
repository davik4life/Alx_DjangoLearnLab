from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "create_book.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.save()
        return redirect("book_list")
    return render(request, "edit_book.html", {"book": book})
