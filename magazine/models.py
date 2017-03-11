from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager,\
    BaseUserManager
from django.db.models.fields import IntegerField
from django.db.models.signals import post_save
from django.db.models import Sum
from ckeditor.fields import RichTextField

#TODO: Check a better way to set default encoding
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    contributor_languages = models.ManyToManyField(Language, through='Language_Contributor', through_fields=('contributor','language'))
    
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



class Language_Contributor(models.Model):
    FIRST_LANGUAGE = 0
    SECOND_LANGUAGE = 1
    LANGUAGES_CHOICES = (
                   (FIRST_LANGUAGE, 'FIRST_LANGUAGE'),
                   (SECOND_LANGUAGE,'SECOND_LANGUAGE'),
    )
    contributor = models.ForeignKey(Contributor)
    language = models.ForeignKey(Language, related_name='contributor_languages')
    type = models.IntegerField(choices=LANGUAGES_CHOICES, default=FIRST_LANGUAGE)
    
class Issue(models.Model):
    MIN_AMOUNT_CONTRIBUTORS = 6
    
    IN_PROGRESS         = 0
    PENDING             = 1
    APPROVED            = 2
    PUBLISHED           = 3
    REJECTED            = 4
    
    STATUS_CHOICES = (
                   (IN_PROGRESS, 'IN_PROGRESS'),
                   (PENDING,'PENDING'),
                   (APPROVED, 'APPROVED'),
                   (PUBLISHED, 'PUBLISHED'),
                   (REJECTED, 'REJECTED')
    )
    created_at          = models.DateTimeField(auto_now_add=True)
    title               = models.CharField(max_length=60)
    status              = models.IntegerField(choices=STATUS_CHOICES, default=IN_PROGRESS)
    #TODO: Make trigger to update this field when status changes
    status_changed_at   = models.DateTimeField(null=True)
    issue_contributors  = models.ManyToManyField(Contributor, through='Issue_Contributor')
    
    def __str__(self):
        return self.title
    
    # TODO: Check if this methods should be in a manager in a different file
    def amount_contributors(self):
        return self.issue_contributors.count()
    
    def amount_articles(self):
        return Article.objects.filter(issue_id=self.id).count()
    
    def amount_introductions(self):
        return Introduction.objects.filter(issue_id=self.id).count()
    
    def is_pending(self):
        return self.status == Issue.PENDING

class Issue_Translation(models.Model):
    issue           = models.ForeignKey(Issue)
    language_from   = models.ForeignKey(Language, related_name='issue_language_from')
    language_to     = models.ForeignKey(Language, related_name='issue_language_to')
    title           = models.CharField(max_length=60)
    created_at      = models.DateTimeField(auto_now_add=True)
    
class Introduction(models.Model):
    issue               = models.ForeignKey(Issue)
    contributor         = models.ForeignKey(Contributor)
    language            = models.ForeignKey(Language)
    country             = models.CharField(max_length=2)
    writer_name         = models.CharField(max_length=60)
    writer_description  = models.CharField(max_length=60)
    content             = RichTextField()
    is_approved          = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    TOTAL_ARTICLES_IN_ISSUE = 5
    
    issue               = models.ForeignKey(Issue)
    contributor         = models.ForeignKey(Contributor)
    language            = models.ForeignKey(Language)
    country             = models.CharField(max_length=2)
    writer_name         = models.CharField(max_length=60)
    writer_description  = models.CharField(max_length=60)
    content             = RichTextField()
    is_approved         = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:4]
    
    # TODO: Move to Manager?
    def get_votes_count(self):
        votes_array = Article_Vote.objects.filter(article_id=self.id).aggregate(Sum(('vote')))
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

class Introduction_Vote(models.Model):
    issue = models.ForeignKey(Issue)
    introduction = models.ForeignKey(Introduction)
    contributor = models.ForeignKey(Contributor)
    vote = IntegerField()
    
class Article_Vote(models.Model):
    MAX_VOTES_PER_CONTRIBUTOR = 5
    MIN_PERCENTAGE_VOTES_IN_ISSUE = 0.8
    # TODO: do we need a foreign key to issue?
    issue       = models.ForeignKey(Issue)
    article     = models.ForeignKey(Article)
    contributor = models.ForeignKey(Contributor)
    vote        = IntegerField()
    
class Introduction_Translation(models.Model):
    introduction    = models.ForeignKey(Introduction)
    issue_translation = models.ForeignKey(Issue_Translation)
    language_from   = models.ForeignKey(Language, related_name='introduction_language_from')
    language_to     = models.ForeignKey(Language, related_name='introduction_language_to')
    contributor     = models.ForeignKey(Contributor)
    country             = models.CharField(max_length=2)
    content         = RichTextField()
    publisher_name  = models.CharField(max_length=60)
    writer_name         = models.CharField(max_length=60)
    writer_description  = models.CharField(max_length=60)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(null=True)
    is_approved     = models.BooleanField(default=False)

class Article_Translation(models.Model):
    article        = models.ForeignKey(Article)
    issue_translation = models.ForeignKey(Issue_Translation)
    language_from  = models.ForeignKey(Language, related_name='article_language_from')
    language_to    = models.ForeignKey(Language, related_name='article_language_to')
    contributor    = models.ForeignKey(Contributor)
    country             = models.CharField(max_length=2)
    content        = RichTextField()
    publisher_name = models.CharField(max_length=60)
    writer_name         = models.CharField(max_length=60)
    writer_description  = models.CharField(max_length=60)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(null=True)
    is_approved    = models.BooleanField(default=False)
