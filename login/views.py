from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect 
from django.core.context_processors import csrf
from magazine.models import Contributor,Language, Language_Contributor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from login.registrationform import RegistrationForm
from django.contrib.auth import logout
from login.loginform import LoginForm
import sendgrid
from django.conf import settings

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


            for language_from in form.cleaned_data['languages_from']:
                new_contributor_language = Language_Contributor(
                contributor=new_contributor,
                language=language_from,
                type=Language_Contributor.FIRST_LANGUAGE
                )
                new_contributor_language.save()
            
            
            for language_to in form.cleaned_data['languages_to']:
                new_contributor_language = Language_Contributor(
                contributor=new_contributor,
                language=language_to,
                type=Language_Contributor.SECOND_LANGUAGE
                )
                new_contributor_language.save()
                
           
            user=authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            login(request,user)
            
            sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)
            message = sendgrid.Mail(to=form.cleaned_data['email'], subject='Welcome to Odisseia!', from_email='odisseia@posteo.net')
            message.add_filter('templates', 
                   { "enable", "template_id"}, 
                   { 1, settings.EMAIL_TEMPLATE}
                   )
            status, msg = sg.send(message)
            print(status, msg)
        
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

@csrf_protect
def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard/')      
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect('/dashboard/')  
                else:
                    # Return a 'disabled account' error message
                    return render(request, 'login/disabled_account.html')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/accounts/signup/')     
    
    else:
        form = LoginForm()
    context = {}
    context.update(csrf(request))
    context['form'] = form   
    return render_to_response('login/login.html', context)
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')     