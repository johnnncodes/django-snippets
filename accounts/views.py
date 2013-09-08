from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import (
    login,
    logout
)
from django.utils.translation import ugettext as _
from django.views.generic.edit import (
    BaseFormView
)

from accounts.forms import LoginForm


class LoginView(BaseFormView):

    form_class = LoginForm

    INVALID_CREDENTIALS = _('Invalid username and password')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, LoginView.INVALID_CREDENTIALS)
        return redirect('home')

    def get_success_url(self):
        return reverse('snippets');


