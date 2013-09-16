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
from .models import ApprovedTag
from .forms import CreateTagForm


class TagsView(LoginRequiredMixin, ListView):
   
    template_name = 'tags/tags.html'
    model = ApprovedTag
    context_object_name = 'tags'

    def get_queryset(self):
        return self.model.objects.filter(approved=True)


class CreateTagView(LoginRequiredMixin, CreateView):

    template_name = 'tags/create.html'
    model = ApprovedTag
    form_class = CreateTagForm
    success_url = reverse_lazy('tags')

    def form_valid(self, form):
        tag = form.save(commit=False)
        tag.author = self.request.user
        return super(CreateTagView, self).form_valid(form)




