# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0011_auto_20170219_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue_Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(to='magazine.Issue')),
                ('language_from', models.ForeignKey(related_name='issue_language_from', to='magazine.Language')),
                ('language_to', models.ForeignKey(related_name='issue_language_to', to='magazine.Language')),
            ],
        ),
    ]
