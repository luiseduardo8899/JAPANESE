from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from dictionary.models import Entry 
from dictionary.utils import * #to get random entries, quizes
from userinfo.utils import * #to get user profile and stats
from django.template import loader
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from random import *
from django.core.mail import send_mail

# Search Dictionary View #TODO :define a new index page for dictionary
def index(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('account/login/')

    #method_decorator(login_required) #<<< TODO: Check why decorator did not work
    user = get_user(request) #include here if user not logged in
    stats = get_stats(user)
    latest_noun_list = Entry.objects.order_by('-pub_date')[:50]
    template = loader.get_template('dictionary/search.html')
    context = {
        'user' : user,
        'stats' : stats,
        'latest_noun_list': latest_noun_list,
    }
    return HttpResponse(template.render(context, request))

#View Function : random_quiz(request, word_id):
# Retrieve a random quiz, based on user level
def random_quiz(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('account/login/')

    user = get_user(request)
    stats = get_stats(user)

    #TODO: how to account points in stats ?
    stats.points = stats.points+1
    stats.save()

    list_size = get_list_size(user)

    if list_size > 10: 
        choose = randint(1, 9)
        if choose == 1: #10% chance
            quiz = get_furigana_quiz(user)
            template = loader.get_template('dictionary/random_quiz.html')
        elif choose > 1 and choose < 6: #50% chance
            quiz = get_definition_quiz(user)
            template = loader.get_template('dictionary/random_quiz.html')
        else : #50% chance pronunciation quiz
            quiz = get_pronounce_quiz(user)
            template = loader.get_template('dictionary/pronounce_quiz.html')

        description = quiz['etext']
        kanji = quiz['kanji']
        furigana = quiz['furigana']
        definition1 = quiz['definition1']
        definition2 = quiz['definition2']
        definition3 = quiz['definition3']
        right_index = quiz['right_index']
        entry_stats = quiz['entry_stats']
    else :
        description = "Add some more words to you vocabulary list first"
        right_index = 0 #0 to mean not able to retrieve quiz
        kanji = ""
        furigana = ""
        definition1 = ""
        definition2 = ""
        definition3 = ""
        entry_stats = None

    context = {
        'user' : user,
        'stats' : stats,
        'description': description, #description of the tested item
        'kanji': kanji,
        'furigana': furigana,
        'definition1': definition1,
        'definition2': definition2,
        'definition3': definition3,
        'right_index': right_index,
        'list_size' : list_size,
        'entry_stats': entry_stats,
    }
    return HttpResponse(template.render(context, request))

#View Function : detail(request, word_id):
# View details for a specififc function
# Returns word, furigana, romanji, definitions
def random(request):
    user = get_user(request)
    stats = get_stats(user)

    entry  = get_random_entry()
    entry_stats = get_entry_stats(user, entry , 0) #0, do not new unless user decides to add to list
    title = entry.get_text()
    description = entry.get_definition()
    #display of entry is completely handled by template. Q: Is this faster? as opposed to processing text here..
    return render(request, "dictionary/detail.html", {'entry':entry, 'user':user, 'stats':stats, 'entry_stats':entry_stats, 'title':title, 'description':description})

#View Function : detail(request, word_id):
# View details for a specififc function
# Returns word, furigana, romanji, definitions
def detail(request, word_id):
    user = get_user(request)
    stats = get_stats(user)
    entry  = get_entry_by_id(word_id)
    entry_stats = ""
    #entry_stats = get_entry_stats(user, entry , 0) #0 do not new if does not exist
    title = entry.get_text()
    description = entry.get_definition()
    return render(request, "dictionary/detail.html", {'entry':entry, 'user':user, 'stats':stats, 'entry_stats':entry_stats, 'title':title, 'description':description})

def learn(request, word_id):
    user = get_user(request)
    stats = get_stats(user)
    entry  = get_entry_by_id(word_id)
    entry_stats = get_entry_stats(user, entry , 1) #1 new if does not exist

    return render(request, "dictionary/detail.html", {'entry':entry, 'user':user, 'stats':stats, 'entry_stats': entry_stats})

def send_email(request, email, word_id):
    user = get_user(request)
    stats = get_stats(user)
    entry  = get_entry_by_id(word_id)
    #text = entry.get_text() # get Keb or Reb
    #definition = entry.get_definition() # get First definition
    text = "SABUI"
    definition = " Lame, uninteresting"
    #form title of the email   
    title  = text+': '+definition

    #body : send html text for body # send summary, and link to full entry
    #send email, and remain in detail page
    send_mail(
        title,
        'This is the word entry',
        'japanese@gokokan.com',
        [email],
        fail_silently=False,
    )
    return render(request, "dictionary/detail.html", {'entry':entry})

#from list view, if user hits remove, remove item and refresh list
def remove(request, word_id):
    user = get_user(request)
    stats = get_stats(user)
    ok = remove_entry_stats(user, word_id) #remove from user
    all_entry_stats = get_entry_stats_all(user)

    return render(request, "dictionary/list.html", {'user':user, 'stats':stats, 'all_entry_stats': all_entry_stats})

#TODO: MOVE this really fall under userinfo.views? TODO
def entry_list(request):
    user = get_user(request)
    stats = get_stats(user)
    all_entry_stats = get_entry_stats_all(user)
    return render(request, "dictionary/list.html", {'user':user, 'stats':stats, 'all_entry_stats': all_entry_stats})
