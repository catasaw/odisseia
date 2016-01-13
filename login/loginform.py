from django import forms
from magazine.models import Contributor
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class LoginForm(forms.Form):
 
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'class' : 'form-control', 'placeholder': _('E-mail'),}), label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'min_length': 8, 'max_length': 30, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Password'), }), label=_("Password"))