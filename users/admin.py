__author__ = 'karolinka'

from  users.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user']

admin.site.register(UserProfile, UserProfileAdmin)

