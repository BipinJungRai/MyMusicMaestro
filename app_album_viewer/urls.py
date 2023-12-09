from django.urls import path
from . import views

# Dynamic Pages

urlpatterns = [
    path('album_detail/', views.show_album_detail, name='album_detail'),
    path('song_detail/', views.show_album_songs, name='song_detail'),
    path('', views.show_albums_overview, name='albums_overview'),
    path('album_edit/<int:album_id>/', views.edit_album, name='album_edit'),
    path('album_add/', views.add_album, name='album_add'),
    path('album_delete/<int:album_id>/', views.delete_album, name='album_delete'),
    path('album_detail/<int:album_id>/', views.show_album_detail, name='album_detail'),
    path('album_songs/<int:album_id>/', views.album_songs, name='album_songs'),

]
