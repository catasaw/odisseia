# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20170207_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='introduction',
            old_name='publisher_description',
            new_name='writer_description',
        ),
        migrations.RenameField(
            model_name='introduction',
            old_name='publisher_name',
            new_name='writer_name',
        ),
    ]
