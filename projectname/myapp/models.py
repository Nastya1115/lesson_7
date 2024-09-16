from django.db import models

# Create your models here..

class LibraryBook(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=100, unique=True)
    available = models.BooleanField()

    class Meta():
        ordering = ['author']