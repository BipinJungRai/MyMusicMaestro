from django.urls import path
from . import views

# Dynamic Pages

urlpatterns = [
    path('album_detail/', views.show_album_detail, name='album_detail'),
    path('song_detail/', views.show_album_songs, name='song_detail'),
    path('', views.show_albums_overview, name='albums_overview'),
]
