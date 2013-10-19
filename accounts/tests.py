from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class LoginViewTest(TestCase):

    USERNAME = 'john'
    EMAIL = 'john@gmail.com'
    PASSWORD = 'admin'

    def setUp(self):
        User.objects.create_user(self.USERNAME, self.EMAIL, self.PASSWORD)

    def test_login_logout(self):
        # login using wrong credentials
        response = self.client.post(reverse('login'), \
            {'username': 'john', 'password': 'wrong password'}, \
            follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertIn('Invalid username and password', response.content)

        # login using correct credentials
        response = self.client.post(reverse('login'), \
            {'username': self.USERNAME, 'password': self.PASSWORD})
        self.assertRedirects(response, reverse('snippets'))

        # logout
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

