from django.db import models

# Create your models here.    

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="library/images/author/photos/",
        blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)

class Book(models.Model):
    title = models.CharField(max_length=355)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_hidden = models.BooleanField(default=False)
    poster = models.ImageField(
        upload_to="library/images/books/posters/",
        blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='books')
    authors = models.ManyToManyField(
        Author, related_name='books')
    year = models.ManyToManyField(
        Year, related_name='books')

    def __str__(self):
        return self.title    



