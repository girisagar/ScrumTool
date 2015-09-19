# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBacklog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='productbacklog_created_by', to='hris.Employee')),
                ('deleted_by', models.ForeignKey(related_name='productbacklog_deleted_by', blank=True, to='hris.Employee', null=True)),
                ('owner', models.ForeignKey(related_name='productbacklog_owned_by', blank=True, to='hris.Employee', null=True)),
                ('updated_by', models.ForeignKey(related_name='productbacklog_updated_by', to='hris.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseBacklog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='release_backlog_created_by', to='hris.Employee')),
                ('deleted_by', models.ForeignKey(related_name='release_backlog_deleted_by', blank=True, to='hris.Employee', null=True)),
                ('product_backlog', models.ForeignKey(blank=True, to='scrum.ProductBacklog', null=True)),
                ('scrum_master', models.ForeignKey(blank=True, to='hris.Employee', null=True)),
                ('updated_by', models.ForeignKey(related_name='release_backlog_updated_by', to='hris.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Sprint name should be in order like Sprint-1, Sprint-2, and so on', unique=True, max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='sprint_created_by', to='hris.Employee')),
                ('deleted_by', models.ForeignKey(related_name='sprint_deleted_by', blank=True, to='hris.Employee', null=True)),
                ('release_backlog', models.ForeignKey(blank=True, to='scrum.ReleaseBacklog', null=True)),
                ('updated_by', models.ForeignKey(related_name='sprint_updated_by', to='hris.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('developer_effort', models.IntegerField(null=True, blank=True)),
                ('tester_effort', models.IntegerField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('assiged_developer', models.ForeignKey(related_name='userstory_assiged_developer', blank=True, to='hris.Employee', null=True)),
                ('assiged_tester', models.ForeignKey(related_name='userstory_assiged_tester', blank=True, to='hris.Employee', null=True)),
                ('created_by', models.ForeignKey(related_name='userstory_created_by', to='hris.Employee')),
                ('deleted_by', models.ForeignKey(related_name='userstory_deleted_by', blank=True, to='hris.Employee', null=True)),
                ('product_backlog', models.ForeignKey(blank=True, to='scrum.ProductBacklog', null=True)),
                ('release_backlog', models.ForeignKey(blank=True, to='scrum.ReleaseBacklog', null=True)),
                ('sprint', models.ForeignKey(blank=True, to='scrum.Sprint', null=True)),
                ('updated_by', models.ForeignKey(related_name='userstory_updated_by', to='hris.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('work_remaining', models.IntegerField()),
                ('work_done', models.IntegerField()),
                ('description', models.TextField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='worklog_created_by', to='hris.Employee')),
                ('deleted_by', models.ForeignKey(related_name='worklog_deleted_by', blank=True, to='hris.Employee', null=True)),
                ('employee', models.ForeignKey(related_name='worklog_employee', to='hris.Employee')),
                ('updated_by', models.ForeignKey(related_name='worklog_updated_by', to='hris.Employee')),
                ('user_story', models.ForeignKey(related_name='worklog_employee', to='scrum.UserStory')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='worklog',
            unique_together=set([('date', 'employee')]),
        ),
    ]
