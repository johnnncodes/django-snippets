from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class ApprovedTag(TagBase):

    approved = models.BooleanField(default=False)


class ApprovedThroughModel(GenericTaggedItemBase):

    tag = models.ForeignKey(ApprovedTag, related_name='tagged_items')


class Snippet(TimeStampedModel):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='snippets')
    slug = AutoSlugField(
        populate_from='title', 
        unique=True
    )
    approved = models.BooleanField(default=False)
    tags = TaggableManager(through=ApprovedThroughModel, blank=True)

    def get_absolute_url(self):
        return reverse('snippet_details', args=(self.slug,))