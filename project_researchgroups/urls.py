from django.conf.urls import patterns, include, url
from django.contrib import admin
from project_researchgroups import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'researchdoor_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name="index"),

)

