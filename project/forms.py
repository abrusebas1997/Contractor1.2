from django import forms
from project.models import Code


class CodeForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Code model. """
        model = Code
        fields = ("title", "content", "author")
