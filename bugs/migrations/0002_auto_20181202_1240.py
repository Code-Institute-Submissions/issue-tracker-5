# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 02:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20181129_1729'),
        ('features', '0001_initial'),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='feature_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Features'),
        ),
        migrations.AddField(
            model_name='comments',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfilePicture'),
        ),
        migrations.AddField(
            model_name='comments',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.Bugs'),
        ),
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bugupvote',
            name='upvoted_bug',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bugs.Bugs'),
        ),
        migrations.AddField(
            model_name='bugupvote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bugs',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfilePicture'),
        ),
        migrations.AddField(
            model_name='bugs',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]