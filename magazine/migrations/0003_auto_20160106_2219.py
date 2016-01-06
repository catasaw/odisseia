# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20160106_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='approved_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='translated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
