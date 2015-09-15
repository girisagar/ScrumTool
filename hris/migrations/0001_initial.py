# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'hris/employee-image', blank=True)),
                ('emp_id', models.CharField(unique=True, max_length=10)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('zip', models.IntegerField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='employee_created_by', blank=True, to='hris.Employee', null=True)),
                ('deleted_by', models.ForeignKey(related_name='employee_deleted_by', blank=True, to='hris.Employee', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('code', models.CharField(help_text=b'Code defines the short and understandable word for role', max_length=20)),
                ('is_visible', models.BooleanField(default=True)),
                ('icon_class', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(to='hris.Role'),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(related_name='employee_updated_by', blank=True, to='hris.Employee', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
