from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from app_album_viewer.forms import AlbumForm
from app_album_viewer.models import Album, Song


# Create your views here.
def show_albums_overview(request):
    query = request.GET.get('q')
    if query:
        albums = Album.objects.filter(title__icontains=query)
    else:
        albums = Album.objects.all()
    return render(request, 'albums_overview.html', {'albums': albums})


def show_album_detail(request, album_id, slug=None):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})


def show_album_songs(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()
    return render(request, 'album_songs.html', {'album': album, 'songs': songs})


def edit_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums_overview')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_edit.html', {'form': form})


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums_overview')
    else:
        form = AlbumForm()
    return render(request, 'album_add.html', {'form': form})


def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return redirect('albums_overview')


def album_songs(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()
    return render(request, 'album_songs.html', {'album': album, 'songs': songs})


def show_album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})


def show_album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    comments = album.comments.all()
    return render(request, 'album_detail.html', {'album': album, 'comments': comments})


def song_choices(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        song_ids = request.POST.getlist('song_ids')
        songs = Song.objects.filter(id__in=song_ids)
        album.songs.clear()
        album.songs.add(*songs)
        return redirect('album_songs', album_id=album.id)
    else:
        all_songs = Song.objects.all()
        selected_songs = album.songs.all()
        unselected_songs = all_songs.difference(selected_songs)
        return render(request, 'song_choices.html',
                      {'selected_songs': selected_songs, 'unselected_songs': unselected_songs, 'album': album})


# fuction for the account page
from app_album_viewer.models import Comment


@login_required(login_url='page_login')
def show_account(request):
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'account.html', {'comments': comments})


def logout_view(request):
    logout(request)
    return redirect('page_home')  # Redirect to the home page after logout
