from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from app_album_viewer.models import Album, Song, Comment
from .models import User


class AlbumModelTest(TestCase):
    def setUp(self):
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )

    def test_album_creation(self):
        self.assertEqual(self.album.title, "Test Album")
        self.assertEqual(self.album.artist, "Test Artist")
        self.assertEqual(self.album.price, 10.99)
        self.assertEqual(self.album.format, 'CD')

    def test_album_default_cover_art(self):
        self.assertEqual(self.album.cover_art, 'album_covers/default_cover.png')

    def test_album_release_date_future(self):
        future_date = timezone.now().date() + timezone.timedelta(days=365 * 2)
        future_album = Album.objects.create(
            title="Future Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=future_date
        )
        self.assertEqual(future_album.release_date, future_date)

    def test_user_album_comments_relationship(self):
        user = User.objects.create(username="testuser", password="testpassword")
        comment = Comment.objects.create(user=user, album=self.album, text="This is a test comment.")
        user.album_comments.add(comment)


class SongModelTest(TestCase):
    def setUp(self):
        self.song = Song.objects.create(title="Test Song", running_time=180)
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )

    def test_song_creation(self):
        self.assertEqual(self.song.title, "Test Song")
        self.assertEqual(self.song.running_time, 180)

    def test_song_albums_relationship(self):
        self.song.albums.add(self.album)
        self.assertIn(self.album, self.song.albums.all())


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            password="testpassword",
            display_name="Test User"
        )
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.password, "testpassword")
        self.assertEqual(self.user.display_name, "Test User")

    def test_user_album_comments_relationship(self):
        comment = Comment.objects.create(user=self.user, album=self.album, text="This is a test comment.")
        self.user.album_comments.add(comment)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )
        self.comment = Comment.objects.create(
            user=self.user,
            album=self.album,
            text="This is a test comment."
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.album, self.album)
        self.assertEqual(self.comment.text, "This is a test comment.")


class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_show_account_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_show_account_unauthenticated(self):
        response = self.client.get(reverse('account'))
        self.assertRedirects(response, reverse('page_login') + '?next=' + reverse('account'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('page_logout'))
        self.assertNotIn('_auth_user_id', self.client.session)


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )
        self.song = Song.objects.create(title="Test Song", running_time=180)
        self.album.songs.add(self.song)
        self.comment = Comment.objects.create(user=self.user, album=self.album, text="This is a test comment.")

    def test_show_albums_overview(self):
        response = self.client.get(reverse('albums_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'albums_overview.html')
        self.assertIn('albums', response.context)

    def test_show_album_songs(self):
        response = self.client.get(reverse('album_songs', args=[self.album.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'album_songs.html')
        self.assertIn('album', response.context)
        self.assertIn('songs', response.context)

    def test_show_album_detail(self):
        response = self.client.get(reverse('album_detail', args=[self.album.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'album_detail.html')
        self.assertIn('album', response.context)
        self.assertIn('comments', response.context)

    def test_show_account(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        self.assertIn('comments', response.context)
