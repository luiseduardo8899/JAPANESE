from django.conf.urls import url
from . import views

app_name = 'teacher'
urlpatterns = [
    # ex: /teacher/
    #url(r'^$', userinfo.views.profile, name='profile'), #teacher views profile
    #url(r'view', userinfo.views.profile, name='profile'), #teacher view profile
    url(r'create_powerpoint', views.create_powerpoint, name='create_powerpoint'), #create svg images of vocabulary entrie
    url(r'create_images', views.create_images, name='create_images'), #create svg images of vocabulary entrie
    url(r'upload_dictionary', views.upload_dictionary, name='upload_dictionary'), #update profile
    url(r'update_dictionary', views.update_dictionary, name='update_dictionary'), #update profile
    url(r'upload_vocab', views.upload_vocab, name='upload_vocab'), #update profile
    url(r'update_vocab', views.update_vocab, name='update_vocab'), #update profile
    url(r'upload_grammar', views.upload_grammar, name='upload_grammar'), #update profile
    url(r'update_grammar', views.update_grammar, name='update_grammar'), #update profile
    url(r'upload_kanji', views.upload_kanji, name='upload_kanji'), #update profile
    url(r'update_kanji', views.update_kanji, name='update_kanji'), #update profile
    url(r'successful_upload', views.successful_upload, name='successful_upload'), #update profile
    url(r'create_videos', views.create_videos, name='create_videos'), #create video entries for Vocabulary and Grammar entries
]
