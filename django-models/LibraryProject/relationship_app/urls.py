# from django.urls import path
# from .views import list_books, LibraryDetailView, LoginView, LogoutView, register
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path("books/", list_books, name="list_books"),
#     path("Libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
#     # path("login/", LoginView.as_view(), name="login"),
#     # path("logout/", LogoutView.as_view(), name="logout"),
#     # path("register/", RegisterView.as_view(), name="register"),
#     path("views.register/", RegisterView.as_view(template_name="relationship_app/register.html"), name="register"),
#     path("views.login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
#     path("views.logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
#     path("Libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
# ]

# urlpatterns = [
#     # Authentication
#     path("login/", auth_views.LoginView.as_view(
#         template_name="relationship_app/login.html"
#     ), name="login"),

#     path("logout/", auth_views.LogoutView.as_view(
#         template_name="relationship_app/logout.html"
#     ), name="logout"),

#     path("register/", register, name="register"),
# ]

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, admin_view, librarian_view, member_view, add_book, edit_book, delete_book, LibraryDetailView, register

urlpatterns = [
    path("books/", list_books, name="list-books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),

    path("login/", auth_views.LoginView.as_view(
        template_name="relationship_app/login.html"
    ), name="login"),

    path("logout/", auth_views.LogoutView.as_view(
        template_name="relationship_app/logout.html"
    ), name="logout"),

    path("register/", register, name="register"),
]


urlpatterns = [
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
]



urlpatterns = [
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
]
