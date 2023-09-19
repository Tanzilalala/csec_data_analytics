# csec_data_analytics_app/management/commands/insert_books.py

from django.core.management.base import BaseCommand
from csec_data_analytics_app.models import Book

class Command(BaseCommand):
    help = 'Insert sample books into MongoDB'

    def handle(self, *args, **kwargs):
        # Insert sample books
        books_data = [
            {"title": "Book 1", "author": "Author 1", "genre": "Fiction", "publication_year": 2020, "price": 19.99},
            {"title": "Book 2", "author": "Author 2", "genre": "Mystery", "publication_year": 2018, "price": 14.99},
            {"title": "Book 3", "author": "Author 3", "genre": "Science Fiction", "publication_year": 2021, "price": 24.99},
        ]

        for book_data in books_data:
            book = Book(**book_data)
            book.save()

        self.stdout.write(self.style.SUCCESS('Sample books inserted successfully.'))
