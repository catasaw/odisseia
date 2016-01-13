from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect 
from django.core.context_processors import csrf
from magazine.models import Contributor, Contributor_Language,Language
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from login.registrationform import RegistrationForm

@csrf_protect
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard/')      
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_contributor = Contributor.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            status=Contributor.UNCONFIRMED
            )
            new_contributor.save()
            user=authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            login(request,user)
            return HttpResponseRedirect('/signup/success/')     
    else:
        form = RegistrationForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form
    languages = Language.objects.all().order_by('name')
    context['languages'] = languages    
    return render_to_response('login/signup.html', context)

    
    
def register_success(request):
    
    return render_to_response('login/login_successful.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    languages = Language.objects.all().order_by('name')
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'magazine/dashboard.html')
        else:
            # Return a 'disabled account' error message
            return render(request, 'magazine/signup.html', {'languages': languages})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'magazine/signup.html', {'languages': languages})