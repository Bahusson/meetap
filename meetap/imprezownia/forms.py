from django import forms
from .models import Event, PartyDivider, TaxPanel, UserRole, Tax
from meetap.core.classes import checkifnull as cn
#  from meetap.core.snippets import flare
import datetime


class EventForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=False)
    body = forms.CharField(max_length=1500, required=False)
    image = forms.ImageField(required=False)
    datefrom = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    dateto = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    is_commercial = forms.BooleanField(required=False)  # Komercyjne?
    is_mass_event = forms.BooleanField(required=False)   # Masowe?
    is_adult_only = forms.BooleanField(required=False)  # Dla dorosłych?
    is_alcohol = forms.BooleanField(required=False)  # Z alkoholem?
    is_tobacco = forms.BooleanField(required=False)  # Dla palących?
    other_drugs = forms.CharField(max_length=300, required=False)  # Jakie inne używki?
    is_sex_party = forms.BooleanField(required=False)  # Seksimpreza?
    is_paid = forms.BooleanField(required=False)  # czy jest składka w $
    is_for_straight = forms.BooleanField(required=False)
    is_for_gay = forms.BooleanField(required=False)
    is_for_bi = forms.BooleanField(required=False)
    is_for_trans = forms.BooleanField(required=False)
    is_for_other = forms.BooleanField(required=False)
    is_for_passive = forms.BooleanField(required=False)
    is_for_r_passive = forms.BooleanField(required=False)
    is_for_switch = forms.BooleanField(required=False)
    is_for_r_active = forms.BooleanField(required=False)
    is_for_active = forms.BooleanField(required=False)
    is_for_submisive = forms.BooleanField(required=False)
    is_for_r_submissive = forms.BooleanField(required=False)
    is_for_neutral = forms.BooleanField(required=False)
    is_for_r_dominant = forms.BooleanField(required=False)
    is_for_dominant = forms.BooleanField(required=False)
    other_preferences = forms.CharField(max_length=300, required=False)
    delete_image = forms.BooleanField(required=False)

    class Meta:
        model = Event
        fields = (
         "title", "body", "image", "datefrom", "dateto", "is_commercial",
         "is_mass_event", "is_adult_only", "is_alcohol", "is_tobacco",
         "other_drugs", "is_sex_party", "is_paid", "is_for_straight",
         "is_for_gay", "is_for_bi", "is_for_trans", "is_for_other",
         "is_for_passive", "is_for_r_passive", "is_for_switch",
         "is_for_r_active", "is_for_active", "is_for_submisive",
         "is_for_r_submissive", "is_for_neutral", "is_for_r_dominant",
         "is_for_dominant", "other_preferences")

    def save(self, user_id, commit=True):
        event = super(EventForm, self).save(commit=False)
        event.title = self.cleaned_data["title"]
        event.body = self.cleaned_data["body"]
        event.datefrom = cn(self.cleaned_data["datefrom"], False)
        event.dateto = cn(self.cleaned_data["dateto"], False)
        event.owner = user_id
        event.is_commercial = cn(self.cleaned_data["is_commercial"], False)
        event.is_mass_event = cn(self.cleaned_data["is_mass_event"], False)
        event.is_adult_only = cn(self.cleaned_data["is_adult_only"], False)
        event.is_alcohol = cn(self.cleaned_data["is_alcohol"], False)
        event.is_tobacco = cn(self.cleaned_data["is_tobacco"], False)
        event.other_drugs = self.cleaned_data["other_drugs"]
        event.is_sex_party = cn(self.cleaned_data["is_sex_party"], False)
        event.is_paid = cn(self.cleaned_data["is_paid"], False)
        event.is_for_straight = cn(self.cleaned_data["is_for_straight"], False)
        event.is_for_gay = cn(self.cleaned_data["is_for_gay"], False)
        event.is_for_bi = cn(self.cleaned_data["is_for_bi"], False)
        event.is_for_trans = cn(self.cleaned_data["is_for_trans"], False)
        event.is_for_other = cn(self.cleaned_data["is_for_other"], False)
        event.is_for_passive = cn(self.cleaned_data["is_for_passive"], False)
        event.is_for_r_passive = cn(
         self.cleaned_data["is_for_r_passive"], False)
        event.is_for_switch = cn(self.cleaned_data["is_for_switch"], False)
        event.is_for_r_active = cn(self.cleaned_data["is_for_r_active"], False)
        event.is_for_active = cn(self.cleaned_data["is_for_active"], False)
        event.is_for_submisive = cn(
         self.cleaned_data["is_for_submisive"], False)
        event.is_for_r_submissive = cn(
         self.cleaned_data["is_for_r_submissive"], False)
        event.is_for_neutral = cn(self.cleaned_data["is_for_neutral"], False)
        event.is_for_r_dominant = cn(
         self.cleaned_data["is_for_r_dominant"], False)
        event.is_for_dominant = cn(self.cleaned_data["is_for_dominant"], False)
        event.other_preferences = self.cleaned_data["other_preferences"]
        if event.pubdate is None:
            event.pubdate = datetime.datetime.now()
        imgdelete = self.cleaned_data["delete_image"]
        if imgdelete is True:
            event.image = None
        else:
            event.image = self.cleaned_data["image"]

        if commit:
            event.save()
        return event


class PartyDividerForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    descr = forms.CharField(max_length=1500, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = PartyDivider
        fields = ("title", "descr", "image",)

    def save(self, event_id, commit=True):
        event = super(PartyDividerForm, self).save(commit=False)
        event.title = self.cleaned_data["title"]
        event.descr = self.cleaned_data["descr"]
        event.image = self.cleaned_data["image"]
        event.from_event = event_id

        if commit:
            event.save()
        return event


class TaxPanelForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    descr = forms.CharField(max_length=1500, required=False)
    image = forms.ImageField(required=False)
    tax_type = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TaxPanel
        fields = ("title", "descr", "image", 'tax_type')

    def save(self, event_id, commit=True):
        event = super(TaxPanelForm, self).save(commit=False)
        event.title = self.cleaned_data["title"]
        event.descr = self.cleaned_data["descr"]
        event.image = self.cleaned_data["image"]
        event.tax_type = cn(self.cleaned_data["tax_type"], False)
        event.from_event = event_id

        if commit:
            event.save()
        return event


class UserRoleForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    role_descr = forms.CharField(max_length=600, required=False)
    assigned_user = forms.CharField(max_length=11, required=False)
    alt_user = forms.CharField(max_length=150, required=False)
    tax_free = forms.BooleanField(required=False)
    aux_coordinator = forms.BooleanField(required=False)

    class Meta:
        model = UserRole
        fields = (
         "title", "role_descr", "assigned_user", "alt_user", "tax_free",
         "aux_coordinator",
         )

    def save(self, divider_id, commit=True):
        event = super(UserRoleForm, self).save(commit=False)
        event.title = self.cleaned_data["title"]
        event.role_descr = self.cleaned_data["role_descr"]
        event.assigned_user = 1
        event.tax_type = cn(self.cleaned_data["tax_type"], False)
        event.from_event = divider_id

        if commit:
            event.save()
        return event
