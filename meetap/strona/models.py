from django.db import models
from esks.settings import AUTH_USER_MODEL


class Pageitem(models.Model):
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
    addblog = models.CharField(max_length=200)
    addinfo = models.CharField(max_length=200)
    editme = models.CharField(max_length=200)

    def mainpage_c(self):
        return self.mainpage.upper()


# Aktualności widoczne na głównych kafelkach na stronie.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
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


# Bardziej permanentne "ważne informacje" ze strony E-SKS.
class Info (models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
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
