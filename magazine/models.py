from django.db import models
from django.db.models.fields import IntegerField

class Language(models.Model):
    iso1_code = models.CharField(max_length = 2)
    name = models.CharField(max_length=200)

class User(models.Model):
    UNCONFIRMED = 0
    CONFIRMED = 1
    FORGOT_PASSWORD = 2
    STATUS_CHOICES = (
                   (UNCONFIRMED, 'UNCONFIRMED'),
                   (CONFIRMED,'CONFIRMED'),
                   (FORGOT_PASSWORD, 'FORGOT_PASSWORD'),
    )
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=60)
    token = models.CharField(max_length=30)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNCONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    user_languages = models.ManyToManyField(Language, through='User_Language', through_fields=('user','language_from'))
    
class User_Language(models.Model):
    user = models.ForeignKey(User)
    language_from = models.ForeignKey(Language, related_name='user_language_from')
    language_to = models.ForeignKey(Language, related_name='user_language_to')
    
class Issue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField()
    translated_at = models.DateTimeField()
    published_at = models.DateTimeField()
    issue_users = models.ManyToManyField(User, through='Issue_User')

class Article(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    publisher_name = models.CharField(max_length=60)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Opinion(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    publisher_name = models.CharField(max_length=60)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Issue_User(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey(User)

class Article_Vote(models.Model):
    issue = models.ForeignKey(Issue)
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    vote = IntegerField()
    
class Opinion_Vote(models.Model):
    issue = models.ForeignKey(Issue)
    opinion = models.ForeignKey(Opinion)
    user = models.ForeignKey(User)
    vote = IntegerField()
    
class Article_Translation(models.Model):
    article = models.ForeignKey(Article)
    language_from = models.ForeignKey(Language, related_name='article_language_from')
    language_to = models.ForeignKey(Language, related_name='article_language_to')
    user = models.ForeignKey(User)
    content = models.TextField()
    publisher_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_approved = models.BooleanField(default=False)

class Opinion_Translation(models.Model):
    opinion = models.ForeignKey(Opinion)
    language_from = models.ForeignKey(Language, related_name='opinion_language_from')
    language_to = models.ForeignKey(Language, related_name='opinion_language_to')
    user = models.ForeignKey(User)
    content = models.TextField()
    publisher_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_approved = models.BooleanField(default=False)
