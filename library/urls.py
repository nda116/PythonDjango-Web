from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("new/", views.book_create, name="book-create"),
    path("<int:pk>/", views.book_detail, name="book-detail"),
    path("<int:pk>/edit/", views.book_update, name="book-update"),
    path("<int:pk>/delete/", views.book_delete, name="book-delete"),
]