from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Book(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    publication_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    description = models.TextField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

