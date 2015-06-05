# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import organizations.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('logo', models.ImageField(default=b'img/ngo/default.jpg', upload_to=organizations.models.logo_upload_path)),
                ('creator', models.ForeignKey(related_name='created_organizations', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='organizations', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
