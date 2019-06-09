from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    # ex: /videos/
    url(r'(?P<video_id>[0-9]+)/watch$', views.watch_video, name='watch_video'),
    url(r'(?P<video_level>[0-9]+)/list$', views.list_videos, name='list_videos'),
]
