from django import forms
from .models import Content

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=Content.objects.all(),label='Select a chai varity')
    