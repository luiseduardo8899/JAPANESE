from django.conf.urls import url
from . import views

app_name = 'teacher'
urlpatterns = [
    # ex: /teacher/
    #url(r'^$', userinfo.views.profile, name='profile'), #teacher views profile
    #url(r'view', userinfo.views.profile, name='profile'), #teacher view profile
    url(r'create_images', views.create_images, name='create_images'), #create svg images of vocabulary entrie
    url(r'upload_vocab', views.upload_vocab, name='upload_vocab'), #update profile
    url(r'update_vocab', views.update_vocab, name='update_vocab'), #update profile
    url(r'upload_grammar', views.upload_grammar, name='upload_grammar'), #update profile
    url(r'update_grammar', views.update_grammar, name='update_grammar'), #update profile
    url(r'successful_upload', views.successful_upload, name='successful_upload'), #update profile
]
