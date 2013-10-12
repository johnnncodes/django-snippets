from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class AppTest(TestCase):

    def setUp(self):
        self.client = Client()
        username = 'username'
        email = 'email'
        password = 'password'
        User.objects.create_user(username, email, password)

    def test_login_logout(self):
        username = 'username'
        password = 'password'

        # login using wrong credentials
        response = self.client.post(reverse('login'), \
            {'username': username, 'password': 'wrong password'})

        self.assertRedirects(response, reverse('home'))

        # login using correct credentials
        response = self.client.post(reverse('login'), \
            {'username': username, 'password': password})

        self.assertRedirects(response, reverse('snippets'))

        # logout
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

    def test_register(self):
        username = 'unregistered_username'
        password = 'unregistered_password'

        # valid
        response = self.client.post(reverse('home'), \
            {'username': username, 'password1': password, 'password2': password})
       
        self.assertEqual(response.status_code, 302)

        # invalid
        response = self.client.post(reverse('home'), \
            {'username': '', 'password1': '', 'password2': ''})
        
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
