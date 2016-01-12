# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20160112_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Issue_User',
            new_name='Issue_Contributor',
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_contributors',
            field=models.ManyToManyField(to='magazine.Contributor', through='magazine.Issue_Contributor'),
        ),
    ]
