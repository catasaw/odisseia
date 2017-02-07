from django import forms
from magazine.models import Introduction, Language
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget
 
class OpinionForm(forms.Form):
    
    content = forms.CharField(widget=CKEditorWidget(attrs={'id': 'opinion_field', } ),)
    language = forms.ModelChoiceField(queryset = Language.objects.order_by('name').all())
    
    def clean(self):
        if len(self.cleaned_data['content']) < 250 :
            raise forms.ValidationError(_("Opinion must be minimum 250 char"))
        return self.cleaned_data