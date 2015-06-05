import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from publications.models import Publication
from django.core.urlresolvers import reverse


def logo_upload_path(instance, filename):
    return 'img/ngo/' + uuid4().hex + os.path.splitext(filename)[1]


class Organization(models.Model):
    description = models.TextField(blank=True, default="")
    creator = models.ForeignKey(User, related_name=("created_organizations"))
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name="organizations", blank=True, null=True)
   # publications = models.ManyToManyField(Publication, related_name="mentors", blank=True, null=True)
    logo = models.ImageField(upload_to=logo_upload_path, default='img/ngo/default.jpg') #TODO

    def get_absolute_url(self):
        return reverse('organizations:detail', kwargs={'slug': self.slug, })

    def has_access(self, user):
        if user.is_superuser:
            return True
        return user == self.creator

    def __str__(self):
        return self.name



