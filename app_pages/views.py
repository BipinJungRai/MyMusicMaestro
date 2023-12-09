from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Change this line
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
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
     return render(request, 'account.html')

def show_login(request):
    # logic for the login page
    return render(request, 'login.html')
