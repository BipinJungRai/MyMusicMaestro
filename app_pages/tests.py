from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

# Getting the user model
User = get_user_model()


# LoginViewTest class tests the login functionality
class LoginViewTest(TestCase):
    # Setting up the test environment
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


# LogoutViewTest class tests the logout functionality
class LogoutViewTest(TestCase):
    # Setting up the test environment
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.logout_url = reverse('page_logout')

    # Test case for logout
    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to home page


# LoginTemplateTest class tests if the correct template is used for the login page
class LoginTemplateTest(TestCase):
    # Test case for checking the template used
    def test_template_used(self):
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


# HomePageTest class tests if the correct template is used for the home page
class HomePageTest(TestCase):
    # Test case for checking the home page
    def test_home_page(self):
        response = self.client.get(reverse('page_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


# AboutPageTest class tests if the correct template is used for the about page
class AboutPageTest(TestCase):
    # Test case for checking the about page
    def test_about_page(self):
        response = self.client.get(reverse('page_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


# ContactPageTest class tests if the correct template is used for the contact page
class ContactPageTest(TestCase):
    # Test case for checking the contact page
    def test_contact_page(self):
        response = self.client.get(reverse('page_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


# ErrorHandlingTest class tests how the application handles requests to a non-existent URL
class ErrorHandlingTest(TestCase):
    # Setting up the test environment
    def setUp(self):
        self.client = Client()
        self.error_url = '/dummy_url/'

    # Test case for error handling
    def test_error_handling(self):
        response = self.client.get(self.error_url)
        self.assertEqual(response.status_code, 404)
