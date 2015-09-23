# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0011_worklog_log_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worklog',
            name='log_type',
        ),
    ]
