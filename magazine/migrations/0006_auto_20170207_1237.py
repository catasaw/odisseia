# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20160307_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher_name', models.CharField(max_length=60)),
                ('publisher_description', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(to='magazine.Issue')),
                ('language', models.ForeignKey(to='magazine.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Introduction_Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('publisher_name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('introduction', models.ForeignKey(to='magazine.Introduction')),
                ('language_from', models.ForeignKey(related_name='introduction_language_from', to='magazine.Language')),
                ('language_to', models.ForeignKey(related_name='introduction_language_to', to='magazine.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Introduction_Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField()),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('introduction', models.ForeignKey(to='magazine.Introduction')),
                ('issue', models.ForeignKey(to='magazine.Issue')),
            ],
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='opinion',
            name='language',
        ),
        migrations.RemoveField(
            model_name='opinion_translation',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='opinion_translation',
            name='language_from',
        ),
        migrations.RemoveField(
            model_name='opinion_translation',
            name='language_to',
        ),
        migrations.RemoveField(
            model_name='opinion_translation',
            name='opinion',
        ),
        migrations.RemoveField(
            model_name='opinion_vote',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='opinion_vote',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='opinion_vote',
            name='opinion',
        ),
        migrations.AddField(
            model_name='article',
            name='publisher_description',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Opinion',
        ),
        migrations.DeleteModel(
            name='Opinion_Translation',
        ),
        migrations.DeleteModel(
            name='Opinion_Vote',
        ),
    ]
