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
def get_video(video_id):
    #try to get the user profile TODO: should we try getting multiple times? 
    try:
        video = Videos.objects.get(pk = video_id)
    except Videos.DoesNotExist: #if does not exist create a new one
        video = Null
    return video

#Get all videos based on a specific level
def get_video_list(video_level):
    video_list = Videos.objects.get(level = video_level)
    return video_list
