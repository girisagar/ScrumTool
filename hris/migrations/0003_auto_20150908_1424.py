# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0002_auto_20150908_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
