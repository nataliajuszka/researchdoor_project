# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'img/avatars/anonymous.jpg', upload_to=b'img/avatars/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=b'img/backgrounds/background.jpg', upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='thumbnail',
            field=models.ImageField(default=b'img/avatars/30x30_anonymous.jpg', upload_to=b'img/avatars/'),
            preserve_default=True,
        ),
    ]
