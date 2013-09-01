from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
    
from braces.views import LoginRequiredMixin

from snippets.models import Snippet
from snippets.forms import CreateSnippetForm


class SnippetsView(LoginRequiredMixin, ListView):
   
    template_name = 'snippets/snippets.html'
    model = Snippet
    context_object_name = 'snippets'


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


class SnippetUpdateView(LoginRequiredMixin, UpdateView):

    model = Snippet 
    template_name = 'snippets/update.html'
    context_object_name = 'snippet'
    form_class = CreateSnippetForm


class MySnippetsView(LoginRequiredMixin, ListView):

    model = Snippet
    context_object_name = 'snippets'
    template_name = 'snippets/my_snippets.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)





