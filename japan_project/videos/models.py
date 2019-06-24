from django.db import models
from django.utils import timezone
import datetime

#Integer definition of JLPT_N levels
JLPT_N5 = 5
JLPT_N4 = 4
JLPT_N3 = 3
JLPT_N2 = 2
JLPT_N1 = 1
JLPT_N1P = 0 #More advanced than material covered in JLPT_N1
JLPT_LEVELS = (
    (JLPT_N5, "JLPT_N5"),
    (JLPT_N4, "JLPT_N4"),
    (JLPT_N3, "JLPT_N3"),
    (JLPT_N2, "JLPT_N2"),
    (JLPT_N1, "JLPT_N1"),
    (JLPT_N1P, "JLPT_N1P")
)

#Class Video
#Class which defines a Video URL to a GrammarEntry or a Verb Entry or Vocabulary Entry
class Video(models.Model):
    url = models.CharField(max_length=140)  #Path to the video entry, may be under /media/ or in url http://youtube.com format
                                            #any checks to this field will be made when creating the GrammarVideo entry
    title = models.CharField(max_length=140)  #Title for the video
    #TODO: teacher = models.OneToOneField(Teacher)  #Title for the video
    #TODO: teacher should be a user account with Teacher privileges...
    description = models.CharField(max_length=500)  #Description of video entry
    likes  = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    jlptlevel = models.IntegerField(choices=JLPT_LEVELS, default=5)
    level = models.IntegerField(default=0) # Total of 1-1024

    def __str__(self):
        return "Video#%s" % self.title  

    class Meta:
        ordering = ['pub_date']

#TODO: Move to ActivityStats app?
#class VideoStats(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    video = models.OneToOneField(Entry)#TODO: Change to ManytoMany as many users will have statentries to the same entry
#    times_viewed  = models.IntegerField(default=0)
#    liked  = models.BooleanField(default=False) #whether user liked this video or not
#    view_date = models.DateTimeField('last date viewed') #last date user viewed this video 
#
#    def __str__(self):
#        return "VideoStats#%s " % self.pk , "for Video#%s" % video.pk
