# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0007_auto_20150909_0552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='roles',
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(to='hris.Role', null=True, blank=True),
        ),
    ]
