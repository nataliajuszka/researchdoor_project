__author__ = 'magdalenapeksa'
from django.conf.urls import *
import views

urlpatterns = patterns('',
                       url(r"^login/$", views.UserLoginView.as_view(), name='login'),
                       url(r"^registration/$", views.RegistrationView.as_view(), name='registration'),
                       #url(r"^account/(?P<username>[0-9a-zA-Z_]{4,})$", AccountInfoView.as_view(), name="account_info"),

                        url(r"^logout/$", views.logout_user, name="logout"),
                       #url(r'^profile/(?P<profile_id>\d+)/$', 'users.views.profile'),
                       #url(r'^update_profile/$', 'users.views.update_profile'),
                       #url(r'^send_update_profile/$', 'users.views.send_update_profile'),
)