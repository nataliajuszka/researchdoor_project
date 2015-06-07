from django.db import models
from news.models import News
from django.contrib.auth.models import User
from datetime import datetime


class Comment(models.Model):
    text = models.CharField(max_length=100)
    news = models.ForeignKey(News, related_name='comments_on_news')
    author = models.ForeignKey(User, related_name='created_comments')
    timestamp = models.DateTimeField(default=datetime.now, auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name
