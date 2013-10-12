from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class SnippetsTest(TestCase):

    def setUp(self):
        self.client = Client()
        username = 'username'
        email = 'email'
        password = 'password'
        self.user = User.objects.create_user(username, email, password)

    def test_snippets_page(self):
        username = 'username'
        password = 'password'

        self.client.login(username=username, password=password)

        response = self.client.get(reverse('snippets'))
        self.assertEqual(response.status_code, 200)

        self.assertIsNotNone(response.context['snippets'])

    def test_create_snippet_view(self):
        username = 'username'
        password = 'password'

        self.client.login(username=username, password=password)

        # invalid
        response = self.client.post(reverse('snippet_create', args=(self.user.profile.slug,)), \
            {'title': '', 'body': ''})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.', count=2)

        # valid
        response = self.client.post(reverse('snippet_create', args=(self.user.profile.slug,)), \
            {'title': 'title', 'body': 'body'})

        self.assertRedirects(response, reverse('user_snippets', args=(self.user.profile.slug,)))


