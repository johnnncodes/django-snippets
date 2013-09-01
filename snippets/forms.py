from django import forms

from snippets.models import Snippet

class CreateSnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('title', 'body')


