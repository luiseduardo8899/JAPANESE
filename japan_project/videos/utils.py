from userinfo.models import Profile, Statistics
from videos.models import Video
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from random import *

#Get User Profile Information
def get_video(video_id):
    #try to get the user profile TODO: should we try getting multiple times? 
    try:
        video = Video.objects.get(pk = video_id)
    except Video.DoesNotExist: #if does not exist return None
        video = None
    return video

#Get all videos based on a specific level
def get_video_list(video_level):
    try:
        video_list = Video.objects.all().filter(jlptlevel = video_level)
    except Video.DoesNotExist: #if does not exist return None
        video_list = None
    return video_list
