# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(null=True, blank=True)),
                ('birth_date', models.CharField(max_length=20, null=True, blank=True)),
                ('clean_username', models.SlugField(null=True, blank=True)),
                ('website', models.URLField(max_length=255, null=True, blank=True)),
                ('avatar', models.ImageField(default=b'img/avatars/anonymous.jpg', upload_to=b'img/avatars/')),
                ('thumbnail', models.ImageField(default=b'img/avatars/30x30_anonymous.jpg', upload_to=b'img/avatars/')),
                ('image', models.ImageField(default=b'img/backgrounds/background.jpg', upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='logindata',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
