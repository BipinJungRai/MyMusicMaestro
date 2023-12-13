from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Album(models.Model):
    # cover art image optional; they use a default image if a cover art image is not specified
    cover_art = models.ImageField(upload_to='album_covers', null=True, blank=True,
                                  default='album_covers/default_cover.png')

    # title, which is required and may not be unique
    title = models.CharField(max_length=100, unique=False, null=False, blank=False)

    # description, which could be empty
    description = models.TextField(null=True, blank=True)

    # artist, which is a string, and required
    artist = models.CharField(max_length=100, null=False, blank=False)

    # price, in GBP, which is required but may be zero
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0.00)

    # format, one of 'Digital download', 'CD', 'Vinyl'
    FORMAT_CHOICES = [
        ('Digital download', 'Digital download'),
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
    ]
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, null=False, blank=False)

    # release date; unreleased albums may have a release date up to three years in the future
    # (if more than one year away, it must be set to January)
    release_date = models.DateField(null=False, blank=False)

    # songs
    songs = models.ManyToManyField('Song', related_name='album_songs')

    # comments
    comments = models.ManyToManyField('Comment', related_name='album_comments')


class Song(models.Model):
    # title
    title = models.CharField(max_length=100, unique=False, null=False, blank=False)

    # running time in seconds
    running_time = models.IntegerField(null=False, blank=False)

    # albums
    albums = models.ManyToManyField('Album', related_name='song_albums')


class User(AbstractUser):
    # username
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)

    # password
    password = models.CharField(max_length=50, null=False, blank=False)

    # display name
    display_name = models.CharField(max_length=100, null=True, blank=True)

    # comments on albums
    album_comments = models.ManyToManyField('Comment', related_name='user_comments')

    # permissions
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    groups = models.ManyToManyField(Group, related_name='user_groups')


class Comment(models.Model):
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')

    # album
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    # comment text
    text = models.TextField(null=False, blank=False)
