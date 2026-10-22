from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.SmallIntegerField(default=2010)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=250)
    price = models.SmallIntegerField(default=1000)
    published_year = models.CharField(max_length=100)
    pages = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")