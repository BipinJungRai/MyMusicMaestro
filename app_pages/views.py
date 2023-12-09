from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Change this line
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app_album_viewer.models import Album, Song, Comment
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


def show_home(request):
    # logic for the home page
    return render(request, 'home.html')


def show_about(request):
    # logic for the about page
    return render(request, 'about.html')


def show_contact(request):
    # logic for the contact page
    return render(request, 'contact.html')


# fuction for the account page

def show_account(request):
    if request.method == 'POST':
        print(f'request.POST: {request.POST}')  # Debug print
        username = request.POST['username']
        password = request.POST['password']
        print(f'Username: {username}')  # Debug print
        print(f'Password: {password}')  # Debug print
        user = authenticate(request, username=username, password=password)
        print(f'User: {user}')  # Debug print
        if user is not None:
            login(request, user)
            return redirect('page_home')
        else:
            try:
                user = User.objects.get(username=username)
                print(f'Hashed password in database: {user.password}')  # Debug print
                print(f'Is the plaintext password correct: {check_password(password, user.password)}')  # Debug print
            except User.DoesNotExist:
                print('User does not exist')  # Debug print
                messages.error(request, 'Invalid username or password.')
    return render(request, 'account.html')