from django.contrib import admin
from snippets.models import Snippet, ApprovedTag


admin.site.register(Snippet)
admin.site.register(ApprovedTag)