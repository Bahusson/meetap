from django.db import models
from meetap.settings import AUTH_USER_MODEL


# Klasa główna wydarzenia.
# Najwyższy "Rodzic" spośród klas podległych "wydarzeniom".
class Event(models.Model):
    NONE = 0
    STRAIGHT = 1
    GAY = 2
    BI = 3
    TRANS = 4
    OTHER = 5
    SEX_CHOICES = (
        (NONE, "Brak"),
        (STRAIGHT, "Straight"),
        (GAY, "Gay"),
        (BI, "Bi"),
        (TRANS, "Trans"),
        (OTHER, "Other"),
        )
    NONE = 0
    PASSIVE = 1
    R_PASSIVE = 2
    SWITCH = 3
    R_ACTIVE = 4
    ACTIVE = 5
    ACTIVE_CHOICES = (
        (NONE, "Brak"),
        (PASSIVE, "Pasywny"),
        (R_ACTIVE, "Raczej Pasywny"),
        (SWITCH, "Zmienny"),
        (R_ACTIVE, "Raczej Aktywny"),
        (ACTIVE, "Aktywny"),
    )
    NONE = 0
    SUBMISSIVE = 1
    R_SUBMISSIVE = 2
    NEUTRAL = 3
    R_DOMINANT = 4
    DOMINANT = 5
    DOMINANCE_CHOICES = (
        (NONE, "Brak"),
        (SUBMISSIVE, "Uległy"),
        (R_SUBMISSIVE, "Raczej Uległy"),
        (NEUTRAL, "Neutralny"),
        (R_DOMINANT, "Raczej Dominujący"),
        (DOMINANT, "Dominujący"),
        )
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    datefrom = models.DateTimeField(blank=True, null=True)  # Początek
    dateto = models.DateTimeField(blank=True, null=True)  # Zakończenie
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)  # Twórca wydarzenia
    is_commercial = models.BooleanField(default=False)  # Komercyjne?
    is_mass_event = models.BooleanField(default=False)  # Masowe?
    is_adult_only = models.BooleanField(default=False)  # Dla dorosłych?
    is_alcohol = models.BooleanField(default=False)  # Z alkoholem?
    is_tobacco = models.BooleanField(default=False)  # Dla palących?
    other_drugs = models.CharField(max_length=300)  # Jakie inne używki?
    is_sex_party = models.BooleanField(default=False)  # Seksimpreza?
    is_paid = models.BooleanField(default=False)  # czy jest składka w $
    sex_preference = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES, default=0)
    sex_role_activity = models.PositiveSmallIntegerField(
        choices=ACTIVE_CHOICES, default=0)
    sex_role_dominance = models.PositiveSmallIntegerField(
        choices=DOMINANCE_CHOICES, default=0)
    # Jakie inne orientacje? Oddzielone przecinkami.
    other_preferences = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['-datefrom']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Klasa tłumaczeniowa dla menu wydarzeń
class EventsMenuNames(models.Model):
    maintitle = models.CharField(max_length=50)  # Menu wydarzeń
    new_event = models.CharField(max_length=50)  # Nowe wydarzenie
    my_events = models.CharField(max_length=50)  # Moje wydarzenie
    edit_event = models.CharField(max_length=50)  # Edytuj wydarzenie
    search_events = models.CharField(max_length=50)  # Wyszukaj wydarzenie
    my_templates = models.CharField(max_length=50)  # Moje wzorniki

    class Meta:
        verbose_name_plural = 'EventsMenuNames'


# Klasa pozwala dzielić wydarzenie na różne pomniejsze "działy".
# Np. "pokład", "zaplecze", "udźwiękownienie", itp.
class PartyDivider(models.Model):
    title = models.CharField(max_length=150)
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    from_event = models.ForeignKey('Event', on_delete=models.CASCADE,)

class UserRole(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1500, blank=True, null=True)
    from_event = models.ForeignKey('PartyDivider', on_delete=models.CASCADE,)
    role_descr = models.CharField(max_length=600, blank=True, null=True)
    # Czy zwolniony ze składek?
    tax_free = models.BooleanField(default=False)
    # Czy koordynator pomocniczy?
    aux_coordinator = models.BooleanField(default=False)
