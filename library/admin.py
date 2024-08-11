from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'birth_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster')

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)