from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext as _


class SnippetOwnerRequiredMixin(object):

    NOT_SNIPPET_OWNER = _("You have no permission to do that action because you're not the snippet owner")

    def dispatch(self, request, *args, **kwargs):
        snippet = self.get_object()
        if request.user !=  snippet.author:
            messages.error(self.request, self.NOT_SNIPPET_OWNER)
            return redirect('user_snippets', request.user.profile.slug)
        return super(SnippetOwnerRequiredMixin, self).dispatch(
            request, *args, **kwargs)

class SnippetOwnerRequiredOnDeleteMixin(SnippetOwnerRequiredMixin):

    NOT_SNIPPET_OWNER = _("Sorry you can't delete that snippet because you are not the snippet author.")


class SnippetOwnerRequiredOnUpdateMixin(SnippetOwnerRequiredMixin):

    NOT_SNIPPET_OWNER = _("Sorry you can't update that snippet because you are not the snippet author.")