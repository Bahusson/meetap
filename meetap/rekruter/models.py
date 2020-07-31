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
    STRAIGHT = 0
    GAY = 1
    BI = 2
    TRANS = 3
    OTHER = 4
    SEX_CHOICES = (
        (STRAIGHT, "Straight"),
        (GAY, "Gay"),
        (BI, "Bi"),
        (TRANS, "Trans"),
        (OTHER, "Other"),
    )
    NO_DRINKING = 0
    LET_OTHERS_DRINK = 1
    DRINKS_SOME = 2
    ALCAHOLIC = 3
    ALCOHOL_CHOICES = (
        (NO_DRINKING, "No drinking"),
        (LET_OTHERS_DRINK, "Doesn't mind company"),
        (DRINKS_SOME, "Drinks alcohol"),
        (ALCAHOLIC, "Drinks heavily"),
    )
    NO_SMOKING = 0
    LET_OTHERS_SMOKE = 1
    SMOKES_SOME = 2
    HEAVY_SMOKER = 3
    TOBACCO_CHOICES = (
        (NO_SMOKING, "No smoking"),
        (LET_OTHERS_SMOKE, "Doesn't mind company"),
        (SMOKES_SOME, "Smokes sometimes"),
        (HEAVY_SMOKER, "Smokes heavily"),
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first_name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'))
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True)
    role_council = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=1)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS, null=True, blank=True)
    age = models.DateField()
    mnemo_login = models.CharField(_('mnemo_login'), max_length=11, unique=True, blank=True)
    karma = models.IntegerField(default=0)
    sex_orientation = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES, null=True)
    other_orientation = models.CharField(_('other_orientation'), max_length=30, blank=True)
    sex_role_activity = models.IntegerField(null=True, blank=True)  # 0-100
    sex_role_dominance = models.IntegerField(null=True, blank=True)  # 0-100
    alcohol = models.PositiveSmallIntegerField(
        choices=ALCOHOL_CHOICES, null=True)
    tobacco = models.PositiveSmallIntegerField(
        choices=TOBACCO_CHOICES, null=True)
    # Inne używki - nie podlega wyszukiwaniu.
    other_drugs = models.CharField(_('other_drugs'), max_length=300, blank=True)
    # Numer telefonu. Opcjonalny
    telephone = models.CharField(_('telephone'), max_length=30, blank=True)
    # Inne formy kontaktu ze mną.
    other_contact = models.CharField(_('other_contact'), max_length=300, blank=True)
    # Sekcja "O mnie"
    about_me = models.CharField(_('other_contact'), max_length=1500, blank=True)
    # Zainteresowania w formacie csv
    interests = models.CharField(_('other_contact'), max_length= 500, blank=True)
    # Pokaż mi treści dla dorosłych.
    showme_adultcontent = models.BooleanField(_('showme_adultcontent'), default=False,)
    # Pokaż moją orientację seksualną.
    showmy_sexorientation = models.BooleanField(_('showmy_sexorientation'), default=False,)
    # Pokaż moją rolę w seksie.
    showmy_sexrole = models.BooleanField(_('showmy_sexrole'), default=False,)
    # Pokazuj imprezy komercyjne
    showme_commercial = models.BooleanField(_('showme_commercial'), default=True,)
    # Pokazuj imprezy typu "Open"
    showme_massevents = models.BooleanField(_('showme_massevents'), default=True,)
    # Wysyłaj mi informację o odrzuceniu/akceptacji mojej prośby o doł. do wyd.
    sendme_inv_status_me = models.BooleanField(_('sendme_inv_status_me'), default=True,)
    # Wysyłaj mi informację o odrzuceniu/akceptacji zaproszeń na wyd., które ja wysłałem.
    sendme_inv_status_others = models.BooleanField(_('sendme_inv_status_others'), default=True,)
    # Wysyłaj mi wiadomości o otrzymanych przeze mnie zaproszeniach na wyd.
    sendme_invitations = models.BooleanField(_('sendme_invitations'), default=True,)
    # Wysyłaj mi wiadomości o tym, że znajomy utworzył nowe wydarzenia.
    sendme_friend_events = models.BooleanField(_('sendme_invitations'), default=True,)
    # Wysyłaj mi informację o tym, że ktoś poprosił o dołączenie do mojego wyd.
    sendme_join_request = models.BooleanField(_('sendme_invitations'), default=True,)



    # location = Tutaj wstaw pole geolokalizacji. Do ogarnięcia.
    # search_radius = integer field? do powyższego. W km. Domyślne 5

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
