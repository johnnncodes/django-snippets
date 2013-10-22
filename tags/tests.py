from libs.mixins.test import BaseTestCase
from django.core.urlresolvers import reverse

from snippets.models import Snippet
from .models import ApprovedTag


class TagsViewTest(BaseTestCase):

    def test_can_load_tags_page_properly(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['tags'])


class CreateTagViewTest(BaseTestCase):

    def test_create_tag(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        # invalid
        response = self.client.post(reverse('tag_create', \
            args=(self.user.profile.slug,)), {'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.', count=1)

        # valid
        response = self.client.post(reverse('tag_create', args=(self.user.profile.slug,)), \
            {'name': 'My first tag'}, follow=True)
        self.assertRedirects(response, reverse('tag_create', args=(self.user.profile.slug,)))        
        self.assertIn('Tag successfully submitted and waiting for the approval of the site admin.', \
            response.content)


class TagSnippetsViewTest(BaseTestCase):

    def test_can_load_tag_snippets_page_properly(self):
        tag = ApprovedTag.objects.create(name='authentication', author=self.user)
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('tag_snippets', args=(tag.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['snippets'])