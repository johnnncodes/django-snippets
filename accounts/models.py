from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField


class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')
    slug = AutoSlugField(
        populate_from=lambda instance: instance.user.get_full_name(),
        unique=True
    )

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
