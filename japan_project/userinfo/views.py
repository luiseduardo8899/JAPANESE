from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from userinfo.models import Profile
from userinfo.utils import *
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.conf.urls.static import static #for profile picture?
import json
from django.http import JsonResponse

# Profile View
def profile(request):
    user = get_user(request)
    profile = get_profile(user)
    template = loader.get_template('userinfo/profile.html')
    context = {
        'user': user,
        'profile': profile,
    }
    return HttpResponse(template.render(context, request))

# Profile Update
def update(request):
    user = get_user(request)
    profile = get_profile(user)

	#try and retrieve Form inputs..
    try:
        intro = request.POST['intro']
    except ValueError: 
        # Redisplay the profile form.
        return render(request, 'userinfo/profile.html', {
            'user': user,
            'profile': profile,
            'error_message': "Please enter a profile introduction",
        })
    else:
        intro = request.POST['intro']
        gender = request.POST['gender']
        country = request.POST['country']
        location = request.POST['location']
        #TODO : check for errors in inputs ? Use Django FORMS?
        profile.intro = intro
        profile.gender = gender
        profile.country = country
        profile.location = location
        profile.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('userinfo:profile'))

def statistics(request):
    user = get_user(request)
    stats = get_stats(user)
    #TODO all_entry_stats = get_entry_stats_all(user)
    template = loader.get_template('userinfo/statistics.html')
    context = {
        'user': user,
        'stats': stats,
        #TODO: 'entry_stats': all_entry_stats,
    }
    return HttpResponse(template.render(context, request))
