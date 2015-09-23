# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0018_auto_20150922_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='name',
            field=models.CharField(help_text=b'Sprint name should be in order like Sprint-1, Sprint-2, and so on', max_length=50),
        ),
    ]
