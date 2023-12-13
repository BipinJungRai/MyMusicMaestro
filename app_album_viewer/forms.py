from django import forms
from django.forms.widgets import DateInput

from app_album_viewer.models import Album, Song


class AlbumForm(forms.ModelForm):
    # Meta class is used to provide specifications on the AlbumForm fields
    class Meta:
        model = Album
        fields = ['title', 'artist', 'price', 'format', 'release_date', 'description', 'cover_art']
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
        }


class SongForm(forms.ModelForm):
    # Meta class is used to provide specifications on the SongForm fields
    class Meta:
        model = Song
        fields = ['title', 'running_time']
