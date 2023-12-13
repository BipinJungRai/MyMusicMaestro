from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def show_home(request):
    # logic for the home page
    return render(request, 'home.html')


def show_about(request):
    # logic for the about page
    return render(request, 'about.html')


def show_contact(request):
    # logic for the contact page
    return render(request, 'contact.html')


def login_view(request):
    # logic for the login page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:

            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
