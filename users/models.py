from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    description = models.TextField(blank=True, null=True)
    birth_date = models.CharField(max_length=20, blank=True, null=True)
    clean_username = models.SlugField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(
        upload_to = "img/avatars/",
        default = 'img/avatars/anonymous.jpg',
      #  storage = OverwriteStorage()
    )
    thumbnail = models.ImageField(
        upload_to = "img/avatars/",
        default = 'img/avatars/30x30_anonymous.jpg',
        #storage = OverwriteStorage()
    )
    image = models.ImageField(
       # upload_to = get_upload_path,
        default = 'img/backgrounds/background.jpg'
    )


class LoginData(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date',]
