# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0010_auto_20150922_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='worklog',
            name='log_type',
            field=models.CharField(default=None, max_length=15, null=True, blank=True, choices=[(b'test', b'Test'), (b'development', b'Development')]),
        ),
    ]
