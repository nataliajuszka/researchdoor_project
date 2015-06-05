__author__ = 'magdalenapeksa'
from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^profile/(?P<profile_id>\d+)/$', 'users.views.profile'),
                       url(r'^update_profile/$', 'users.views.update_profile'),
                       url(r'^send_update_profile/$', 'users.views.send_update_profile'),

                      )