# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0014_auto_20150922_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='user_story',
            field=models.ForeignKey(related_name='worklog_user_story', to='scrum.UserStory'),
        ),
    ]
