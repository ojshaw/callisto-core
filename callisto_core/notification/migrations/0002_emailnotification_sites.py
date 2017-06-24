# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-07 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('notification', '0001_initial_create_email_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]
