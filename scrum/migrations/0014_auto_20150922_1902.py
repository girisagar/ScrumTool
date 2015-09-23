# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0013_worklog_log_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='worklog',
            unique_together=set([('date', 'employee', 'log_type', 'user_story')]),
        ),
    ]
