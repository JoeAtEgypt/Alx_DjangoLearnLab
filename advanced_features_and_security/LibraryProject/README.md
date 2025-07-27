# Django Custom Permissions and Groups Setup Guide

## Custom Permissions for Book Model

The following custom permissions are defined in `bookshelf/models.py` for the `Book` model:

- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

## Groups Setup

Three groups are recommended:

- **Editors**: Assigned `can_view`, `can_create`, `can_edit`
- **Viewers**: Assigned `can_view`
- **Admins**: Assigned all four permissions

To create and assign these permissions programmatically, use the script in the comment at the bottom of `bookshelf/admin.py`.

## Assigning Users to Groups

1. Go to the Django admin site (`/admin/`).
2. Create users or use existing ones.
3. Assign users to the appropriate group (Editors, Viewers, Admins) via the user edit page.

## Permission Enforcement in Views

Views that create, edit, or delete books are protected using the following decorators:

- `@permission_required('bookshelf.can_create', raise_exception=True)`
- `@permission_required('bookshelf.can_edit', raise_exception=True)`
- `@permission_required('bookshelf.can_delete', raise_exception=True)`

Only users with the corresponding permissions (via group membership) can access these views.

## Manual Testing Steps

1. **Create test users** in the Django admin.
2. **Assign each user to a different group** (Editors, Viewers, Admins).
3. **Log in as each user** and attempt to:
   - Create a book (should require `can_create`)
   - Edit a book (should require `can_edit`)
   - Delete a book (should require `can_delete`)
   - View books (should require `can_view`)
4. **Expected Results:**
   - Editors: Can view, create, and edit books, but cannot delete.
   - Viewers: Can only view books.
   - Admins: Can view, create, edit, and delete books.

If a user lacks the required permission, they will receive a 403 Forbidden error when accessing the protected view.

## Notes

- Permissions are enforced using the variable names: `can_view`, `can_create`, `can_edit`, `can_delete`.
- You can further customize permissions and groups as needed for your application.
