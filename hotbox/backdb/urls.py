from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView, DetailView
#from signup.views import *
from . import views
from .models import Forums


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/', views.sec_reg, name='sec_reg'),
    url(r'^profile/', views.prof, name='prof'),
    url(r'^forum/', ListView.as_view(queryset=Forums.objects.all().order_by("-rating_pop")[:60], template_name="backdb/forum.html")),
    url(r'^subforum/', views.subforum, name='subforum'),
#    url(r'^forum/pop/', views.forum_pop, name='forum_pop'),
#    url(r'^forum/tag/', views.forum_tag, name='forum_tag'),
#    url(r'^subforum/pr/', views.subforum_pr, name='subforum_pr'),
#    url(r'^subforum/tag/', views.subforum_tag, name='subforum_tag'),
#    url(r'^subforum/pop/', views.subforum_pop, name='subforum_pop'),
    url(r'^thread/', views.thread, name='thread'),
    url(r'^subscription/', views.subs, name='subs'),


]
