from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.core.context_processors import csrf
from magazine.models import User,User_Language,Language
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

def signup(request):
    languages = Language.objects.all().order_by('name')
    return render(request, 'login/signup.html', {'languages': languages})

@csrf_protect
def register(self, request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')     
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('login/signup.html', token)

    
    
def registration_complete(self, request):
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