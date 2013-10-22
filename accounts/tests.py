from django.core.urlresolvers import reverse

from libs.mixins.test import BaseTestCase


class LoginViewTest(BaseTestCase):

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

