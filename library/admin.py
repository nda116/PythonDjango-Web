from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "owner", "updated_at")
    search_fields = ("title", "author", "owner__username")
    list_filter = ("publication_year",)
