from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from meetap.settings import AUTH_USER_MODEL
import uuid


# Klasa zmienia autentykację Usera na email
class User(AbstractBaseUser, PermissionsMixin):
    MINOR = 1
    ADULT = 2
    ADULT_MEMBER = 3
    ADULT_COUNCIL_MEMBER = 4
    SUPERUSER = 5
    ROLE_CHOICES = (
     (MINOR, 'User minor'),
     (ADULT, 'User Adult'),
     (ADULT_MEMBER, 'User Adult Member'),
     (ADULT_COUNCIL_MEMBER, 'User Adult Council Member'),
     (SUPERUSER, 'Superuser'),
    )
    OTHER = 0
    MALE = 1
    FEMALE = 2
    GENDERS = (
     (OTHER, 'other'),
     (MALE, 'male'),
     (FEMALE, 'female'),
    )
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True)
    role_council = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True, default=1)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS, null=True, blank=True)
    age = models.DateTimeField(blank=True, null=True)
    mnemo_login = models.CharField(_('mnemo_login'), max_length=11, unique=True)
    karma = models.IntegerField(default=0)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


# Klasa zawierająca tłumaczenia podstawowych elementów formularzy.
class FormItems(models.Model):
    login = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    re_password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    register = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    agree_to_rules = models.CharField(max_length=50)
    male = models.CharField(max_length=50)
    female = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
