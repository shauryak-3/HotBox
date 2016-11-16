from django.shortcuts import render

# Create your views here.

from signup.forms import *
from .models import *
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
#from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
#@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            handle=form.cleaned_data['handle'],
            passwd=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'signup/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'signup/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
#@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
