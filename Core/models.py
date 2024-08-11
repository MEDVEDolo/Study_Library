from django.contrib.auth.models import AbstractUser
from django.db import models
from library.models import Book

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, blank=True
    )
    books_purchased = models.ManyToManyField(Book, verbose_name='buyers', blank=True, null=True)

class Rent(models.Model):
    book = models.ForeignKey(Book, related_name='rents', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rents', on_delete=models.CASCADE)
    end = models.DateField()    

    def __str__(self):
        return str(self.user) + ': ' + str(self.book)