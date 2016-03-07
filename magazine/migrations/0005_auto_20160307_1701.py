# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_add_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language_Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=0, choices=[(0, b'FIRST_LANGUAGE'), (1, b'SECOND_LANGUAGE')])),
            ],
        ),
        migrations.RemoveField(
            model_name='contributor_language',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='contributor_language',
            name='language_from',
        ),
        migrations.RemoveField(
            model_name='contributor_language',
            name='language_to',
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_languages',
            field=models.ManyToManyField(to='magazine.Language', through='magazine.Language_Contributor'),
        ),
        migrations.DeleteModel(
            name='Contributor_Language',
        ),
        migrations.AddField(
            model_name='language_contributor',
            name='contributor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='language_contributor',
            name='language',
            field=models.ForeignKey(related_name='contributor_languages', to='magazine.Language'),
        ),
    ]
