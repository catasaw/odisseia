# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_auto_20160112_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='email',
        ),
    ]
