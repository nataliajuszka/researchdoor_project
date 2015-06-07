from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from organizations.models import Organization


class News(models.Model):
    title = models.CharField(max_length=50, default="")
    content = models.TextField(blank=True, default="")
    author = models.ForeignKey(User, related_name="created_news")
    organizations = models.ManyToManyField(Organization, related_name="organization_news")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name