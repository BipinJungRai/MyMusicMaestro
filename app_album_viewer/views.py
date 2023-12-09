from django.shortcuts import render, get_object_or_404

from app_album_viewer.models import Album


# Create your views here.
def show_albums_overview(request):
    albums = Album.objects.all()
    return render(request, 'albums_overview.html', {'albums': albums})


def show_album_detail(request, album_id, slug=None):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})


def show_album_songs(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()
    return render(request, 'album_songs.html', {'album': album, 'songs': songs})
