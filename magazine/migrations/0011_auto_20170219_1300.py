# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_auto_20170219_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_translation',
            name='country',
            field=models.CharField(default='de', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introduction_translation',
            name='country',
            field=models.CharField(default='de', max_length=2),
            preserve_default=False,
        ),
    ]
