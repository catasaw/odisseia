# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0007_auto_20160112_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_language',
            name='language_from',
            field=models.ForeignKey(related_name='contributor_language_from', to='magazine.Language'),
        ),
        migrations.AlterField(
            model_name='user_language',
            name='language_to',
            field=models.ForeignKey(related_name='contributor_language_to', to='magazine.Language'),
        ),
    ]
