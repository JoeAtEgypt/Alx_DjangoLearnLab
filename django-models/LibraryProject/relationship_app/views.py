from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Book, Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related("author").all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
