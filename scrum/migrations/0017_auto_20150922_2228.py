# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0016_auto_20150922_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasebacklog',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
