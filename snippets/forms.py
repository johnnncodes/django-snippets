from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from snippets.models import Snippet


class CreateSnippetForm(forms.ModelForm):

    submit_label = None
    DEFAULT_SUBMIT_LABEL = 'Submit'

    def __init__(self, *args, **kwargs):
        super(CreateSnippetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', self.get_submit_label()))

    class Meta:
        model = Snippet
        fields = ('title', 'body')

    def get_submit_label(self):
        if not self.submit_label:
            return self.DEFAULT_SUBMIT_LABEL

        return self.submit_label


class UpdateSnippetForm(CreateSnippetForm):

    def __init__(self, *args, **kwargs):
        self.submit_label = 'Update'
        super(UpdateSnippetForm, self).__init__(*args, **kwargs)
        