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

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        context['numbers'] = [1,2,3,4,5,6,7,8,9,10]
        return context

    def get_queryset(self):
        return self.model.objects.filter(approved=True)


class CreateTagView(LoginRequiredMixin, CreateView):

    template_name = 'tags/create.html'
    model = ApprovedTag
    form_class = CreateTagForm

    TAG_CREATED = _('Tag successfully submitted and waiting for the approval of the site admin.')

    def form_valid(self, form):
        tag = form.save(commit=False)
        tag.author = self.request.user
        messages.success(self.request, CreateTagView.TAG_CREATED)
        return super(CreateTagView, self).form_valid(form)

    def get_success_url(self):
        return reverse('tag_create', args=(self.request.user.profile.slug,))


