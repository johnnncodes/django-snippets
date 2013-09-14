from django.shortcuts import redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.utils.translation import ugettext as _

from braces.views import LoginRequiredMixin

from snippets.models import Snippet
from snippets.forms import (
    CreateSnippetForm,
    UpdateSnippetForm
)


class SnippetsView(LoginRequiredMixin, ListView):
   
    template_name = 'snippets/snippets.html'
    model = Snippet
    context_object_name = 'snippets'

    def get_queryset(self):
        return self.model.objects.filter(approved=True).order_by('-created')


class SnippetDetailsView(LoginRequiredMixin, DetailView):

    template_name = 'snippets/snippet_details.html'
    model = Snippet
    context_object_name = 'snippet'


class CreateSnippetView(LoginRequiredMixin, CreateView):

    template_name = 'snippets/create.html'
    model = Snippet
    form_class = CreateSnippetForm
    success_url = reverse_lazy('snippets')

    def form_valid(self, form):
        snippet = form.save(commit=False)
        snippet.author = self.request.user
        return super(CreateSnippetView, self).form_valid(form)


class SnippetDeleteView(LoginRequiredMixin, DeleteView):

    model = Snippet
    success_url = reverse_lazy('snippets')

    NOT_SNIPPET_OWNER = _("Sorry you can't delete that snippet because you are not the snippet author.")

    def dispatch(self, request, *args, **kwargs):
        snippet = self.get_object()
        if request.user !=  snippet.author:
            messages.error(self.request, SnippetDeleteView.NOT_SNIPPET_OWNER)
            return redirect('user_snippets', request.user.profile.slug)

        return super(SnippetDeleteView, self).dispatch(request, *args, **kwargs)

class SnippetUpdateView(LoginRequiredMixin, UpdateView):

    model = Snippet 
    template_name = 'snippets/update.html'
    context_object_name = 'snippet'
    form_class = UpdateSnippetForm

    def get_initial(self):
        obj = self.get_object()
        return {'tags': obj.tags.all()}


class MySnippetsView(LoginRequiredMixin, ListView):

    model = Snippet
    context_object_name = 'snippets'
    template_name = 'snippets/my_snippets.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('-created')





