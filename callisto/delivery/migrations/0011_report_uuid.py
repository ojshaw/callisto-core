# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-10 22:54
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_email_notification_data_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
