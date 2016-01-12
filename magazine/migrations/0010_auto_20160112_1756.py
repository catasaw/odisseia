# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0009_auto_20160112_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='password',
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
