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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')  # Redirect to the account page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
