from django import forms
from django.forms.widgets import DateInput
from app_album_viewer.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'price', 'format', 'release_date', 'description', 'cover_art']
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
        }
