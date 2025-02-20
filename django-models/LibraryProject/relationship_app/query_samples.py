import os
import django

from relationship_app.models import Author, Book, Librarian, Library

def query_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by author {author_name}:")
        for i in books:
            print(f"- {i.title}")

    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")


def library_books(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"books in {library_name}:")
        for i in Library:
            print(f"- {books.title} by {books.author}")
    except Library.DoesNotExist:
        print(f"library {library_name} not found.")

def him(library_name):
    try:
        library = Librarian.objects.get(name=library_name)
        Librarian = library.Librarian
        print(f"librarian for {library_name} is {Librarian.name}")
    except Library.DoesNotExist:
        print(f"library '{library_name}' does not found.")
    except Librarian.DoesNotExist:
        print(f"no librarin found for {library_name}.")

# sample outputs for testing

if __name__ == "__main__":
    print(query_author("George Orwell"))
    print(library_books("1984"))
    
