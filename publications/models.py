from django.contrib.auth.models import User
from django.db import models


class Publication():
    abstract = models.TextField(blank=True, default='')
    authors = models.ManyToManyField(User, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

