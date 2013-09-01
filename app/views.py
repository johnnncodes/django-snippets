from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm
)
from django.utils.translation import ugettext as _
from django.views.generic import (
    CreateView
)


class RedirectAuthenticated(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('snippets')
        return super(RedirectAuthenticated, self).dispatch(
            request, *args, **kwargs)


class HomeView(RedirectAuthenticated, CreateView):

    template_name = 'app/home.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    REGISTRATION_SUCCESSFUL = _('Successfully registered!')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

    def form_valid(self, form):
        messages.success(self.request, HomeView.REGISTRATION_SUCCESSFUL)
        return super(HomeView, self).form_valid(form)