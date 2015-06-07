# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150605_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'static/static_dirs/static_root'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=b'static/static_dirs/img'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='thumbnail',
            field=models.ImageField(upload_to=b'static/static_dirs/img'),
            preserve_default=True,
        ),
    ]
