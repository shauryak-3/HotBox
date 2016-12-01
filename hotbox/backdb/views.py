from django.shortcuts import render
#from django.views.generic import ListView, DetailView
#from .models import *

# Create your views here.
def home(request) :
	return render(request, 'backdb/home.html')

def sec_reg(request) :
	return render(request, 'backdb/register.html')

def prof(request) :
	return render(request, 'backdb/profile.html')
"""
def forum_pop(request) :
	return render(request, 'backdb/popforum.html', {content : ['first string' , 'second string']})

def forum_tag(request) :
	return render(request, 'backdb/tagforum.html')

def subforum_pr(request) :
	return render(request, 'backdb/prsubforum.html')

def subforum_pop(request) :
	return render(request, 'backdb/popsubforum.html')

def subforum_tag(request) :
	return render(request, 'backdb/tagsubforum.html')
"""
def thread(request) :
	return render(request, 'backdb/thread.html')

def subs(request) :
	return render(request, 'backdb/subs.html')

def forum(request) :
	name = request.get('')
	return render(request, 'backdb/forum.html')

def threadlist(request) :
	return render(request, 'backdb/threadlist.html')

def subforum(request) :
#	username = request.get('username')
	return render(request, 'backdb/subforum.html')

#Bhardwaj comment
