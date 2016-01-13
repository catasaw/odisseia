# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('token', models.CharField(max_length=30)),
                ('status', models.IntegerField(default=0, choices=[(0, b'UNCONFIRMED'), (1, b'CONFIRMED'), (2, b'FORGOT_PASSWORD')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher_name', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article_Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('publisher_name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='magazine.Article')),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article_Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField()),
                ('article', models.ForeignKey(to='magazine.Article')),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor_Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=60)),
                ('approved_at', models.DateTimeField(null=True)),
                ('translated_at', models.DateTimeField(null=True)),
                ('published_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('updated_at', models.DateTimeField(null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('contributor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(to='magazine.Issue')),
                ('opinion', models.ForeignKey(to='magazine.Opinion')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_contributors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='magazine.Issue_Contributor'),
        ),
        migrations.AddField(
            model_name='contributor_language',
            name='language_from',
            field=models.ForeignKey(related_name='contributor_language_from', to='magazine.Language'),
        ),
        migrations.AddField(
            model_name='contributor_language',
            name='language_to',
            field=models.ForeignKey(related_name='contributor_language_to', to='magazine.Language'),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
        ),
        migrations.AddField(
            model_name='article_vote',
            name='issue',
            field=models.ForeignKey(to='magazine.Issue'),
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
            model_name='contributor',
            name='contributor_languages',
            field=models.ManyToManyField(to='magazine.Language', through='magazine.Contributor_Language'),
        ),
    ]
