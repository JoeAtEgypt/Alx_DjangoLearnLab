# CRUD Operations Documentation

## Create

See `create.md`:

```python
# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: Book instance created successfully with id=<some_id>
```

---

## Retrieve

See `retrieve.md`:

```python
# Retrieve and display all attributes of the created book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
```

---

## Update

See `update.md`:

```python
# Update the title of "1984" to "Nineteen Eighty-Four"
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected output: Nineteen Eighty-Four
```

---

## Delete

See `delete.md`:

```python
# Delete the book and confirm deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Expected output: <QuerySet []> (empty queryset, confirming deletion)
```