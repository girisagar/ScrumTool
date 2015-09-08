# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0003_auto_20150908_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='h', upload_to=b'/media/employee-image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zip',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
