from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from random import *

# Search Dictionary View #TODO :define a new index page for dictionary
def hello(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('account/login/')

    #method_decorator(login_required) #<<< TODO: Check why decorator did not work
    #user = get_user(request) #include here if user not logged in
    #stats = get_stats(user)
    #latest_noun_list = Entry.objects.order_by('-pub_date')[:50]
    template = loader.get_template('account/hello.html')
    #context = {
    #    'user' : user,
    #    'stats' : stats,
    #    'latest_noun_list': latest_noun_list,
    #}
    context = {'user':'Luis'}
    return HttpResponse(template.render(context, request))

# Search Dictionary View #TODO :define a new index page for dictionary
def byebye(request):
    # Redirect to Homepage if user is not signed in

    #method_decorator(login_required) #<<< TODO: Check why decorator did not work
    #user = get_user(request) #include here if user not logged in
    #stats = get_stats(user)
    #latest_noun_list = Entry.objects.order_by('-pub_date')[:50]
    template = loader.get_template('account/byebye.html')
    #context = {
    #    'user' : user,
    #    'stats' : stats,
    #    'latest_noun_list': latest_noun_list,
    #}
    context = {'user':'Luis'}
    return HttpResponse(template.render(context, request))

# Welcome page
def welcome(request):
    template = loader.get_template('account/welcome.html')
    context = {'user':'Luis'}
    return HttpResponse(template.render(context, request))
