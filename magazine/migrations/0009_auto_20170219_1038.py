# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0008_auto_20170207_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.CharField(default='de', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introduction',
            name='country',
            field=models.CharField(default='de', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
