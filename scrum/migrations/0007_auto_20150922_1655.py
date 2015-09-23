# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0006_auto_20150922_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='created_by',
            field=models.ForeignKey(related_name='worklog_created_by', blank=True, to='hris.Employee', null=True),
        ),
    ]
