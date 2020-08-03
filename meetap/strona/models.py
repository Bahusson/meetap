from django.db import models
from meetap.settings import AUTH_USER_MODEL


# Klasa tłumaczeniowa dla "core"
class PageNames(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    information = models.CharField(max_length=200)  # Informacje w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    logout = models.CharField(max_length=200)  # Wyloguj
    news = models.CharField(max_length=200)  # Aktualności
    faq = models.CharField(max_length=200)  # FAQ
    login = models.CharField(max_length=200)  # zaloguj
    panel_user = models.CharField(max_length=200)
    panel_council = models.CharField(max_length=200)
    panel_staff = models.CharField(max_length=200)
    backtouserpanel = models.CharField(max_length=200)
    see_more = models.CharField(max_length=200)
    editme = models.CharField(max_length=200)
    faq = models.CharField(max_length=200)
    settings = models.CharField(max_length=200)
    myprofile = models.CharField(max_length=200)
    events = models.CharField(max_length=200)
    friends = models.CharField(max_length=200)
    rules = models.CharField(max_length=200)
    register = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'PageNames'

    # def mainpage_c(self):
    #    return self.mainpage.upper()
    # Wycięte, bo by się zesrało z funkcją all_names w translatorze
    # Puszczaj takie rzeczy przez dodatkowe funkcje lub templatetagi.


# Aktualności widoczne na głównych kafelkach na stronie.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    lastmod = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Klasa skórek do naszej apki. Pola nienulowalne.
class PageSkin(models.Model):
    themetitle = models.CharField(max_length=200)
    position = models.IntegerField()
    blogimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    avatarimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    welcomebanner = models.ImageField(
     upload_to='skins', blank=True, null=True)
    welcomebanner_small = models.ImageField(
     upload_to='skins', blank=True, null=True)
    meetaplogo_main = models.ImageField(
     upload_to='skins', blank=True, null=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.themetitle


# klasa tłumaczeniowa dla Bloga i forum Mecenasów
class BlogNames(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    lastmod = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)
    new = models.CharField(max_length=200)
    change = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'BlogNames'


# Klasa tłumaczeniowa dla Login/Register i myprofile.
class RegNames(models.Model):
    password = models.CharField(max_length=50, null=True)
    re_password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    agree_to_rules = models.CharField(max_length=50)
    male = models.CharField(max_length=50)
    female = models.CharField(max_length=50)
    other = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'RegNames'


# Klasa tłumaczeniowa dla myprofile.
class ProfileNames(models.Model):
    sex_preference = models.CharField(max_length=50, null=True)
    sex_role_activity = models.CharField(max_length=50, null=True)
    sex_role_dominance = models.CharField(max_length=50, null=True)
    alcohol = models.CharField(max_length=50, null=True)
    tobacco = models.CharField(max_length=50, null=True)
    other_drugs = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=50, null=True)
    other_contact = models.CharField(max_length=50, null=True)
    about_me = models.CharField(max_length=50, null=True)
    interests = models.CharField(max_length=50, null=True)
    showme_adultcontent = models.CharField(max_length=50, null=True)
    showmy_sexorientation = models.CharField(max_length=50, null=True)
    showmy_sexrole = models.CharField(max_length=50, null=True)
    showme_commercial = models.CharField(max_length=50, null=True)
    showme_massevents = models.CharField(max_length=50, null=True)
    sendme_inv_status_me = models.CharField(max_length=150, null=True)
    sendme_inv_status_others = models.CharField(max_length=150, null=True)
    sendme_invitations = models.CharField(max_length=150, null=True)
    sendme_friend_events = models.CharField(max_length=150, null=True)
    sendme_join_request = models.CharField(max_length=150, null=True)
    active = models.CharField(max_length=50, null=True)
    passive = models.CharField(max_length=50, null=True)
    neutral = models.CharField(max_length=50, null=True)
    dominant = models.CharField(max_length=50, null=True)
    submissive = models.CharField(max_length=50, null=True)
    profile_settings = models.CharField(max_length=50, null=True)
    general_settings = models.CharField(max_length=50, null=True)
    contact_settings = models.CharField(max_length=50, null=True)
    adult_settings = models.CharField(max_length=50, null=True)
    mailing_settings = models.CharField(max_length=50, null=True)
    avatar = models.CharField(max_length=50, null=True)
    mnemo_login = models.CharField(max_length=50, null=True)
    mnemo_explanation = models.CharField(max_length=150, null=True)
    age_explanation = models.CharField(max_length=150, null=True)
    contact_explanation = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name_plural = 'ProfileNames'
