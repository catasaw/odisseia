# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_issue_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Contributor',
        ),
    ]
