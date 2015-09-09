# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0005_auto_20150908_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('icon_class', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/employee-image', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ForeignKey(blank=True, to='hris.Role', null=True),
        ),
    ]
