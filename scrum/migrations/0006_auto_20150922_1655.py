# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0005_auto_20150922_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='work_done',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
