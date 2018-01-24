from django.shortcuts import render
from dictionary.utils import * #to get video and video stats
from videos.utils import * #to get videos
from userinfo.utils import * #to get user profile and stats
from videos.models import Video

# Watch Function : watch(request, word_id):
# Watch a video lesson
def watch_video(request, video_id):
    user = get_user(request)
    stats = get_stats(user)
    video  = get_video(video_id)
    #video_stats = get_video_stats(user, video , 1) #1 new if it does not exist
    #return render(request, "videos/watch.html", {'video':video, 'user':user, 'stats':stats, 'video_stats':video_stats })
    return render(request, "videos/watch.html", {'video':video, 'user':user, 'stats':stats })


# List Function : list(request, level):
# List all videos for a specific level, sublevel
def list_videos(request, video_level):
    user = get_user(request)
    stats = get_stats(user)
    video_list  = get_video_list(video_level)
    #video_stats = get_video_stats(user, video , 1) #1 new if it does not exist
    #return render(request, "videos/watch.html", {'video':video, 'user':user, 'stats':stats, 'video_stats':video_stats })
    return render(request, "videos/watch.html", {'video_list':video_list, 'user':user, 'stats':stats })
