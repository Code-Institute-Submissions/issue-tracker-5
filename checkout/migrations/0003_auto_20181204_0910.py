# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20181202_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='upvoted_feature',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]