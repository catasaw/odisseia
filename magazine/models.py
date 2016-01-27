from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager,\
    BaseUserManager
from django.db.models.fields import IntegerField
from django.db.models.signals import post_save
from django.db.models import Sum

class Language(models.Model):
    iso1_code = models.CharField(max_length = 2)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class ContributorManager(BaseUserManager):
    def create_user(self, email, status, password=None):
        """
        Creates and saves a User with the given email, status and password.
        """
        if not email:
            raise ValueError('Contributors must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            status=status,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, status, password):
        """
        Creates and saves a superuser with the given email, status and password.
        """
        user = self.create_user(email,
            password=password,
            status=status
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Contributor(AbstractBaseUser):
    UNCONFIRMED = 0
    CONFIRMED = 1
    FORGOT_PASSWORD = 2
    STATUS_CHOICES = (
                   (UNCONFIRMED, 'UNCONFIRMED'),
                   (CONFIRMED,'CONFIRMED'),
                   (FORGOT_PASSWORD, 'FORGOT_PASSWORD'),
    )
    email = models.EmailField(max_length=255, unique=True)
    token = models.CharField(max_length=30)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNCONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    contributor_languages = models.ManyToManyField(Language, through='Contributor_Language', through_fields=('contributor','language_from'))
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects     =   ContributorManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['status']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email[:3] + '...'

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# Create User object to attach to Contributor object

def create_contributor_user_callback(sender, instance, **kwargs):
    contributor, new = Contributor.objects.get_or_create(user=instance)
post_save.connect(create_contributor_user_callback, User)

class Contributor_Language(models.Model):
    contributor = models.ForeignKey(Contributor)
    language_from = models.ForeignKey(Language, related_name='contributor_language_from')
    language_to = models.ForeignKey(Language, related_name='contributor_language_to')
    
class Issue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=60)
    approved_at = models.DateTimeField(null=True)
    translated_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    issue_contributors = models.ManyToManyField(Contributor, through='Issue_Contributor')
    
    def __str__(self):
        return self.title
    
    # TODO: Check if this methods should be in a manager in a different file
    def amount_contributors(self):
        return self.issue_contributors.count()
    
    def amount_opinions(self):
        return Opinion.objects.filter(issue_id=self.id).count()
    
    def amount_articles(self):
        return Article.objects.filter(issue_id=self.id).count()

class Article(models.Model):
    issue = models.ForeignKey(Issue)
    contributor = models.ForeignKey(Contributor)
    language = models.ForeignKey(Language)
    publisher_name = models.CharField(max_length=60)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Opinion(models.Model):
    issue = models.ForeignKey(Issue)
    contributor = models.ForeignKey(Contributor)
    language = models.ForeignKey(Language)
    publisher_name = models.CharField(max_length=60)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:4]
    
    # TODO: Move to Manager?
    def get_votes_count(self):
        votes_array = Opinion_Vote.objects.filter(opinion_id=self.id).aggregate(Sum(('vote')))
        return votes_array['vote__sum']

class Comment(models.Model):
    issue = models.ForeignKey(Issue)
    contributor = models.ForeignKey(Contributor)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Issue_Contributor(models.Model):
    issue = models.ForeignKey(Issue)
    contributor = models.ForeignKey(Contributor)
    joined_at = models.DateTimeField(auto_now_add=True)

class Article_Vote(models.Model):
    issue = models.ForeignKey(Issue)
    article = models.ForeignKey(Article)
    contributor = models.ForeignKey(Contributor)
    vote = IntegerField()
    
class Opinion_Vote(models.Model):
    # TODO: do we need a foreign key to issue?
    issue = models.ForeignKey(Issue)
    opinion = models.ForeignKey(Opinion)
    contributor = models.ForeignKey(Contributor)
    vote = IntegerField()
    
class Article_Translation(models.Model):
    article = models.ForeignKey(Article)
    language_from = models.ForeignKey(Language, related_name='article_language_from')
    language_to = models.ForeignKey(Language, related_name='article_language_to')
    contributor = models.ForeignKey(Contributor)
    content = models.TextField()
    publisher_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_approved = models.BooleanField(default=False)

class Opinion_Translation(models.Model):
    opinion = models.ForeignKey(Opinion)
    language_from = models.ForeignKey(Language, related_name='opinion_language_from')
    language_to = models.ForeignKey(Language, related_name='opinion_language_to')
    contributor = models.ForeignKey(Contributor)
    content = models.TextField()
    publisher_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_approved = models.BooleanField(default=False)
