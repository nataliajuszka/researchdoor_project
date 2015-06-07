from django.contrib.auth.models import User
from django.db import models
from organizations.models import Organization

from users.models import UserProfile

__author__ = 'koala'



class Entry(models.Model):
    title = models.CharField(max_length=40)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    date = models.DateField(blank=True)
    person = models.ForeignKey(User, blank=True, null=True)
    is_weekly=models.BooleanField(blank=True)
   # organization=models.ForeignKey(Organization,blank=True)

    def __unicode__(self):
        return unicode(self.person.profile.avatar) + u" - " + self.title

    class Meta:
        ordering = ['start_time']
