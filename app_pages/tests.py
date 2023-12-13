from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('page_login')

    def test_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.logout_url = reverse('page_logout')

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to home page


class LoginTemplateTest(TestCase):
    def test_template_used(self):
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('page_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class AboutPageTest(TestCase):
    def test_about_page(self):
        response = self.client.get(reverse('page_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


class ContactPageTest(TestCase):
    def test_contact_page(self):
        response = self.client.get(reverse('page_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
