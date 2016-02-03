# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_issue_contributor_joined_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='approved_at',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='translated_at',
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'IN_PROGRESS'), (1, b'PENDING'), (2, b'APPROVED'), (3, b'PUBLISHED'), (4, b'REJECTED')]),
        ),
        migrations.AddField(
            model_name='issue',
            name='status_changed_at',
            field=models.DateTimeField(null=True),
        ),
    ]
