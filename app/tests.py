from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):

    def test_registration(self):
        # valid
        response = self.client.post(reverse('home'), \
            {'username': 'john', 'password1': 'admin', 'password2': 'admin'}, \
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Successfully registered!', response.content)

        # invalid
        response = self.client.post(reverse('home'), \
            {'username': '', 'password1': '', 'password2': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('This field is required.', response.content)

    def test_can_load_home_page_properly(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h3>Login</h3>', response.content)
        self.assertIn('<h3>Register</h3>', response.content)

