from django.db import models
from meetap.settings import AUTH_USER_MODEL


# Klasa główna wydarzenia.
# Najwyższy "Rodzic" spośród klas podległych "wydarzeniom".
# Może zamiast robić listę z PSIField dla orientacji itp lepiej zrobić
# dla każdej możliwej opcji po BooleanField?
class Event(models.Model):
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
    other_drugs = models.CharField(max_length=300, blank=True, null=True)  # Jakie inne używki?
    is_sex_party = models.BooleanField(default=False)  # Seksimpreza?
    is_paid = models.BooleanField(default=False)  # czy jest składka w $
    # Opcje czy dla danej orientacji/dominacji/roli:
    is_for_straight = models.BooleanField(default=False)
    is_for_gay = models.BooleanField(default=False)
    is_for_bi = models.BooleanField(default=False)
    is_for_trans = models.BooleanField(default=False)
    is_for_other = models.BooleanField(default=False)
    is_for_passive = models.BooleanField(default=False)
    is_for_r_passive = models.BooleanField(default=False)
    is_for_switch = models.BooleanField(default=False)
    is_for_r_active = models.BooleanField(default=False)
    is_for_active = models.BooleanField(default=False)
    is_for_submisive = models.BooleanField(default=False)
    is_for_r_submissive = models.BooleanField(default=False)
    is_for_neutral = models.BooleanField(default=False)
    is_for_r_dominant = models.BooleanField(default=False)
    is_for_dominant = models.BooleanField(default=False)
    # Jakie inne orientacje? Oddzielone przecinkami.
    other_preferences = models.CharField(max_length=300, blank=True, null=True)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data publikacji


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

    def __str__(self):
        return self.title


# Klasa Roli usera na wydarzeniu.
class UserRole(models.Model):
    title = models.CharField(max_length=150)
    role_descr = models.CharField(max_length=600, blank=True, null=True)
    # "Dziecko" klasy dzielącej wydarzenie na strefy.
    from_event = models.ForeignKey('PartyDivider', on_delete=models.CASCADE,)
    # Użytkownik może być przydzielony z bazy danych lub nie.
    assigned_user = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # Jesli Użytkownika nie ma na portalu to tutaj wpisuje się jego nazwę.
    # Wyświetla się tylko wtedy gdy powyższe jest puste.
    alt_user = models.CharField(max_length=150, blank=True, null=True)
    # Czy zwolniony ze składek?
    tax_free = models.BooleanField(default=False)
    # Czy koordynator pomocniczy?
    aux_coordinator = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Klasa panelu składki. Rodzic "Składek"
class TaxPanel(models.Model):
    AND = 0
    OR = 1
    OPTIONAL = 2
    EVERYONE = 3
    TAX_CHOICES = (
        (AND, "i"),
        (OR, "lub"),
        (OPTIONAL, "opcjonalnie"),
        (EVERYONE, "każdy"),
        )
    title = models.CharField(max_length=50)
    descr = models.CharField(max_length=200, blank=True, null=True)
    tax_type = models.PositiveSmallIntegerField(
            choices=TAX_CHOICES, default=0)
    from_event = models.ForeignKey('Event', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title


# Klasa składki. Dziecko "Panelu składki"
class Tax(models.Model):
    title = models.CharField(max_length=50)
    # Opis składki pojawiający się jako onhover ikony "informacja".
    descr = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    from_event = models.ForeignKey('TaxPanel', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
