from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from opinion.opinionform import OpinionForm
from django.http.response import HttpResponseRedirect
from django.template.context_processors import csrf

@login_required
@csrf_protect
def opinions_view(request, issue_id):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/dashboard/')     
    else:
        form = OpinionForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    return render(request, 'opinion/opinion_view.html', context)
