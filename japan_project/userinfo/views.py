from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from userinfo.models import Profile
from userinfo.utils import *
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.conf.urls.static import static #for profile picture?
from django.shortcuts import redirect 
from .forms import ProfileForm
import json
from django.http import JsonResponse

#Create Profile
def create_profile(request):
    user = get_user(request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            p = Profile()
            p.user = user
            p.gender = form.cleaned_data['gender']
            p.gender_other = form.cleaned_data['gender_other']
            p.year_ob = form.cleaned_data['year_ob']
            p.month_ob = form.cleaned_data['month_ob']
            p.day_ob = form.cleaned_data['day_ob']
            p.country = form.cleaned_data['country']
            p.location = form.cleaned_data['location']
            p.language = form.cleaned_data['language']
            p.intro = form.cleaned_data['intro']
            p.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/userinfo/view')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'userinfo/create_profile.html', {'form': form})

# Profile View
def profile(request):
    user = get_user(request)
    if user.is_anonymous : 
        return redirect("/account/login")
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
        #TODO: age = request.POST['age']
        #TODO: language = request.POST['language']
        #TODO : check for errors in inputs ? Use Django FORMS?
        profile.intro = intro
        profile.gender = gender
        profile.country = country
        profile.location = location
        #TODO profile.language = language
        #TODO profile.age = age
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
