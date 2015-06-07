__author__ = 'karolinka'
from django.conf.urls import *
import views

urlpatterns = patterns('',
                       url(r"^login/$", views.UserLoginView.as_view(), name='login'),
                       url(r"^registration/$", views.RegistrationView.as_view(), name='registration'),
                       url(r"^logout/$", views.logout_user, name="logout"),
                       url(r'^profile/$', 'users.views.profile', name='profile'),
                       #url(r'^update_profile/(?P<profile_id>\d+)/$', 'users.views.update_profile', name='update_profile'),
                       url(r'^update_profile/$', 'users.views.update_profile', name='update_profile'),
                       url(r'^send_update_profile/$', 'users.views.send_update_profile'),

                      )
