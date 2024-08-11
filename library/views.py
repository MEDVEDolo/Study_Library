from django.shortcuts import render, redirect
from .models import *
from Core.models import *
import dateutil.relativedelta as relativedelta
import datetime

# Create your views here.
def main(request):
    user = User.objects.get(id=request.user.id)
    rents = user.rents.filter(user=user)
    today = datetime.date.today()
    messages = []
    for rent in rents:
        delta = datetime.timedelta(weeks=1)
        first_time = rent.end - delta
        if today >= first_time and today <= rent.end:
            days = str(rent.end - today)
            days_id = days.find(' ')
            days = days[0 : (days_id)]
            message = 'Аренда книги: ' + rent.book.title + ' закончится через - ' + days + ' дней'
            messages.append(message)
            if today == rent.end:
                rent.delete()
        else:
            message = 'Аренда книг ещё не скоро закончится'
            messages.append(message)

    return render(request, 'library/main.html', {'messages': messages})

def book_list(request): 
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books
    })

def category_list(request): 
    categories = Category.objects.all()
    return render(request, 'library/category_list.html', {
        'categories': categories
    })

def year_list(request): 
    years = Year.objects.all()
    return render(request, 'library/year_list.html', {
        'years': years
    })

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {
        'authors': authors, 'title': 'Авторы'
    })

def book_detail(request, book_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    book_list_buy = []
    book_list_rent = []
    books_buy = user.books_purchased.all()
    rents = user.rents.filter(user=user)
    for book_buy in books_buy:
        book_list_buy.append(book_buy.title)
    for rent in rents:
        book_list_rent.append(rent.book.title)
    return render(request, 'library/book_detail.html', {
        'book': book,
        'book_list_buy': book_list_buy,
        'book_list_rent': book_list_rent
    })

def category_detail(request, category_id):  # Сами
    category = Category.objects.get(id=category_id)
    books = category.books.all()
    return render(request, 'library/category_detail.html', {
        'category': category, 'books': books
    })

def year_detail(request, year_id):  # Сами
    year = Year.objects.get(id=year_id)
    books = year.books.all()
    return render(request, 'library/category_detail.html', {
        'year': year, 'books': books
    })

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.books.all()
    return render(request, 'library/author_detail.html', {
        'author': author,
        'books': books
    })

def buy_book(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        user = User.objects.get(id=request.user.id)
        book = Book.objects.get(id=book_id)
        user.books_purchased.add(book)
        return redirect('book_list')

def rent_book(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(id=book_id)
        time = request.POST.get('time')
        user = User.objects.get(id=request.user.id)
        today = datetime.date.today()
        if time == 'two_weeks':
            delta = datetime.timedelta(weeks=2)
        elif time == 'mounth':
            delta = relativedelta.relativedelta(months=1)
        else:
            delta = relativedelta.relativedelta(months=3)
        end_time = today + delta
        Rent.objects.create(
            book=book,
            user=user,
            end=end_time
        )
        return redirect('book_list')