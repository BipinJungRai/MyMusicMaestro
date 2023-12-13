from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Album


# Test case for Album Viewer
class AlbumViewerTest(TestCase):
    # Setup for Album Viewer test case
    def setUp(self):
        self.album = Album.objects.create(
            title='Test Album',
            artist='Test Artist',
            price=Decimal('10.00'),
            format='CD',
            release_date=date.today()
        )

    # Test case for album creation
    def test_album_creation(self):
        self.assertEqual(self.album.title, 'Test Album')
        self.assertEqual(self.album.artist, 'Test Artist')
        self.assertEqual(self.album.price, Decimal('10.00'))
        self.assertEqual(self.album.format, 'CD')

    # Test case for showing albums overview
    def test_show_albums_overview(self):
        response = self.client.get(reverse('albums_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album')
        self.assertTemplateUsed(response, 'albums_overview.html')

    # Test case for adding an album
    def test_add_album(self):
        url = reverse('album_add')
        data = {
            'title': 'New Album',
            'artist': 'New Artist',
            'price': '15.00',
            'format': 'CD',
            'release_date': '2022-12-31'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Album.objects.count(), 2)
        self.assertEqual(Album.objects.get(title='New Album').artist, 'New Artist')


class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_show_account(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('page_logout'))
        self.assertNotIn('_auth_user_id', self.client.session)
