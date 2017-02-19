# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0009_auto_20170219_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_translation',
            name='writer_description',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_translation',
            name='writer_name',
            field=models.CharField(default=' ', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introduction_translation',
            name='writer_description',
            field=models.CharField(default=' ', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introduction_translation',
            name='writer_name',
            field=models.CharField(default='string', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article_translation',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='introduction_translation',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
