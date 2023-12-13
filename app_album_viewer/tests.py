from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from app_album_viewer.models import Album, Song, Comment
from .models import User


# Test class for Album model
class AlbumModelTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create an Album instance with sample data
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )

    # Test case for album creation and attributes
    def test_album_creation(self):
        # Assertions for album attributes
        self.assertEqual(self.album.title, "Test Album")
        self.assertEqual(self.album.artist, "Test Artist")
        self.assertEqual(self.album.price, 10.99)
        self.assertEqual(self.album.format, 'CD')

    # Test case for default album cover art
    def test_album_default_cover_art(self):
        self.assertEqual(self.album.cover_art, 'album_covers/default_cover.png')

    # Test case for future album release date
    def test_album_release_date_future(self):
        # Create an Album instance with a future release date
        future_date = timezone.now().date() + timezone.timedelta(days=365 * 2)
        future_album = Album.objects.create(
            title="Future Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=future_date
        )
        # Assertion for the future release date
        self.assertEqual(future_album.release_date, future_date)

    # Test case for user-album-comments relationship
    def test_user_album_comments_relationship(self):
        # Create a User instance and a Comment instance related to the album
        user = User.objects.create(username="testuser", password="testpassword")
        comment = Comment.objects.create(user=user, album=self.album, text="This is a test comment.")
        user.album_comments.add(comment)


# Test class for Song model
class SongModelTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create a Song instance and an Album instance
        self.song = Song.objects.create(title="Test Song", running_time=180)
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format='CD',
            release_date=timezone.now().date()
        )

    # Test case for song creation and attributes
    def test_song_creation(self):
        # Assertions for song attributes
        self.assertEqual(self.song.title, "Test Song")
        self.assertEqual(self.song.running_time, 180)

    # Test case for song-albums relationship
    def test_song_albums_relationship(self):
        # Add the album to the song's related albums and assert its presence
        self.song.albums.add(self.album)
        self.assertIn(self.album, self.song.albums.all())


# Test class for User model
class UserModelTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create a User instance and an Album instance
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

    # Test case for user creation and attributes
    def test_user_creation(self):
        # Assertions for user attributes
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.password, "testpassword")
        self.assertEqual(self.user.display_name, "Test User")

    # Test case for user-album-comments relationship
    def test_user_album_comments_relationship(self):
        # Create a Comment instance related to the user and the album
        comment = Comment.objects.create(user=self.user, album=self.album, text="This is a test comment.")
        self.user.album_comments.add(comment)


# Test class for Comment model
class CommentModelTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create a User instance, an Album instance, and a Comment instance
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

    # Test case for comment creation and attributes
    def test_comment_creation(self):
        # Assertions for comment attributes
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.album, self.album)
        self.assertEqual(self.comment.text, "This is a test comment.")


# Test class for authentication-related views
class AuthenticationTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create a Django client and a user for authentication testing
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    # Test case for authenticated account view
    def test_show_account_authenticated(self):
        # Log in the user, make a request to the account view, and assert the response
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    # Test case for unauthenticated account view
    def test_show_account_unauthenticated(self):
        # Make a request to the account view without logging in and assert the redirection
        response = self.client.get(reverse('account'))
        self.assertRedirects(response, reverse('page_login') + '?next=' + reverse('account'))

    # Test case for user logout view
    def test_logout_view(self):
        # Log in the user, make a request to the logout view, and assert the session state
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('page_logout'))
        self.assertNotIn('_auth_user_id', self.client.session)


# Test class for views in the application
class ViewTest(TestCase):
    # Set up the initial data for testing
    def setUp(self):
        # Create a Django client, a user, an album, a song, and a comment for view testing
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
        self.comment
