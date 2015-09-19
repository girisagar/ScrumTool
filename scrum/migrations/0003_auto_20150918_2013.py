# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0002_auto_20150918_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='release_backlog',
            field=models.ForeignKey(to='scrum.ReleaseBacklog'),
        ),
    ]
