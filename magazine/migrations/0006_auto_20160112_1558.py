# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20160112_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='article_translation',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='article_vote',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='user_languages',
            new_name='contributor_languages',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_users',
            new_name='issue_contributors',
        ),
        migrations.RenameField(
            model_name='issue_user',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='opinion_translation',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='opinion_vote',
            old_name='user',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='user_language',
            old_name='user',
            new_name='contributor',
        ),
    ]
