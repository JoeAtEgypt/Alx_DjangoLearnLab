## Delete

See `delete.md`:

```python
# Delete the book and confirm deletion
from bookshelf.models import Boo
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Expected output: <QuerySet []> (empty queryset, confirming deletion)
```
