from django.db import models
from django.contrib.auth.models import User

from taggit.models import TagBase, GenericTaggedItemBase


class ApprovedTag(TagBase):

    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='tags')


class ApprovedThroughModel(GenericTaggedItemBase):

    tag = models.ForeignKey(ApprovedTag, related_name='tagged_items')