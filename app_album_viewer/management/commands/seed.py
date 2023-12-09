import json
from pathlib import Path
from app_album_viewer.models import Album, Song, User, Comment
from django.core.management import BaseCommand
from django.core.files.images import ImageFile

ROOT_DIR = Path('app_album_viewer') / 'management'


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):

        # Clear existing data
        Album.objects.all().delete()
        Song.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()

        with open(ROOT_DIR / 'sample_data.json') as json_file:
            sample_data = json.load(json_file)
            for album_data in sample_data['albums']:

                # Create user
                user, created = User.objects.get_or_create(
                    display_name=album_data['comments'][0]['user__display_name'],
                    defaults={'password': 'password'}
                )

                # Set the password
                user.set_password('password')

                # Set the username as display_name + "#" + user id
                user.username = f"{user.display_name}#{user.id}"

                # Save the user
                user.save()

                # Cover art handling
                image_path = album_data['cover']
                if image_path is not None:
                    cover_art_path = Path('app_album_viewer/media/Album Covers') / image_path
                    kwargs = {'cover_art': ImageFile(open(cover_art_path, 'rb'), name=image_path)}
                else:
                    kwargs = {}

                # Create album
                album = Album.objects.create(
                    title=album_data['title'],
                    artist=album_data['artist'],
                    price=album_data['price'],
                    format=album_data['format'],
                    release_date=album_data['release_date'],
                    **kwargs
                )

                # Create songs and associate them with the album
                for song_data in sample_data['songs']:
                    if album_data['title'] in song_data['albums']:
                        song, created = Song.objects.get_or_create(
                            title=song_data['title'],
                            running_time=song_data['runtime']
                        )
                        album.songs.add(song)
                        song.albums.add(album)

                # Create comments and associate them with the user and album
                for comment_data in album_data['comments']:
                    comment = Comment.objects.create(
                        user=user,
                        album=album,
                        text=comment_data['message']
                    )
                    user.album_comments.add(comment)
                    album.comments.add(comment)

                # Save the album
                album.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
