from django import forms
from magazine.models import Comment
from django.utils.translation import ugettext_lazy as _
 
class CommentForm(forms.Form):
    
    content = forms.CharField(widget=forms.Textarea(attrs={'required': True, 'min_length': 8, 'max_length': 250, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Write your comment here ...'), }),)
    