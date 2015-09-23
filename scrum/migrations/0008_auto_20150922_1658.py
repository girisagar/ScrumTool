# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0007_auto_20150922_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='created_by',
            field=models.ForeignKey(related_name='worklog_created_by', default=1, to='hris.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worklog',
            name='work_done',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worklog',
            name='work_remaining',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
