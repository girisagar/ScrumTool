# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0015_auto_20150922_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='work_done',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
