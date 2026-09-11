from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book

@login_required
def book_list(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.filter(owner=request.user)

    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    return render(
        request,
        "library/book_list.html",
        {"books": books, "query": query},
    )


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    return render(request, "library/book_detail.html", {"book": book})

@login_required
def book_create(request):
    form = BookForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        book = form.save(commit=False)
        book.owner = request.user
        book.save()
        messages.success(request, "Book added successfully.")
        return redirect("library:book-detail", pk=book.pk)

    return render(
        request,
        "library/book_form.html",
        {"form": form, "heading": "Add book"},
    )

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Book updated successfully.")
        return redirect("library:book-detail", pk=book.pk)

    return render(
        request,
        "library/book_form.html",
        {"form": form, "book": book, "heading": "Edit book"},
    )


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, owner=request.user)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect("library:book-list")

    return render(
        request,
        "library/book_delete.html",
        {"book": book},
    )


