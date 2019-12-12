from django import forms
from codes.models import Code


class CodeForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Code model. """
        model = Code
        fields = ("title", "content", "author")
