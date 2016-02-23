# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import sqlparse


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20160203_1113'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO magazine_language (iso1_code, name) VALUES ('de', 'Deutsch');"),
        migrations.RunSQL("INSERT INTO magazine_language (iso1_code, name) VALUES ('it', 'Italiano');"),
        migrations.RunSQL("INSERT INTO magazine_language (iso1_code, name) VALUES ('en', 'English');"),
        migrations.RunSQL("INSERT INTO magazine_language (iso1_code, name) VALUES ('es', 'Español');"),
        migrations.RunSQL("INSERT INTO magazine_language (iso1_code, name) VALUES ('fr', 'Français');"),
    ]
