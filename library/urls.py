from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),

    path('books/', book_list, name='book_list'),
    path('categories/', category_list, name='category_list'),
    path('years/', year_list, name='year_list'),
    path('authors/', author_list, name='author_list'),

    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('year/<int:year_id>/', year_detail, name='year_detail'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),

    path('buy_book/', buy_book, name='buy_book'),
    path('rent_book/', rent_book, name='rent_book'),
]