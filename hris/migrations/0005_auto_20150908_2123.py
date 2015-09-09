# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0004_auto_20150908_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/media/employee-image', blank=True),
        ),
    ]
