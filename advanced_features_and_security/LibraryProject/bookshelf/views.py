from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book


# Example: View to create a book (requires can_create permission)
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(
            title=title, author=author, publication_year=publication_year
        )
        return redirect("book_list")  # Replace with your book list view name
    return render(request, "bookshelf/create_book.html")


# Example: View to edit a book (requires can_edit permission)
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("book_list")  # Replace with your book list view name
    return render(request, "bookshelf/edit_book.html", {"book": book})


# Example: View to delete a book (requires can_delete permission)
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")  # Replace with your book list view name
    return render(request, "bookshelf/confirm_delete.html", {"book": book})
