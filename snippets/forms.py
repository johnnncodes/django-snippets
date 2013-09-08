from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from snippets.models import Snippet

from taggit.models import Tag

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
        fields = ('title', 'body', 'tags')

    def get_submit_label(self):
        if not self.submit_label:
            return self.DEFAULT_SUBMIT_LABEL

        return self.submit_label

    def clean_tags(self):
        available_tags = Tag.objects.all().values_list('name', flat=True)
        chosen_tags = self.cleaned_data['tags'] 

        for tag in chosen_tags:
            if tag not in available_tags:
                raise forms.ValidationError(_('The tag you chose is not avaiable.'))

        return chosen_tags


class UpdateSnippetForm(CreateSnippetForm):

    def __init__(self, *args, **kwargs):
        self.submit_label = 'Update'
        super(UpdateSnippetForm, self).__init__(*args, **kwargs)
        