from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect 
from django.core.context_processors import csrf
from magazine.models import User,User_Language,Language
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from login.registrationform import RegistrationForm
from datetime import datetime

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            status= User.UNCONFIRMED,
            )
            return HttpResponseRedirect('/signup/success/')     
    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    languages = Language.objects.all().order_by('name')
    token['languages'] = languages    
    return render_to_response('login/signup.html', token)

    
    
def register_success(request):
    
    return render_to_response('login/login_successful.html')


def login(self, request):
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