# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0004_auto_20150921_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='work_remaining',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
