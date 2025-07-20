from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Book, Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
