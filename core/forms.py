from django import forms
from .models import Double


class DoubleForm(forms.ModelForm):
    class Meta:
        model = Double
        fields = ['name', 'value', 'double_value', 'date']
        widgets = {'double_value': forms.HiddenInput(), 'date': forms.HiddenInput()}

