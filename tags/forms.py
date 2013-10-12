from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import ApprovedTag


class CreateTagForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateTagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'submit'))

    class Meta:
        model = ApprovedTag
        fields = ('name',)