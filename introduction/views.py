from django.shortcuts import render, redirect
from magazine.models import Introduction, Introduction_Translation,\
    Language_Contributor
from django.http.response import HttpResponse, HttpResponseRedirect

def introduction_view(request, issue_id, introduction_id):
    context = {}
    context['issue_id'] = issue_id
    context['introduction'] = issue_id
    
    introduction_translation = Introduction_Translation.objects.filter(introduction_id = introduction_id).filter(language_to__iso1_code = request.LANGUAGE_CODE).first()
    if introduction_translation:
        return render(request, 'introduction/introduction_view.html', {'introduction': introduction_translation})
    
    # If there is no translation, display original
    try:
        introduction= Introduction.objects.get(id=introduction_id)
        return render(request, 'introduction/introduction_view.html', {'introduction': introduction}) 
    except Introduction.DoesNotExist:
        return redirect('/') 
            
