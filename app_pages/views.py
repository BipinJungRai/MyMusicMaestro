from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _

from app_album_viewer.models import Album
from app_pages.forms import RecommendFriendForm


# Function to display the home page
def show_home(request):
    return render(request, 'home.html')


# Function to display the about page
def show_about(request):
    return render(request, 'about.html')


# Function to display the contact page
def show_contact(request):
    return render(request, 'contact.html')


# Function to handle user login
def login_view(request):
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


# Function to recommend a friend
def recommend_friend(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, _('MustBeLoggedIn'))
        return HttpResponseRedirect(reverse('page_home'))

    album_id = request.GET.get('album_id', None)
    if album_id:
        album = get_object_or_404(Album, pk=album_id)
    else:
        messages.add_message(request, messages.ERROR, _('NoAlbumSpecified'))
        return HttpResponseRedirect(reverse('page_home'))
    if request.method == 'GET':
        form = RecommendFriendForm()
        to = ""
        subject = _('RecommendEmailSubject')
        message = _('RecommendEmailMessageWithUser') % {'user': request.user.display_name, 'album': album.title}
        form = RecommendFriendForm({'to': to, 'subject': subject, 'message': message})
    else:
        form = RecommendFriendForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, request.user.email, [to])
            messages.add_message(request, messages.SUCCESS, _('RecommendEmailSent'))
            return HttpResponseRedirect(reverse('page_home'))
    return render(request, 'recommend_friend.html', {'form': form, 'album': album})
