# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0008_auto_20160112_1609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Language',
            new_name='Contributor_Language',
        ),
        migrations.AlterField(
            model_name='contributor',
            name='contributor_languages',
            field=models.ManyToManyField(to='magazine.Language', through='magazine.Contributor_Language'),
        ),
    ]
