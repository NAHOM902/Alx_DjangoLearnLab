from django.contrib import admin
from .models import Book

# Customize the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for the publication year and author
    list_filter = ('publication_year', 'author')

    # Enable search functionality for the title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)