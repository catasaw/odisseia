# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher_name', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article_Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('publisher_name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('is_approved', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='magazine.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField()),
                ('article', models.ForeignKey(to='magazine.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_at', models.DateTimeField()),
                ('translated_at', models.DateTimeField()),
                ('published_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.ForeignKey(to='magazine.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso1_code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher_name', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(to='magazine.Issue')),
                ('language', models.ForeignKey(to='magazine.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion_Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('publisher_name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('is_approved', models.BooleanField(default=False)),
                ('language_from', models.ForeignKey(related_name='opinion_language_from', to='magazine.Language')),
                ('language_to', models.ForeignKey(related_name='opinion_language_to', to='magazine.Language')),
                ('opinion', models.ForeignKey(to='magazine.Opinion')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion_Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField()),
                ('issue', models.ForeignKey(to='magazine.Issue')),
                ('opinion', models.ForeignKey(to='magazine.Opinion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('password', models.CharField(max_length=60)),
                ('token', models.CharField(max_length=30)),
                ('status', models.IntegerField(default=0, choices=[(0, b'UNCONFIRMED'), (1, b'CONFIRMED'), (2, b'FORGOT_PASSWORD')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_from', models.ForeignKey(related_name='user_language_from', to='magazine.Language')),
                ('language_to', models.ForeignKey(related_name='user_language_to', to='magazine.Language')),
                ('user', models.ForeignKey(to='magazine.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_languages',
            field=models.ManyToManyField(to='magazine.Language', through='magazine.User_Language'),
        ),
        migrations.AddField(
            model_name='opinion_vote',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='opinion_translation',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='opinion',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='issue_user',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_users',
            field=models.ManyToManyField(to='magazine.User', through='magazine.Issue_User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='article_vote',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
        ),
        migrations.AddField(
            model_name='article_vote',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='article_translation',
            name='language_from',
            field=models.ForeignKey(related_name='article_language_from', to='magazine.Language'),
        ),
        migrations.AddField(
            model_name='article_translation',
            name='language_to',
            field=models.ForeignKey(related_name='article_language_to', to='magazine.Language'),
        ),
        migrations.AddField(
            model_name='article_translation',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
        ),
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.ForeignKey(to='magazine.Language'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to='magazine.User'),
        ),
    ]
