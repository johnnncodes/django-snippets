from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from snippets.models import Snippet


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('login')
        self.helper.add_input(Submit('submit', 'Login'))


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

