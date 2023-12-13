from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase, Client
from django.urls import reverse

# Getting the user model
User = get_user_model()


# Test case for views
class ViewTest(TestCase):
    # Test case for home view
    def test_home_view(self):
        response = self.client.get(reverse('page_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # Test case for about view
    def test_about_view(self):
        response = self.client.get(reverse('page_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    # Test case for contact view
    def test_contact_view(self):
        response = self.client.get(reverse('page_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    # Test case for login view
    def test_login_view(self):
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    # Test case for recommend friend view
    def test_recommend_friend_view(self):
        response = self.client.get(reverse('recommend_friend'))
        self.assertEqual(response.status_code, 302)


# Test case for mailer
class MailerTest(TestCase):
    # Test case for mailer function
    def test_mailer(self):
        mail.send_mail(
            'Hello',
            'Body goes here',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Hello')


# Test case for login view
class LoginViewTest(TestCase):
    # Setup for login view test case
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('page_login')

    # Test case for successful login
    def test_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)

    # Test case for failed login
    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')


# Test case for logout view
class LogoutViewTest(TestCase):
    # Setup for logout view test case
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.logout_url = reverse('page_logout')

    # Test case for logout
    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)


# Test case for login template
class LoginTemplateTest(TestCase):
    # Test case for login template
    def test_template_used(self):
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


# Test case for home page
class HomePageTest(TestCase):
    # Test case for home page
    def test_home_page(self):
        response = self.client.get(reverse('page_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


# Test case for about page
class AboutPageTest(TestCase):
    # Test case for about page
    def test_about_page(self):
        response = self.client.get(reverse('page_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


# Test case for contact page
class ContactPageTest(TestCase):
    # Test case for contact page
    def test_contact_page(self):
        response = self.client.get(reverse('page_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


# Test case for error handling
class ErrorHandlingTest(TestCase):
    # Setup for error handling test case
    def setUp(self):
        self.client = Client()
        self.error_url = '/dummy_url/'

    # Test case for error handling
    def test_error_handling(self):
        response = self.client.get(self.error_url)
        self.assertEqual(response.status_code, 404)
