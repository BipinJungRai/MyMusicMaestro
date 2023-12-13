from django.test import TestCase

from app_album_viewer.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, 'testuser')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_password(self):
        self.assertTrue(self.user.check_password('testpassword'))
