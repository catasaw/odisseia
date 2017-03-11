# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0012_issue_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_translation',
            name='issue_translation',
            field=models.ForeignKey(default=1, to='magazine.Issue_Translation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='introduction_translation',
            name='issue_translation',
            field=models.ForeignKey(default=1, to='magazine.Issue_Translation'),
            preserve_default=False,
        ),
    ]
