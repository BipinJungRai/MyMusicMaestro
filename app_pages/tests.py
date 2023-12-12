from django.test import TestCase, Client
from django.urls import reverse

from app_album_viewer.models import User


# This class is for testing the login view
class LoginViewTest(TestCase):
    # This method sets up the necessary objects for the tests
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('page_login')

    # This method tests the case where the login is successful
    def test_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    # This method tests the case where the login fails
    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')


# This class is for testing the login template
class LoginTemplateTest(TestCase):
    # This method tests that the correct template is used for the login view
    def test_template_used(self):
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


# This class is for testing the home page template
class HomePageTest(TestCase):
    # This method tests that the home page template is used
    def test_home_page(self):
        response = self.client.get(reverse('page_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


# This class is for testing the about page template
class AboutPageTest(TestCase):
    # This method tests that the about page template is used
    def test_about_page(self):
        response = self.client.get(reverse('page_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


# This class is for testing the contact page template
class ContactPageTest(TestCase):
    # This method tests that the contact page template is used
    def test_contact_page(self):
        response = self.client.get(reverse('page_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
