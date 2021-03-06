from django import forms
from magazine.models import Contributor
from django.contrib.auth.models import User
from magazine.models import Language
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'class' : 'form-control', 'placeholder': _('E-mail'),}), label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'min_length': 8, 'max_length': 30, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Password'), }), label=_("Password"))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'min_length': 8, 'max_length': 30, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Repeat Password'), }), label=_("Password (again)"))
    languages_from = forms.ModelMultipleChoiceField(queryset= Language.objects.order_by('name').all())
    languages_to = forms.ModelMultipleChoiceField(queryset = Language.objects.order_by('name').all())
 
    def clean_email(self):
        try:
            user = Contributor.objects.get(email__iexact=self.cleaned_data['email'])
        except Contributor.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))
    
 
    def clean(self):
        if 'password' in self.cleaned_data and 'password_repeat' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data