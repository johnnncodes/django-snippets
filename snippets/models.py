from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField


class Snippet(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='snippets')
    slug = AutoSlugField(
        populate_from='title', 
        unique=True
    )

    def get_absolute_url(self):
        return reverse('snippet_details', args=(self.slug,))