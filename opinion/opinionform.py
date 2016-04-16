from django import forms
from magazine.models import Opinion, Language
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
 
class OpinionForm(forms.Form):
    
    content = forms.CharField(widget=TinyMCE(attrs={'id': 'opinion_field', 'required': True, 'min_length': 250, 'class' : 'form-control', 'render_value': False, 'placeholder': _('Write your comment here ...'), } ),)
    language = forms.ModelChoiceField(queryset = Language.objects.order_by('name').all())
    
    def clean(self):
        if len(self.cleaned_data['content']) < 250 :
            raise forms.ValidationError(_("Opinion must be minimum 250 char"))
        return self.cleaned_data