from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import (
    LibraryDetailView,
    add_book,
    admin_view,
    delete_book,
    edit_book,
    librarian_view,
    list_books,
    member_view,
)

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path("admin-dashboard/", admin_view, name="admin_dashboard"),
    path("librarian-dashboard/", librarian_view, name="librarian_dashboard"),
    path("member-dashboard/", member_view, name="member_dashboard"),
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:pk>/", edit_book, name="edit_book"),
    path("delete_books/<int:pk>/", delete_book, name="delete_book"),
]
