# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0017_auto_20150922_2228'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='releasebacklog',
            unique_together=set([('product_backlog', 'name')]),
        ),
    ]
