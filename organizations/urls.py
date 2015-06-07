from django.conf.urls import *
import views

urlpatterns = patterns('',
                       url(r"^create_organization/$", views.CreateOrganizationView.as_view(), name='create_organization'),
)