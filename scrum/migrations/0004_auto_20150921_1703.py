# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0003_auto_20150918_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='sprint_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='sprint_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
