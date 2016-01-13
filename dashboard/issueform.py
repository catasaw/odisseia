from django import forms
from magazine.models import Issue
from django.utils.translation import ugettext_lazy as _
 
class IssueForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'min_length': 8, 'max_length': 250, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Write title here'), }),)
    