from userinfo.models import Profile, Statistics
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from random import *

#Default routine to check user exists and login
def get_user(request):
    try:
        user = request.user
    except User.DoesNotExist:
        raise Http404("Gomenazai~~~ USER  does not exist")
    if user.is_anonymous :
        print("User is ANONYMOUS")
    return user

#Get User Profile Information
def get_profile(puser):
    #try to get the user profile TODO: should we try getting multiple times? 
    try:
        profile = Profile.objects.get(user = puser)
    except Profile.DoesNotExist: #if does not exist create a new one
        profile = Profile(user = puser)
        profile.country = ""
        profile.location = ""
        profile.gender = "Male"
        profile.introduction = ""
        profile.age = 18
        profile.save()
    return profile

#Get baseline statistics for this user
def get_stats(puser):
    #try to get the user profile TODO: should we try getting multiple times? 
    if puser.is_anonymous :
        stats = None # return empty object
    else: 
        try:
            stats = Statistics.objects.get(user = puser)
        except Statistics.DoesNotExist: #if does not exist create a new one
            stats = Statistics(user = puser)
            stats.points = 1
            stats.level=1
            stats.save()
