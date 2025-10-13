from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime

class Video(models.Model):
    GENRE_CHOICES = [
        ("Comedy", "Comedy"),
        ("Romance", "Romance"),
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Sci-Fi", "Sci-Fi"),
        ("Thriller", "Thriller"),
        ("Animation", "Animation"),
        ("Other", "Other"),
    ]

    MovieID = models.CharField(max_length=20, unique=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=120)
    Actor2Name = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120)
    MovieGenre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ReleaseYear = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.now().year + 1),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
