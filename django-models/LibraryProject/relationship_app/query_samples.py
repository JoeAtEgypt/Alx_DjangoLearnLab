from relationship_app.models import Author, Book, Library


# Query all books by a specific author
def get_books_by_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


# List all books in a library
def get_books_in_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        books = (
            library.books.all()
        )  # Assuming a ManyToMany or ForeignKey from Book to Library
        return books
    except Library.DoesNotExist:
        return []


# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        librarian = library.librarian  # Assuming a ForeignKey from Library to Librarian
        return librarian
    except Library.DoesNotExist:
        return None
