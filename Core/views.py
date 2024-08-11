from Core.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        r_password = request.POST['repeat_password']
        if password != r_password:
            return render(request, 'Core/signup.html', {
                'error': 'Пароли не совпадают.'
            })
        User.objects.create_user(
            username=username, 
            email=email,
            password=password,
        )
        return redirect('signin')
    return render(request, 'Core/auth/signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password
        )
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'Core/auth/signin.html', {
                'error': 'Неверный логин или пароль.'
            })
    return render(request, 'Core/auth/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'Core/auth/profile.html')