from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.faker = User.objects.create_user(
            username="Faker",
            password="StrongPass123!",
        )
        self.messi = User.objects.create_user(
            username="Messi",
            password="StrongPass123!",
        )
        Book.objects.create(owner=self.faker, title="Harry Potter", author="J.K. Rowling", publication_year=1997)
        Book.objects.create(owner=self.messi, title="Sherlock Holmes", author="Arthur Conan Doyle", publication_year=1887)

    def test_login_is_required(self):
        response = self.client.get(reverse("library:book-list"))
        self.assertEqual(response.status_code, 302)

    def test_user_only_sees_their_own_books(self):
        self.client.login(username="Faker", password="StrongPass123!")
        response = self.client.get(reverse("library:book-list"))

        self.assertContains(response, "Harry Potter")
        self.assertNotContains(response, "Sherlock Holmes")
