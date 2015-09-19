# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='release_backlog',
            field=models.ForeignKey(default=None, to='scrum.ReleaseBacklog'),
        ),
    ]
