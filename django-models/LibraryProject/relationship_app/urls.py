from django.urls import path

from .views import LibraryDetailView, list_books, login_view, logout_view, register_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", login_view, name="login"),
    path(
        "logout/",
        logout_view.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", register_view, name="register"),
]
