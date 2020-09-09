from django import forms
from .models import Event
# from rekruter.models import User
from meetap.core.classes import checkifnull as cn
import datetime


class EventForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
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

    class Meta:
        model = Event
        fields = ()  # "__all__"

    def save(self, user_id, commit=True):
        event = (EventForm, self).save(commit=False)
        print("string testowy!!!")
        event.title = cn(self.cleaned_data["title"], "Debugtitle")
        event.body = cn(self.cleaned_data["body"], False)
        event.image = cn(self.cleaned_data["image"], False)
        event.datefrom = cn(self.cleaned_data["datefrom"], False)
        event.dateto = cn(self.cleaned_data["dateto"], False)
        event.owner = user_id
        event.is_commercial = cn(self.cleaned_data["is_commercial"], False)
        event.is_mass_event = cn(self.cleaned_data["is_mass_event"], False)
        event.is_adult_only = cn(self.cleaned_data["is_adult_only"], False)
        event.is_alcohol = cn(self.cleaned_data["is_alcohol"], False)
        event.is_tobacco = cn(self.cleaned_data["is_tobacco"], False)
        event.other_drugs = cn(self.cleaned_data["other_drugs"], False)
        event.is_sex_party = cn(self.cleaned_data["is_sex_party"], False)
        event.is_paid = cn(self.cleaned_data["is_paid"], False)
        event.is_for_straight = cn(self.cleaned_data["is_for_straight"], False)
        event.is_for_gay = cn(self.cleaned_data["is_for_gay"], False)
        event.is_for_bi = cn(self.cleaned_data["is_for_bi"], False)
        event.is_for_trans = cn(self.cleaned_data["is_for_trans"], False)
        event.is_for_other = cn(self.cleaned_data["is_for_other"], False)
        event.is_for_passive = cn(self.cleaned_data["is_for_passive"], False)
        event.is_for_r_passive = cn(self.cleaned_data["is_for_r_passive"], False)
        event.is_for_switch = cn(self.cleaned_data["is_for_switch"], False)
        event.is_for_r_active = cn(self.cleaned_data["is_for_r_active"], False)
        event.is_for_active = cn(self.cleaned_data["is_for_active"], False)
        event.is_for_submisive = cn(self.cleaned_data["is_for_submisive"], False)
        event.is_for_r_submissive = cn(self.cleaned_data["is_for_r_submissive"], False)
        event.is_for_neutral = cn(self.cleaned_data["is_for_neutral"], False)
        event.is_for_r_dominant = cn(self.cleaned_data["is_for_r_dominant"], False)
        event.is_for_dominant = cn(self.cleaned_data["is_for_dominant"], False)
        event.other_preferences = cn(self.cleaned_data["other_preferences"], False)
        event.pubdate = datetime.datetime.now()

        if commit:
            event.save()
        return event
