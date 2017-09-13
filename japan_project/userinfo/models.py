from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

#Class profile: 
class Profile(models.Model):  
    user = models.OneToOneField(User)
    country = models.CharField(max_length=140) #TODO: Use a dropdown to select country
    location = models.CharField(max_length=140) #TODO: Use a dropdown to select country
    gender = models.CharField(max_length=60) #Man, Woman, More-> user enters his own 
    intro = models.CharField(max_length=250)  
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

#Class: Statistics
class Statistics(models.Model): #TODO: rename PointStats
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)    #Total points accumulated
    level = models.IntegerField(default=0)     #current level (1-4096) : 4K levels must match LevelStats.level.level.

    def __str__(self):
        return 'Statistics for user: %s' % self.user.username

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

    def add_point(self):
        self.points = self.points + 1
        self.save()
        return self.points

    def add_points(self, n):
        if int(n) > 10: #limit tasks to 10 points, avoid errors
            n = 10
        self.points = self.points + int(n)
        self.save()
        return self.points

    def get_points(self):
        return self.points

    def get_points(text):
        self.notes = text
        self.save()
        return self.notes
