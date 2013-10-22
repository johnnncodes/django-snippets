from django.core.urlresolvers import reverse

from libs.mixins.test import BaseTestCase
from snippets.models import Snippet


class SnippetsViewTest(BaseTestCase):

    def test_can_load_snippets_page_properly(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('snippets'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['snippets'])


class SnippetDetailsViewTest(BaseTestCase):

    def test_can_load_snippet_detail_page_properly(self):
        snippet = Snippet(title='title', body='body', author=self.user)
        snippet.save()

        # invalid (not logged in)
        response = self.client.get(reverse('snippet_details', args=(snippet.slug,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('home') + '?next=/snippets/%s/' % snippet.slug)

        # invalid (logged-in but snippet is not yet approved and user is not the snippet author)
        self.client.login(username=self.USERNAME2, password=self.PASSWORD2)
        response = self.client.get(reverse('snippet_details', args=(snippet.slug,)), follow=True)
        self.assertEqual(response.status_code, 404)

        # valid (if the author is the current logged in user)
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('snippet_details', args=(snippet.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['snippet'])


class CreateSnippetViewTest(BaseTestCase):

    def test_create_snippet(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        # invalid
        response = self.client.post(reverse('snippet_create', \
            args=(self.user.profile.slug,)), {'title': '', 'body': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.', count=2)

        # valid
        response = self.client.post(reverse('snippet_create', args=(self.user.profile.slug,)), \
            {'title': 'My first snippet', 'body': 'The snippet body'}, follow=True)
        self.assertRedirects(response, reverse('user_snippets', args=(self.user.profile.slug,)))        
        self.assertIn('My first snippet', response.content)


class SnippetDeleteViewTest(BaseTestCase):

    def test_delete_snippet(self):
        snippet = Snippet(title='title', body='body', author=self.user)
        snippet.save()

        # invalid (not logged-in)
        response = self.client.post(reverse('snippet_delete', args=(snippet.slug,)))
        self.assertRedirects(response, reverse('home') + '?next=/snippets/title/delete/')

        # invalid (logged-in, not snippet owner)
        self.client.login(username=self.USERNAME2, password=self.PASSWORD2)
        response = self.client.post(reverse('snippet_delete', \
            args=(snippet.slug,)), follow=True)
        self.assertRedirects(response, reverse('user_snippets', args=(self.user2.profile.slug,)))       
        self.assertIn("Sorry you can't delete that snippet because you are not the snippet author.", \
            response.content.replace('&#39;', "'"))

        # valid (logged-in, snippet owner)
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(reverse('snippet_delete', args=(snippet.slug,)))
        self.assertRedirects(response, reverse('snippets'))


class SnippetUpdateViewTest(BaseTestCase):

    def test_update_snippet(self):
        snippet = Snippet(title='title', body='body', author=self.user)
        snippet.save()

        # invalid (not logged-in)
        response = self.client.post(reverse('snippet_update', args=(snippet.slug,)))
        self.assertRedirects(response, reverse('home') + '?next=/snippets/title/update/')

        # invalid (logged-in, not snippet owner)
        self.client.login(username=self.USERNAME2, password=self.PASSWORD2)
        response = self.client.post(reverse('snippet_update', \
            args=(snippet.slug,)), follow=True)
        self.assertRedirects(response, reverse('user_snippets', args=(self.user2.profile.slug,)))       
        self.assertIn("Sorry you can't update that snippet because you are not the snippet author.", \
            response.content.replace('&#39;', "'"))

        # valid (logged-in, snippet owner)
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(reverse('snippet_update', args=(snippet.slug,)), \
            {'title': 'new title', 'body': 'new body'})
        self.assertRedirects(response, reverse('snippet_details', args=(snippet.slug,)))


class MySnippetsViewTest(BaseTestCase):

    def test_can_load_my_snippets_page_properly(self):
        # logged-in
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('user_snippets', args=(self.user.profile.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['snippets'])