# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20160106_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
