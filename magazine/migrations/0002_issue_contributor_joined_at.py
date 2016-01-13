# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_contributor',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
