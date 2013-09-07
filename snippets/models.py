from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Snippet(TimeStampedModel):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='snippets')
    slug = AutoSlugField(
        populate_from='title', 
        unique=True
    )
    approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('snippet_details', args=(self.slug,))