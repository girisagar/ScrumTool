# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0019_auto_20150922_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbacklog',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
